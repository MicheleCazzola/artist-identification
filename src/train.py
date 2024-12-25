from dataclasses import dataclass
import json
import logging
import os
from statistics import mean
import time
from matplotlib import pyplot as plt
import torch
import torch.optim as optim
import torch.nn as nn
from torch.backends import cudnn
from src.config import Config
from src.mutlti_branch_nn import MultibranchNetwork
from torch.utils.data import DataLoader
from torchvision.transforms import Compose
from torchmetrics.classification import Accuracy, MulticlassAccuracy, ConfusionMatrix, MulticlassConfusionMatrix
from torchvision import transforms

from src.utils import execution_time

class TrainingMetrics:
    def __init__(self, num_classes: int, top_k: int):
        
        if top_k > num_classes:
            logging.error(f"Top-k value {top_k} cannot be greater than number of classes {num_classes}")
        
        self.num_classes = num_classes
        self.top_k = top_k
        self.top_1_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes=num_classes)
        self.top_k_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes=num_classes, top_k=top_k)
        self.mca: MulticlassAccuracy = MulticlassAccuracy(num_classes=num_classes, average=None)
        self.confusion_matrix: MulticlassConfusionMatrix = MulticlassConfusionMatrix(num_classes=num_classes, normalize="true")
        # TODO: Add Kaggle score (optional)
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        self.top_1_accuracy.update(outputs, labels)
        self.top_k_accuracy.update(outputs, labels)
        self.mca.update(outputs, labels)
        self.confusion_matrix.update(outputs, labels)
        
    def reset(self):
        self.top_1_accuracy.reset()
        self.top_k_accuracy.reset()
        self.mca.reset()
        self.confusion_matrix.reset()
        
    def compute(self):
        top_1_accuracy = self.top_1_accuracy.compute().item()
        top_k_accuracy = self.top_k_accuracy.compute().item()
        mca_result = self.mca.compute().mean().item()
        top_1_confusion_matrix = self.confusion_matrix.compute().tolist()
        
        return {
            "top-1_accuracy": top_1_accuracy,
            f"top-{self.top_k}_accuracy": top_k_accuracy,
            "mca": mca_result,
            "confusion_matrix": top_1_confusion_matrix
        }
        
    def to(self, device: torch.device):
        return TrainingMetrics.from_metrics(
            self.num_classes,
            self.top_k,
            self.top_1_accuracy.to(device),
            self.top_k_accuracy.to(device),
            self.mca.to(device),
            self.confusion_matrix.to(device)
        )

    @staticmethod
    def from_metrics(num_classes, top_k, *metrics) -> "TrainingMetrics":
        new_metrics = TrainingMetrics(num_classes, top_k)
        new_metrics.top_1_accuracy = metrics[0]
        new_metrics.top_k_accuracy = metrics[1]
        new_metrics.mca = metrics[2]
        new_metrics.confusion_matrix = metrics[3]

        return new_metrics

@dataclass
class TrainingResult:
    train_losses: list
    train_accuracies: list
    val_losses: list
    val_accuracies: list
    best_num_epochs: int = None
    
    def __iter__(self):
        return iter((self.train_losses, self.train_accuracies, self.val_losses, self.val_accuracies))
    
    
@dataclass
class EvaluationResult:
    loss: float
    metrics: dict

    def __iter__(self):
        return iter((self.loss, *self.metrics.values()))
    

class Trainer: 
    def __init__(
        self,
        model: MultibranchNetwork, 
        trainloader: DataLoader,
        validloader: DataLoader,
        testloader: DataLoader,
    ):
        self.model: MultibranchNetwork = model
        self.trainloader: DataLoader = trainloader
        self.validloader: DataLoader = validloader
        self.testloader: DataLoader = testloader
        
        self.device: torch.device = None
        self.log_frequency: int = None
        
        self.num_epochs: int = None
        self.lr: float = None
        self.momentum: float = None
        self.step_size: int = None
        self.gamma: float = None
        self.weight_decay: float = None
        
        self.augment: bool = None
        self.aug_train: Compose = None
        self.norm_eval: transforms.Normalize = None
        
        self.criterion: str = None
        self.optimizer: str = None
        self.scheduler: str = None
        self.metrics: TrainingMetrics = None
        self.train_accuracy: bool = None
        
        self.data_type: torch.dtype = torch.float32
        
        self.best_num_epochs: int = None
        
        self.model_path: str = "./temp/best_model.pth"
        
        self.training_results: TrainingResult = None
        self.test_results: EvaluationResult = None
        
    def build(self, cfg: Config):
        self.device = torch.device(cfg.device)
        self.train_log_frequency = cfg.train_log_frequency
        self.val_log_frequency = cfg.val_log_frequency
        self.num_epochs = cfg.num_epochs
        self.lr = cfg.lr
        self.momentum = cfg.momentum
        self.step_size = cfg.scheduler_step_size
        self.gamma = cfg.scheduler_gamma
        self.weight_decay = cfg.weight_decay
        self.top_k = cfg.top_k
        self.augment = cfg.augment
        self.train_accuracy = cfg.train_accuracy
        
        self._set_precision(cfg.precision)
        self._prepare_training(cfg.criterion, cfg.optimizer, cfg.scheduler)
        
        self.metrics = TrainingMetrics(num_classes=cfg.num_classes, top_k=cfg.top_k)
        
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
        
    def add_aug_norm_transforms(self, transforms: dict):
        
        if not self.augment:
            self.aug_train = transforms["val"]
            self.norm_eval = transforms["val"]
        else:
            self.aug_train = transforms["train"]
            self.norm_eval = transforms["val"]
        
    def _prepare_training(
        self,
        criterion: str,
        optimizer: str,
        scheduler: str
    ):
        
        if criterion == "cross_entropy":
            self.criterion = nn.CrossEntropyLoss()
        else:
            raise ValueError(f"Criterion {criterion} not supported")
        
        if optimizer == "adam":
            self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=self.weight_decay)
        elif optimizer == "sgd":
            self.optimizer = optim.SGD(self.model.parameters(), lr=self.lr, momentum=self.momentum, weight_decay=self.weight_decay)
        else:
            raise ValueError(f"Optimizer {optimizer} not supported")
        
        if scheduler == "step_lr":
            self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, self.step_size, self.gamma)
        elif scheduler == "constant" or scheduler is None:
            self.scheduler = None
        else:
            raise ValueError(f"Scheduler {scheduler} not supported")
    
    @execution_time
    def train(self):
        
        if self.device == "cuda":
            cudnn.benchmark = True

        val_losses, val_accuracies = [], []
        train_losses, train_accuracies = [], []
        best_accuracy = -1
        best_num_epochs = None
        
        if self.norm_eval is None and self.aug_train is None:
            logging.warning("Neither augmentation nor normalization transforms found")
        elif self.aug_train == self.norm_eval:
            logging.info("No augmentation found, only normalization will be applied")
        
        for epoch in range(self.num_epochs):
            
            current_step = 0
            epoch_losses = []
            
            self.model.train()
            for (inputs, labels) in self.trainloader:
                
                if self.aug_train is not None:
                    inputs = torch.stack([self.aug_train(input_img) for input_img in inputs])

                inputs = inputs.type(self.data_type).to(self.device)
                labels = labels.to(self.device)
                
                # print(inputs, labels)

                # Forward pass
                self.optimizer.zero_grad()
                
                outputs = self.model(inputs)
                
                loss = self.criterion(outputs, labels)
                
                epoch_losses.append(loss.item())

                # Backward pass
                loss.backward()
                self.optimizer.step()

                if (current_step + 1) % self.train_log_frequency == 0:
                    logging.info(f"Training epoch {epoch + 1}, Iteration {current_step + 1}, "+
                                 f"Loss: {mean(epoch_losses[current_step + 1 - self.train_log_frequency : current_step + 1]):.5f}")

                current_step += 1

            if self.train_accuracy:
                train_loss, train_accuracy = self.training_eval()
            else:
                train_loss = mean(epoch_losses)
                train_accuracy = None
                
            val_loss, val_accuracy = self.validate()
            
            if val_accuracy > best_accuracy:
                best_accuracy = val_accuracy
                best_num_epochs = epoch + 1
                torch.save(self.model.state_dict(), self.model_path)

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
        losses, top_1_accuracies, _, _, _ = self.evaluate(self.trainloader)
        return losses, top_1_accuracies
    
    def validate(self) -> EvaluationResult:
        losses, top_1_accuracies, _, _, _ = self.evaluate(self.validloader)
        return losses, top_1_accuracies
    
    @execution_time
    def test(self):
        
        self.model.load_state_dict(torch.load(self.model_path, weights_only=True))
        
        # Remove model file to free memory
        os.remove(self.model_path)
        test_result = self.evaluate(self.testloader)
        
        self.test_results = test_result

    @torch.no_grad()
    def evaluate(self, dataloader: DataLoader) -> EvaluationResult:
        
        self.model.eval()

        if self.device == "cuda":
            cudnn.benchmark = True

        losses = []
        data_len = 0
        corrects = 0
        current_step = 0
        for inputs, labels in dataloader:

            data_len += inputs.size(0)
            
            if self.norm_eval is not None:
                inputs = torch.stack([self.norm_eval(input_img) for input_img in inputs])

            inputs = inputs.to(self.device)
            labels = labels.to(self.device)

            # Forward pass
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)

            losses.append(loss.item())
            
            if (current_step + 1) % self.val_log_frequency == 0:
                logging.info(f"Validation iteration {current_step + 1}, " +
                             f"Loss: {mean(losses[current_step + 1 - self.val_log_frequency : current_step + 1]):.5f}")

            # Calculate accuracy
            self.metrics.update(outputs, labels)
            predictions = torch.argmax(outputs, dim=1)
            corrects += torch.sum(predictions == labels).item()
            
            current_step += 1

        metrics = self.metrics.compute()
        self.metrics.reset()
        
        return EvaluationResult(mean(losses), metrics)
    
    def save_results(self, cfg: Config, save_path: str, training_time: float, test_time: float):
        id = time.strftime("%Y%m%d_%H%M%S")
        
        full_save_path = f"{save_path}/{id}"
        os.makedirs(full_save_path)
        
        self._save_files(cfg, full_save_path, training_time, test_time)
        self._save_plots("Loss", full_save_path)
        self._save_plots("Accuracy", full_save_path)
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
        plt.xlim(0, self.num_epochs - 0.8)
        
        if name == "Accuracy":
            plt.ylim(-0.01, max(values[0] + values[1]) + 0.1)
            
        f.savefig(f"{save_path}/{name.lower()}.png")
    
    def _save_files(self, cfg: Config, save_path: str, training_time: float, test_time: float):
        result = cfg.__dict__.copy()
        result["hog_params"] = cfg.hog_params.__dict__
        result["training_time"] = training_time
        result["test_time"] = test_time
        result.update(self.training_results.__dict__)
        result.update(self.test_results.__dict__)
        
        with open(f"{save_path}/result.json", "w") as f:
            json.dump(result, f, indent=4)
            
    def _save_confusion_matrix(self, save_path: str):
        confusion_matrix = self.test_results.metrics["confusion_matrix"]
        
        f = plt.figure("Confusion Matrix")
        plt.imshow(confusion_matrix, cmap="coolwarm", interpolation='nearest')
        plt.colorbar()
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.title("Confusion Matrix")
        
        plt.xticks(ticks=range(len(confusion_matrix)), labels=range(len(confusion_matrix)))
        plt.yticks(ticks=range(len(confusion_matrix)), labels=range(len(confusion_matrix)))
        
        f.savefig(f"{save_path}/confusion_matrix.png")