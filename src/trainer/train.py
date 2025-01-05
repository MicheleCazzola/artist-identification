from dataclasses import dataclass, field
import json
import logging
import os
import time
from statistics import mean

import torch
import torch.nn as nn
import torch.optim as optim
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, Subset
from torchvision import transforms
from torchvision.transforms import Compose

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
        return iter((self.train_losses, self.train_accuracies, self.val_losses, self.val_accuracies))
    
    
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
        self.step_size: int = None
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
        self.best_model_path: str = None
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
        self.step_size = cfg.train.scheduler_step_size
        self.gamma = cfg.train.scheduler_gamma
        self.weight_decay = cfg.train.weight_decay
        self.top_k = cfg.train.top_k
        self.train_accuracy = cfg.train.train_accuracy
        self.best_model_path = cfg.path.best_model_path
        self.sanity_check = cfg.train.sanity_check
        self.save_models = cfg.train.save_models
        self.resume_training = cfg.train.resume_training
        self.trained_model_path = cfg.path.trained_model_path
        
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
            self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, self.step_size, self.gamma)
        elif scheduler == "constant" or scheduler is None:
            self.scheduler = None
        else:
            raise ValueError(f"Scheduler {scheduler} not supported")
        
    def _save_checkpoint(self, epoch: int = None):
        checkpoint = {
            "epoch": epoch,
            "model_state_dict": self.model.state_dict(),
            "optimizer_state_dict": self.optimizer.state_dict()
        }
        epoch_info = f"_{epoch}" if epoch is not None else ""
        torch.save(checkpoint, f"{self.best_model_path}{epoch_info}.pth")
        
    def _load_checkpoint(self, model_path: str):
        checkpoint = torch.load(model_path, weights_only=True)
        self.model.load_state_dict(checkpoint["model_state_dict"])
        self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    
    @execution_time
    def train(self):
        
        if self.resume_training:
            self._load_checkpoint(self.trained_model_path)

        val_losses, val_accuracies = [], []
        train_losses, train_accuracies = [], []
        best_accuracy = None
        best_num_epochs = None
        
        if self.sanity_check:    
            train_loss, train_accuracy = self.training_eval()
            val_loss, val_accuracy = self.validate()
            
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
        
        for epoch in range(self.num_epochs):
            
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
                
            if self.save_models:
                self._save_checkpoint(epoch + 1)
                
            val_loss, val_accuracy = self.validate()
            
            if best_accuracy is None or val_accuracy > best_accuracy or \
                (val_accuracy == best_accuracy and val_loss < val_losses[best_num_epochs - 1]):
                    best_accuracy = val_accuracy
                    best_num_epochs = epoch + 1
                    self._save_checkpoint()

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

            # Scheduler is None if learning rate is constant
            if self.scheduler is not None:
                self.scheduler.step()

        self.best_num_epochs = best_num_epochs
        logging.info(f"Best validation accuracy: {best_accuracy:.3f} at epoch {best_num_epochs}")

        self.training_results = TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs)
    
    def training_eval(self) -> EvaluationResult:
        losses, top_1_acc, _, _, top_k_weighted_mca, _ = self.evaluate(self.trainloader)
        return losses, top_k_weighted_mca
    
    def validate(self) -> EvaluationResult:
        losses, top_1_acc, _, _, top_k_weighted_mca, _ = self.evaluate(self.validloader)
        return losses, top_k_weighted_mca
    
    @execution_time
    def test(self, model_path: str = None, testloader: DataLoader = None, save_path: str = None):
        
        model_path = model_path if model_path is not None else f"{self.best_model_path}.pth"
        self._load_checkpoint(model_path)
        
        if save_path is not None:
            
            assert testloader is not None, "Missing dataloader for working set"
            
            self.predict(testloader, save_path)
        else:
            test_result = self.evaluate(self.testloader)
            
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
        
        plt.ylim(-0.05, max(values[0] + values[1]) + 1)
            
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