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

from ..config.config import Config
from ..model.network import MultiBranchArtistNetwork
from ..utils.utils import execution_time
from .metrics import Metrics

@dataclass
class TrainingResult:
    train_losses: list = field(default_factory=list)
    train_accuracies: list = field(default_factory=list)
    val_losses: list = field(default_factory=list)
    val_accuracies: list = field(default_factory=list)
    best_num_epochs: int = None
    
    def __iter__(self):
        return iter((self.train_losses, self.train_accuracies, self.val_losses, self.val_accuracies, self.best_num_epochs))
    
@dataclass
class EvaluationResult:
    loss: float = field(default_factory=list)
    metrics: dict = field(default_factory=dict.fromkeys(["top-1_accuracy", "top-5_accuracy", "mca", "weighted_top-5_mca", "confusion_matrix"]))

    def __iter__(self):
        return iter((self.loss, *self.metrics.values()))
    

class Trainer: 
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
        self.log_frequency: int = None
        
        self.num_epochs: int = None
        self.lr: float = None
        self.momentum: float = None
        self.milestones: list[int] = None
        self.gamma: float = None
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
        self.saved_model_path: str = None
        self.save_models: bool = None
        
        self.training_results: TrainingResult = None
        self.test_results: EvaluationResult = None
        
    def build(self, cfg: Config):
        
        self.device = torch.device(cfg.env.device)
        self.train_log_frequency = cfg.train.train_log_frequency
        self.val_log_frequency = cfg.train.val_log_frequency
        self.num_epochs = cfg.train.num_epochs
        self.lr = cfg.train.lr
        self.momentum = cfg.train.momentum
        self.milestones = list(cfg.train.scheduler_milestones)
        self.gammas = cfg.train.scheduler_gammas
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
        
        self.metrics = Metrics(num_classes=cfg.train.num_classes, top_k=cfg.train.top_k)
        
        self.training_results: TrainingResult = TrainingResult()
        self.test_results: EvaluationResult = EvaluationResult(
            [], 
            dict(zip(
                ["top-1_accuracy", "top-5_accuracy", "mca", "weighted_top-5_mca", "confusion_matrix"],
                [0,0,0,0, [[0] * cfg.train.num_classes] * cfg.train.num_classes]
            ))
        )
        
        self.model = self.model.to(self.device)
        self.metrics = self.metrics.to(self.device)
        
    def _set_precision(self, precision: int):
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
        
        if criterion == "cross_entropy":
            self.criterion = nn.CrossEntropyLoss()
        elif criterion == "weighted_cross_entropy":
            weights = self._get_weights().to(self.device)
            self.criterion = nn.CrossEntropyLoss(weight=weights)
        else:
            raise ValueError(f"Criterion {criterion} not supported")
        
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
        
        if scheduler == "step_lr":
            assert len(self.gammas) == 1, "Only one gamma value is allowed for MultiStepLR"
            self.scheduler: optim.lr_scheduler.MultiStepLR = optim.lr_scheduler.MultiStepLR(
                self.optimizer, 
                self.milestones, 
                self.gammas[0]
            )
        elif scheduler == "custom_step_lr":
            self.scheduler: CustomMultiStepLR = CustomMultiStepLR(
                self.optimizer, 
                self.milestones, 
                self.gammas
            )
        elif scheduler == "constant" or scheduler is None:
            self.scheduler = None
        else:
            raise ValueError(f"Scheduler {scheduler} not supported")
        
    def _save_checkpoint(self, epoch: int, model_path: str):
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
        saved_path = f"{model_path}_{epoch}.pth.tar"
        if os.path.exists(saved_path):
            os.remove(saved_path)
            
            logging.info(f"Checkpoint removed at {saved_path}")
        else:
            logging.error(f"Checkpoint {saved_path} not found")
        
    def _load_checkpoint(self, model_path: str):
        checkpoint = torch.load(model_path, weights_only=True)
        
        self.start_epoch = checkpoint["epoch"]
        self.model.load_state_dict(checkpoint["model_state_dict"])
        self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        self.optimizer.param_groups[0]["lr"] = self.lr
        self.training_results = checkpoint["training_results"]
        
        logging.info(f"Checkpoint loaded from {model_path}")
        
    def _load_pretrained(self, model_path: str):
        checkpoint = torch.load(model_path, weights_only=True)
        self.model.load_state_dict(checkpoint["model_state_dict"])
        
        logging.info(f"Pretrained model loaded from {model_path}")
    
    @execution_time
    def train(self):
        
        val_losses, val_accuracies = [], []
        train_losses, train_accuracies = [], []
        best_accuracy = None
        best_num_epochs = None
        
        if self.resume_training:
            self._load_checkpoint(self.trained_model_path)
            train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs = self.training_results
            
            assert self.start_epoch < self.num_epochs, "Training already completed"
        
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
        
        if train_losses and val_losses and val_accuracies:
            logging.info(f"Last training loss: {train_losses[-1]:.5f}")
            logging.info(f"Last validation loss: {val_losses[-1]:.5f}")
            logging.info(f"Last validation accuracy: {val_accuracies[-1]:.3f}")
        if train_accuracies:
            logging.info(f"Last training accuracy: {train_accuracies[-1]:.3f}")
            
        if val_accuracies:
            logging.info(f"Best validation accuracy: {val_accuracies[best_num_epochs - 1]:.3f} at epoch {best_num_epochs}")
        
        for epoch in range(self.start_epoch, self.num_epochs):
            
            current_lr = self.optimizer.param_groups[0]["lr"]
            logging.info(f"Start of Epoch {epoch+1}, LR: {current_lr}, WD: {self.weight_decay}")
            
            current_step = 0
            epoch_losses = []
            
            self.model.train()
            for (inputs, labels) in self.trainloader:

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

            if self.train_accuracy:
                train_loss, train_accuracy = self.training_eval()
            else:
                train_loss = mean(epoch_losses)
                train_accuracy = None
                
            val_loss, val_accuracy = self.validate()

            logging.info(f"End of Epoch {epoch+1}")
            
            if self.train_accuracy:
                logging.info(f"Training accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
            else:
                logging.info(f"Training loss: {train_loss:.3f}")
                
            logging.info(f"Validation accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")

            val_losses.append(val_loss)
            val_accuracies.append(val_accuracy)
            train_losses.append(train_loss)
            
            if self.train_accuracy:
                train_accuracies.append(train_accuracy)
                
            
            self.training_results = TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs)
            if self.save_models and ((epoch + 1) % self.save_models_step == 0 or (epoch + 1) == self.num_epochs):
                
                self._save_checkpoint(epoch + 1, self.saved_model_path)
                
            if best_num_epochs is None or val_accuracy > val_accuracies[best_num_epochs - 1] \
                or (math.isclose(val_accuracies[best_num_epochs - 1], val_accuracy, abs_tol=1e-6) and val_loss < val_losses[best_num_epochs - 1]):
                    
                    if best_num_epochs is not None:
                        self._remove_checkpoint(best_num_epochs, self.saved_best_model_path)
                    
                    best_accuracy = val_accuracy
                    best_num_epochs = epoch + 1
                    self.training_results.best_num_epochs = best_num_epochs
                    self._save_checkpoint(best_num_epochs, self.saved_best_model_path)

            # Scheduler is None if learning rate is constant
            if self.scheduler is not None:
                self.scheduler.step()

        self.best_num_epochs = best_num_epochs
        logging.info(f"Best validation accuracy: {best_accuracy:.3f} at epoch {best_num_epochs}")

        self.training_results = TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs)
    
    def training_eval(self) -> EvaluationResult:
        losses, _, _, _, top_k_weighted_mca, _ = self.evaluate(self.trainloader)
        return losses, top_k_weighted_mca
    
    def validate(self) -> EvaluationResult:
        losses, _, _, _, top_k_weighted_mca, _ = self.evaluate(self.validloader)
        return losses, top_k_weighted_mca
    
    @execution_time
    def test(self, model_path: str = None, testloader: DataLoader = None, save_path: str = None):
        
        model_path = model_path if model_path is not None else f"{self.saved_best_model_path}_{self.best_num_epochs}.pth.tar"
        self._load_pretrained(model_path)
        
        if save_path is not None:
            
            assert testloader is not None, "Missing dataloader for working set"
            
            self.predict(testloader, save_path)
        else:
            testloader = self.testloader if testloader is None else testloader
            test_result = self.evaluate(testloader)
            
            self.test_results = test_result

    @torch.no_grad()
    def evaluate(self, dataloader: DataLoader) -> EvaluationResult:
        
        self.model.eval()

        losses = []
        data_len = 0
        current_step = 0
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
        
            # Calculate accuracy
            self.metrics.update(outputs, labels)
            
            current_step += 1

        metrics = self.metrics.compute()
        self.metrics.reset()
        
        return EvaluationResult(mean(losses), metrics)
    
    @torch.no_grad()
    def predict(self, testloader: DataLoader, save_path: str) -> torch.Tensor:
        self.model.eval()
        
        predictions = []
        images = []
        current_step = 0
        for inputs, input_names in testloader:
            inputs = inputs.to(self.device)
            outputs = self.model(inputs)
            
            predicted = torch.topk(outputs, self.top_k, dim=1).indices.cpu().tolist()
            predictions.extend(predicted)
            
            for input_name in input_names:
                images.append(input_name.split("/")[-1])
                
            if (current_step + 1) % self.val_log_frequency == 0:
                logging.info(f"Prediction iteration {current_step + 1}")
                
            current_step += 1

        self._save_predictions(images, predictions, save_path)
    
    def _save_predictions(self, images: list, predictions: list[list[int]], save_path: str):
        with open(save_path, "w") as f:
            classes = ",".join([f"Class{i}" for i in range(1, self.top_k + 1)])
            f.write(f"Image Name,{classes}\n")
            for image, pred in zip(images, predictions):
                f.write(f"{image},{','.join(self.categories[p].replace('_', '-') for p in pred)}\n")
        
        
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
        id = time.strftime("%Y%m%d_%H%M%S")
        
        full_save_path = f"{save_path}/{id}"
        os.makedirs(full_save_path)
        
        self._save_files(cfg, full_save_path, transformations, training_time, test_time)
        
        if not inference_only:
            self._save_plots("Loss", full_save_path)
            self._save_plots("Accuracy", full_save_path)
        if not train_only:
            self._save_confusion_matrix(full_save_path)
    
    def _save_plots(self, name: str, save_path: str):
        
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
        result = cfg.to_dict()
        result["transformations"] = transformations.to_dict()
        result["training_time"] = training_time
        result["test_time"] = test_time
        
        result.update(self.training_results.__dict__)
        result.update(self.test_results.__dict__)
        
        with open(f"{save_path}/result.json", "w") as f:
            json.dump(result, f, indent=4)
            
    def _save_confusion_matrix(self, save_path: str):
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