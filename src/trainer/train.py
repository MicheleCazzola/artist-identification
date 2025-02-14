from dataclasses import dataclass, field
import json
import logging
import math
import os
import time
from statistics import mean

import torch
import torch.nn as nn
import torch.optim as optim
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, Subset

from src.trainer.scheduler import CustomMultiStepLR
from src.transformations.transformations import Transforms
from src.config.config import Config
from src.model.network import MultiBranchArtistNetwork
from src.utils.utils import execution_time
from src.trainer.metrics import Metrics

@dataclass
class TrainingResult:
    """
    Class to store the training results
    
    Attributes:
    -----------
    train_losses: list
        List of training losses
    train_accuracies: list
        List of training accuracies (weighted top-5 MCA)
    val_losses: list
        List of validation losses
    val_accuracies: list
        List of validation accuracies (weighted top-5 MCA)
    best_num_epochs: int
        Best number of epochs for the validation accuracy (weighted top-5 MCA)
    """
    train_losses: list = field(default_factory=list)
    train_accuracies: list = field(default_factory=list)
    val_losses: list = field(default_factory=list)
    val_accuracies: list = field(default_factory=list)
    best_num_epochs: int = None
    
    def __iter__(self):
        return iter((self.train_losses, self.train_accuracies, self.val_losses, self.val_accuracies, self.best_num_epochs))
    
@dataclass
class EvaluationResult:
    """
    Class to store the evaluation results
    
    Attributes:
    -----------
    loss: float
        Loss value
    metrics: dict
        Dictionary containing the metrics (top-1 accuracy, top-5 accuracy, MCA, weighted top-5 MCA, confusion matrix)
    """
    loss: float = field(default_factory=list)
    metrics: dict = field(default_factory=dict.fromkeys(["top-1_accuracy", "top-5_accuracy", "mca", "weighted_top-5_mca", "confusion_matrix"]))

    def __iter__(self):
        return iter((self.loss, *self.metrics.values()))
    

class Trainer: 
    """
    Class to handle training and evaluation of the model.
    
    Attributes:
    -----------
    model: MultiBranchArtistNetwork
        Model to be trained
    trainloader: DataLoader
        DataLoader for the training set
    validloader: DataLoader
        DataLoader for the validation set
    testloader: DataLoader
        DataLoader for the test set
    categories: list
        List of categories in the dataset
    device: torch.device
        Device to use for training and evaluation (CPU or cuda)
    num_epochs: int
        Number of epochs to train the model
    lr: float
        Learning rate
    momentum: float
        Momentum for the optimizer (SGD only)
    milestones: list
        Milestones for the scheduler
    scheduler_factors: list
        Gamma values for the scheduler
    weight_decay: float
        Weight decay for the optimizer
    criterion: str
        Criterion for the loss function
    optimizer: str
        Optimizer to use (Adam, AdamW, SGD)
    scheduler: str
        Learning rate scheduler to use (MultiStepLR, CustomMultiStepLR, None)
    metrics: Metrics
        Metrics to use for evaluation
    train_accuracy: bool
        Flag to enable training accuracy calculation
    sanity_check: bool
        Flag to enable sanity check before training
    data_type: torch.dtype
        Data type for the model
    best_num_epochs: int
        Best number of epochs for the validation accuracy (weighted top-5 MCA)
    saved_model_path: str
        Path to save the model
    saved_best_model_path: str
        Path to save the best model across all training epochs, to use in evaluation
    save_models: bool
        Flag to enable saving all models
    training_results: TrainingResult
        Training results class
    test_results: EvaluationResult
        Evaluation results class
    train_log_frequency: int
        Log frequency for training
    val_log_frequency: int
        Log frequency for validation
    save_models_step: int
        Step for saving models during training
    resume_training: bool
        Flag to resume training from a checkpoint
    trained_model_path: str
        Path to the trained model checkpoint or model for evaluation
    start_epoch: int
        Start epoch for training (used for resuming training)
    top_k: int
        Top-k accuracy level
        
    Methods:
    --------
    build(cfg: Config)
        Build the trainer with the configuration
        
    _set_precision(precision)
        Set the precision for the model
    
    _prepare_training(criterion, optimizer, scheduler)
        Prepare the training with the criterion, optimizer, and scheduler from the configuration
        
    _get_weights()
        Get the weights for the weighted cross entropy loss
    
    _save_checkpoint(epoch, model_path)
        Save a checkpoint at the specified epoch
    
    _remove_checkpoint(epoch, model_path)
        Remove a checkpoint at the specified epoch
        
    _load_checkpoint(model_path)
        Load a checkpoint from the specified path (used when resuming training)
        
    _load_pretrained(model_path)
        Load a pretrained model from the specified path (used in evaluation)
        
    train()
        Train the model
        
    training_eval() -> EvaluationResult
        Wrapper for evaluation on the training set
    
    validate() -> EvaluationResult
        Wrapper for evaluation on the validation set
        
    test(model_path, testloader)
        Wrapper for evaluation on the test set
        
    evaluate(dataloader) -> EvaluationResult
        Evaluate the model on the given dataloader
        
    save_results(cfg, save_path, ...) 
        Save the results to the specified path
    
    _save_plots(name, save_path)
        Save the plots for the training and validation losses and accuracies
    
    _save_files(cfg, save_path, ...)
        Save the configuration, results, and training and test times to the specified path
        
    _save_confusion_matrix(save_path)
        Save the confusion matrix plot to the specified path
    """
    
    def __init__(
        self,
        model: MultiBranchArtistNetwork, 
        trainloader: DataLoader,
        validloader: DataLoader,
        testloader: DataLoader,
        categories: list
    ):
        self.model: MultiBranchArtistNetwork = model
        self.trainloader: DataLoader = trainloader
        self.validloader: DataLoader = validloader
        self.testloader: DataLoader = testloader
        self.categories: list = categories
        
        self.device: torch.device = None
        
        self.num_epochs: int = None
        self.lr: float = None
        self.momentum: float = None
        self.milestones: list[int] = None
        self.scheduler_factors: list[float] = None
        self.weight_decay: float = None
        
        self.criterion: str = None
        self.optimizer: str = None
        self.scheduler: str = None
        self.metrics: Metrics = None
        self.train_accuracy: bool = None
        self.sanity_check: bool = None
        
        self.data_type: torch.dtype = torch.float32
        
        self.best_num_epochs: int = None
        self.saved_model_path: str = None
        self.save_models: bool = None
        
        self.training_results: TrainingResult = None
        self.test_results: EvaluationResult = None
        
    def build(self, cfg: Config):
        """
        
        Build the trainer with the configuration. Parameters are read from CLI or configuration file (default).
        
        cfg: Config
            Configuration for the trainer
        """
        
        self.device = torch.device(cfg.env.device)
        self.train_log_frequency = cfg.train.train_log_frequency
        self.val_log_frequency = cfg.train.val_log_frequency
        self.num_epochs = cfg.train.num_epochs
        self.lr = cfg.train.lr
        self.momentum = cfg.train.momentum
        self.milestones = list(cfg.train.scheduler_milestones)
        self.scheduler_factors = list(cfg.train.scheduler_factors)
        self.weight_decay = cfg.train.weight_decay
        self.top_k = cfg.train.top_k
        self.train_accuracy = cfg.train.train_accuracy
        self.saved_model_path = cfg.path.saved_model_path
        self.saved_best_model_path = cfg.path.saved_best_model_path
        self.sanity_check = cfg.train.sanity_check
        self.save_models = cfg.train.save_models
        self.save_models_step = cfg.train.save_models_step
        self.resume_training = cfg.train.resume_training
        self.trained_model_path = cfg.path.trained_model_path
        self.start_epoch = 0
        
        self._set_precision(cfg.model.precision)
        self._prepare_training(cfg.train.criterion, cfg.train.optimizer, cfg.train.scheduler)
        
        self.metrics = Metrics(num_classes=self.model.num_classes, top_k=cfg.train.top_k)
        
        self.training_results: TrainingResult = TrainingResult()
        self.test_results: EvaluationResult = EvaluationResult(
            [], 
            dict(zip(
                ["top-1_accuracy", "top-5_accuracy", "mca", "weighted_top-5_mca", "confusion_matrix"],
                [0,0,0,0, [[0] * self.model.num_classes] * self.model.num_classes]
            ))
        )
        
        self.model = self.model.to(self.device)
        self.metrics = self.metrics.to(self.device)
        
    def _set_precision(self, precision: int):
        """Set model precision (not used in reality)"""
        if precision == 16:
            self.data_type = torch.float16
        elif precision == 32:
            self.data_type = torch.float32
        elif precision == 64:
            self.data_type = torch.float64
        elif precision == 8:
            self.data_type = torch.float8_e5m2
        else:
            raise ValueError(f"Precision {precision} not supported")
            
    def _get_weights(self):
        """Get the weights for the weighted cross entropy loss"""
        
        if isinstance(self.trainloader.dataset, Subset):
            occ_labels = self.trainloader.dataset.dataset.get_histogram(self.trainloader.dataset.indices)
        else:
            occ_labels = self.trainloader.dataset.get_histogram()
        
        weights = 1 / occ_labels
        return weights / weights.sum()
        
    def _prepare_training(
        self,
        criterion: str,
        optimizer: str,
        scheduler: str
    ):
        """Setup the criterion, optimizer, and scheduler for training"""
        
        # Weighted cross-entropy not used in reality, only some preliminary experiments
        # leading to conflicting results depending on the architecture
        if criterion == "cross_entropy":
            self.criterion = nn.CrossEntropyLoss()
        elif criterion == "weighted_cross_entropy":
            weights = self._get_weights().to(self.device)
            self.criterion = nn.CrossEntropyLoss(weight=weights)
        else:
            raise ValueError(f"Criterion {criterion} not supported")
        
        # AdamW is the best trade-off between Adam fast convergence
        # and SGD better generalization: Adam converges fast but overfits more,
        # SGD converges too slow
        if optimizer == "adam":
            self.optimizer: optim.Adam = optim.Adam(
                self.model.parameters(), 
                lr=self.lr, 
                weight_decay=self.weight_decay
            )
        elif optimizer == "adamw":
            self.optimizer: optim.AdamW = optim.AdamW(
                self.model.parameters(), 
                lr=self.lr, 
                weight_decay=self.weight_decay
            )
        elif optimizer == "sgd":
            self.optimizer: optim.SGD = optim.SGD(
                self.model.parameters(), 
                lr=self.lr, 
                momentum=self.momentum, 
                weight_decay=self.weight_decay
            )
        else:
            raise ValueError(f"Optimizer {optimizer} not supported")
        
        # Custom scheduler for different gamma values at each milestone is used in last runs
        # MultiStepLR is used before, when running for few epochs
        # In some cases, no scheduling is used
        if scheduler == "multistep_lr":
            assert len(self.scheduler_factors) == 1, "Only one gamma value is allowed for MultiStepLR"
            self.scheduler: optim.lr_scheduler.MultiStepLR = optim.lr_scheduler.MultiStepLR(
                self.optimizer, 
                self.milestones, 
                self.scheduler_factors[0]
            )
        elif scheduler == "custom_step_lr":
            self.scheduler: CustomMultiStepLR = CustomMultiStepLR(
                self.optimizer, 
                self.milestones, 
                self.scheduler_factors
            )
        elif scheduler == "constant" or scheduler is None:
            self.scheduler = None
        else:
            raise ValueError(f"Scheduler {scheduler} not supported")
        
    def _save_checkpoint(self, epoch: int, model_path: str):
        """
        Saves a checkpoint at the specified epoch. The checkpoint contains the model state dictionary, optimizer state dictionary,
        the epoch and the training results at the specified epoch.
        """
        checkpoint = {
            "epoch": epoch,
            "model_state_dict": self.model.state_dict(),
            "optimizer_state_dict": self.optimizer.state_dict(),
            "training_results": self.training_results
        }
        save_path = f"{model_path}_{epoch}.pth.tar"
        torch.save(checkpoint, save_path)
        
        logging.info(f"Checkpoint saved at {save_path}")
        
    def _remove_checkpoint(self, epoch: int, model_path: str):
        """
        Removes a checkpoint at the specified epoch. If the checkpoint is not found, a warning is issued.
        """
        saved_path = f"{model_path}_{epoch}.pth.tar"
        if os.path.exists(saved_path):
            os.remove(saved_path)
            
            logging.info(f"Checkpoint removed at {saved_path}")
        else:
            logging.warning(f"Checkpoint {saved_path} not found")
        
    def _load_checkpoint(self, model_path: str):
        """Loads a checkpoint from the specified path. Sets the optimizer learning rate to the current value."""
        
        checkpoint = torch.load(model_path, weights_only=True)
        
        self.start_epoch = checkpoint["epoch"]
        self.model.load_state_dict(checkpoint["model_state_dict"])
        self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        self.optimizer.param_groups[0]["lr"] = self.lr
        self.training_results = checkpoint["training_results"]
        
        logging.info(f"Checkpoint loaded from {model_path}")
        
    def _load_pretrained(self, model_path: str):
        """Loads a pretrained model from the specified path. Used in evaluation."""
        checkpoint = torch.load(model_path, weights_only=True)
        
        # Check if the model is saved with the correct name and if it is a checkpoint or a pretrained model
        if "model_state_dict" in checkpoint:
            if not model_path.endswith(".tar"):
                logging.warning(f"Checkpoint {model_path} not properly saved, please follow naming conventions")
                
            model_state_dict = checkpoint["model_state_dict"]
        else:
            if not model_path.endswith(".pth"):
                logging.warning(f"Model {model_path} not properly saved, please follow naming conventions")
            model_state_dict = checkpoint
        
        # Load the state dictionary
        self.model.load_state_dict(model_state_dict)
        
        logging.info(f"Pretrained model loaded from {model_path}")
    
    @execution_time
    def train(self):
        """
        Performs the training loop. If the resume_training flag is set, the training is resumed from the last checkpoint.
        
        The training results are stored in the training_results attribute.
        """
        
        val_losses, val_accuracies = [], []
        train_losses, train_accuracies = [], []
        best_accuracy = None
        best_num_epochs = None
        
        # Load the checkpoint if resuming training
        # Update the training results with the loaded results
        if self.resume_training:
            self._load_checkpoint(self.trained_model_path)
            train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs = self.training_results
            
            assert self.start_epoch < self.num_epochs, "Training already completed"
        
        # Sanity check before training: evaluate the model before training both on training and validation set
        # Used to check if the evaluation process works, without any training (and detect possible bugs)
        if self.sanity_check:    
            train_loss, train_accuracy = self.training_eval()
            val_loss, val_accuracy = self.validate()
            
            if not self.resume_training:
                train_losses.append(train_loss)
                
                if self.train_accuracy:
                    train_accuracies.append(train_accuracy)
                
                val_losses.append(val_loss)
                val_accuracies.append(val_accuracy)
            
            logging.info(f"Sanity check - Before training")
                
            if self.train_accuracy:
                logging.info(f"Training accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
            else:
                logging.info(f"Training loss: {train_loss:.3f}")
                
            logging.info(f"Validation accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")
            
        logging.info(f"Starting training, from epoch {self.start_epoch + 1} to {self.num_epochs}")
        
        # Log the last training and validation losses and accuracies, if present
        if train_losses and val_losses and val_accuracies:
            logging.info(f"Last training loss: {train_losses[-1]:.5f}")
            logging.info(f"Last validation loss: {val_losses[-1]:.5f}")
            logging.info(f"Last validation accuracy: {val_accuracies[-1]:.3f}")
        if train_accuracies:
            logging.info(f"Last training accuracy: {train_accuracies[-1]:.3f}")
            
        if val_accuracies:
            logging.info(f"Best validation accuracy: {val_accuracies[best_num_epochs - 1]:.3f} at epoch {best_num_epochs}")
        
        # Training loop
        for epoch in range(self.start_epoch, self.num_epochs):
            
            current_lr = self.optimizer.param_groups[0]["lr"]
            logging.info(f"Start of Epoch {epoch+1}, LR: {current_lr}, WD: {self.weight_decay}")
            
            current_step = 0
            epoch_losses = []
            
            self.model.train()
            
            # Training epoch
            for (inputs, labels) in self.trainloader:

                # Data loading
                inputs = inputs.type(self.data_type).to(self.device)
                labels = labels.to(self.device)

                # Forward pass
                self.optimizer.zero_grad()
                
                outputs = self.model(inputs)
                
                loss = self.criterion(outputs, labels)
                
                epoch_losses.append(loss.item())

                # Backward pass
                loss.backward()
                self.optimizer.step()

                if (current_step + 1) % self.train_log_frequency == 0 or current_step == 0:
                    logging.info(f"Training epoch {epoch + 1}, Iteration {current_step + 1}, "+
                                 f"Loss: {mean(epoch_losses[current_step + 1 - self.train_log_frequency : current_step + 1]):.5f}")
                
                current_step += 1

            # Training statistics
            if self.train_accuracy:
                train_loss, train_accuracy = self.training_eval()
            else:
                train_loss = mean(epoch_losses)
                train_accuracy = None
            
            # Validation
            val_loss, val_accuracy = self.validate()

            logging.info(f"End of Epoch {epoch+1}")
            
            if self.train_accuracy:
                logging.info(f"Training accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
            else:
                logging.info(f"Training loss: {train_loss:.3f}")
                
            logging.info(f"Validation accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")

            # Store the results
            val_losses.append(val_loss)
            val_accuracies.append(val_accuracy)
            train_losses.append(train_loss)
            
            if self.train_accuracy:
                train_accuracies.append(train_accuracy)
                
            # Update training results
            self.training_results = TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs)
            
            # Save current checkpoint (if needed)
            if self.save_models and ((epoch + 1) % self.save_models_step == 0 or (epoch + 1) == self.num_epochs):
                self._save_checkpoint(epoch + 1, self.saved_model_path)
                
            # Save the best model (checkpoint) based on the validation accuracy
            if best_num_epochs is None or val_accuracy > val_accuracies[best_num_epochs - 1] \
                or (math.isclose(val_accuracies[best_num_epochs - 1], val_accuracy, abs_tol=1e-6) and val_loss < val_losses[best_num_epochs - 1]):
                    
                    # Could cause a warning: "Checkpoint not found"
                    # Completely unharmful, not found checkpoints are not removed with any program crash
                    if best_num_epochs is not None:
                        self._remove_checkpoint(best_num_epochs, self.saved_best_model_path)
                    
                    best_accuracy = val_accuracy
                    best_num_epochs = epoch + 1
                    self.training_results.best_num_epochs = best_num_epochs
                    self._save_checkpoint(best_num_epochs, self.saved_best_model_path)

            # Scheduler is None if learning rate is constant
            if self.scheduler is not None:
                self.scheduler.step()

        # Update best number of epochs
        self.best_num_epochs = best_num_epochs
        logging.info(f"Best validation accuracy: {best_accuracy:.3f} at epoch {best_num_epochs}")

        # Update training results (best number of epochs)
        self.training_results = TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs)
    
    def training_eval(self) -> EvaluationResult:
        """
        Wrapper for evaluation on the training set. Returns the losses and the top-k weighted MCA.
        """
        losses, _, _, _, top_k_weighted_mca, _ = self.evaluate(self.trainloader)
        return losses, top_k_weighted_mca
    
    def validate(self) -> EvaluationResult:
        """wrapper for evaluation on the validation set. Returns the losses and the top-k weighted MCA."""
        losses, _, _, _, top_k_weighted_mca, _ = self.evaluate(self.validloader)
        return losses, top_k_weighted_mca
    
    @execution_time
    def test(self, model_path: str = None, testloader: DataLoader = None):
        """
        Wrapper for evaluation on the test set.
        
        The test results are stored in the test_results attribute.
        
        model_path: str
            Path to the model checkpoint or pretrained model. If not specified, the current best model path is used.
        testloader: DataLoader
            DataLoader for the test. If not specified, the current testloader attribute is used.
        """
        
        model_path = model_path if model_path is not None else f"{self.saved_best_model_path}_{self.best_num_epochs}.pth.tar"
        testloader = self.testloader if testloader is None else testloader
        
        self._load_pretrained(model_path)
        test_result = self.evaluate(testloader)
        
        self.test_results = test_result

    @torch.no_grad()
    def evaluate(self, dataloader: DataLoader) -> EvaluationResult:
        """
        Performs evaluation on the given dataloader, using the given model and the criterion.
        
        dataloader: DataLoader
            DataLoader to evaluate the model on: could be training, validation, or test set
        
        Returns: EvaluationResult
            Containing the loss and the metrics (top-1 accuracy, top-5 accuracy, MCA, weighted top-5 MCA, confusion matrix)
        """
        
        self.model.eval()

        losses = []
        data_len = 0
        current_step = 0
        
        # Evaluation loop
        for inputs, labels in dataloader:

            data_len += inputs.size(0)

            inputs = inputs.to(self.device)
            labels = labels.to(self.device)

            # Forward pass
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)

            losses.append(loss.item())
            
            if (current_step + 1) % self.val_log_frequency == 0:
                logging.info(f"Validation iteration {current_step + 1}, " +
                             f"Loss: {mean(losses[current_step + 1 - self.val_log_frequency : current_step + 1]):.5f}")
            elif current_step == 0:
                logging.info(f"Validation iteration {current_step + 1}, Loss: {loss.item():.5f}")
        
            # Metrics update
            self.metrics.update(outputs, labels)
            
            current_step += 1

        # Metrics computation
        metrics = self.metrics.compute()
        
        # Reset the metrics
        self.metrics.reset()
        
        return EvaluationResult(mean(losses), metrics)
       
    def save_results(
        self,
        cfg: Config,
        save_path: str,
        transformations: Transforms,
        training_time: float,
        test_time: float,
        train_only: bool,
        inference_only: bool
    ):
        """
        Save training and/or evaluation results to the specified path. Generates a new folder with a (likely) unique ID, at the
        specified path.
        The results are saved in a JSON file, the plots for the training and validation losses and accuracies are saved as PNG files,
        and the confusion matrix is saved as a PNG file, all stored in the generated folder.
        
        cfg: Config
            Configuration for the trainer
        save_path: str
            Path to save the results
        transformations: Transforms
            Transformations used in the training
        training_time: float
            Training time for the whole process
        test_time: float
            Test time for the final inference
        train_only: bool
            Flag to indicate only training has been performed
        inference_only: bool
            Flag to indicate only inference has been performed
        """
        
        # Folder creation
        id = time.strftime("%Y%m%d_%H%M%S")
        
        full_save_path = f"{save_path}/{id}"
        os.makedirs(full_save_path)
        
        # Save JSON file with all data and results
        self._save_files(cfg, full_save_path, transformations, training_time, test_time)
        
        # Save plots and confusion matrix
        if not inference_only:
            self._save_plots("Loss", full_save_path)
            self._save_plots("Accuracy", full_save_path)
        if not train_only:
            self._save_confusion_matrix(full_save_path)
    
    def _save_plots(self, name: str, save_path: str):
        """
        Saves the plots for the training and validation losses and accuracies.+
        
        name: str
            Name of the plot (either "Loss" or "Accuracy")
        save_path: str
            Path to save the plots
        """
        
        assert name in ["Loss", "Accuracy"], f"Plot name must be either 'Loss' or 'Accuracy', found {name}"
        
        if name == "Loss":
            values = [self.training_results.train_losses, self.training_results.val_losses]
            labels = ["training loss", "validation loss"]
        else:
            values = [self.training_results.train_accuracies, self.training_results.val_accuracies]
            labels = ["training accuracy", "validation accuracy"]
        
        f = plt.figure(name)
        for val, label in zip(values, labels):
            plt.plot(val, label=label)
            plt.title(f"{name} vs. epochs")
        
        plt.xticks(ticks=range(self.num_epochs), labels=range(1, self.num_epochs + 1))
        plt.xlabel("Epochs")
        plt.ylabel(name)
        plt.grid(which="both")
        plt.legend()
        plt.xlim(-0.05, self.num_epochs - 0.8)
            
        f.savefig(f"{save_path}/{name.lower()}.png", dpi=300)
    
    def _save_files(self, cfg: Config, save_path: str, transformations: Transforms, training_time: float, test_time: float):
        """
        Save the configuration, results, and training and test execution times to the specified path.
        
        cfg: Config
            Configuration for the workflow
        save_path: str
            Path to save the files
        transformations: Transforms
            Transformations used in the process
        training_time: float
            Training time for the whole process
        test_time: float
            Test time for the final inference
        """
        
        # Merge the configuration with the results and the training and test times
        result = cfg.to_dict()
        result["transformations"] = transformations.to_dict()
        result["training_time"] = training_time
        result["test_time"] = test_time
        
        result.update(self.training_results.__dict__)
        result.update(self.test_results.__dict__)
        
        # Save to JSON file
        with open(f"{save_path}/result.json", "w") as f:
            json.dump(result, f, indent=4)
            
    def _save_confusion_matrix(self, save_path: str):
        """
        Save the confusion matrix plot to the specified path.
        
        save_path: str
            Path to save the confusion matrix plot
        """
        confusion_matrix = self.test_results.metrics["confusion_matrix"]
        
        f = plt.figure("Confusion Matrix", figsize=(16,12))
        plt.imshow(confusion_matrix, cmap="coolwarm", interpolation='nearest', vmin=0, vmax=1)
        plt.colorbar().ax.tick_params(labelsize=18)
        plt.xlabel("Predicted", fontsize=24, labelpad=10)
        plt.ylabel("Actual", fontsize=24, labelpad=10)
        plt.title("Confusion Matrix", fontsize=32, pad=20)
        
        plt.xticks(range(0, len(confusion_matrix), max(1, len(confusion_matrix) // 4)), fontsize=18)
        plt.yticks(range(0, len(confusion_matrix), max(1, len(confusion_matrix) // 4)), fontsize=18)
        
        f.savefig(f"{save_path}/confusion_matrix.png", dpi=100)