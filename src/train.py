from dataclasses import dataclass
import json
import logging
import os
from statistics import mean
from matplotlib import pyplot as plt
import torch
import torch.optim as optim
import torch.nn as nn
from torch.backends import cudnn
from src.config import Config
from src.network import MultibranchNetwork
from torch.utils.data import DataLoader
from torchvision.transforms import Compose
from torchmetrics.classification import Accuracy, MulticlassAccuracy

class TrainingMetrics:
    def __init__(self, num_classes: int, top_k: int):
        
        if top_k > num_classes:
            logging.error(f"Top-k value {top_k} cannot be greater than number of classes {num_classes}")
        
        self.top_k = top_k
        self.top_1_accuracy: MulticlassAccuracy = Accuracy(task="multiclass", num_classes=num_classes)
        self.top_k_accuracy: MulticlassAccuracy = Accuracy(task="multiclass", num_classes=num_classes, top_k=top_k)
        self.mca: MulticlassAccuracy = Accuracy(task="multiclass", num_classes=num_classes, average=None)
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        self.top_1_accuracy(outputs, labels)
        self.top_k_accuracy(outputs, labels)
        self.mca(outputs, labels)
        
    def reset(self):
        self.top_1_accuracy.reset()
        self.top_k_accuracy.reset()
        self.mca.reset()
        
    def compute(self):
        top_1_accuracy = self.top_1_accuracy.compute().item()
        top_k_accuracy = self.top_k_accuracy.compute().item()
        mca_result = self.mca.compute().mean().item()
        return {
            "top-1_accuracy": top_1_accuracy,
            f"top-{self.top_k}_accuracy": top_k_accuracy,
            "mca": mca_result
        }
        
    def to(self, device: torch.device):
        return self.top_1_accuracy.to(device), self.top_k_accuracy.to(device), self.mca.to(device)


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
        aug_train: Compose,
        device: torch.device,
        log_frequency: int
    ):
        self.model = model.to(device)
        self.trainloader = trainloader
        self.validloader = validloader
        self.testloader = testloader
        self.aug_train = aug_train
        self.device = device
        self.log_frequency = log_frequency
        
        self.num_epochs = None
        self.lr = None
        self.momentum = None
        self.step_size = None
        self.gamma = None
        self.weight_decay = None
        
        self.criterion = None
        self.optimizer = None
        self.scheduler = None
        self.metrics = None
        
        self.best_num_epochs = None
        
        self.model_path = "best_model.pth"
        
        self.training_results = None
        self.test_results = None
        
    def set_params(
        self,
        num_epochs: int,
        lr: float,
        momentum: float,
        step_size: int,
        gamma: float,
        weight_decay: float,
        top_k: int
    ):
        self.num_epochs = num_epochs
        self.lr = lr
        self.momentum = momentum
        self.step_size = step_size
        self.gamma = gamma
        self.weight_decay = weight_decay
        self.metrics = TrainingMetrics(num_classes=self.model.out_classes, top_k=top_k).to(self.device)
        
    def build_trainer(
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
            self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)
        elif optimizer == "sgd":
            self.optimizer = optim.SGD(self.model.parameters(), lr=self.lr, momentum=self.momentum, weight_decay=self.weight_decay)
        else:
            raise ValueError(f"Optimizer {optimizer} not supported")
        
        if scheduler == "step_lr":
            self.scheduler = optim.lr_scheduler.StepLR(self.optimizer, self.step_size, self.gamma)
        elif scheduler == "constant":
            self.scheduler = None
        else:
            raise ValueError(f"Scheduler {scheduler} not supported")

    def train(self) -> TrainingResult:
        self.model.train()
        
        if self.device == "cuda":
            cudnn.benchmark

        val_losses, val_accuracies = [], []
        train_losses, train_accuracies = [], []
        best_accuracy = -1
        best_num_epochs = None
        current_step = 0
        
        if len(self.aug_train.transforms) == 1:
            logging.warning("No augmentation transforms found, only image normalization will be applied")
        
        for epoch in range(self.num_epochs):
            for (inputs, labels) in self.trainloader:
                
                aug_inputs = torch.stack([self.aug_train(input_img) for input_img in inputs])
                
                aug_inputs = aug_inputs.to(self.device)
                labels = labels.to(self.device)

                # Forward pass
                self.optimizer.zero_grad()
                
                outputs = self.model(aug_inputs)
                loss = self.criterion(outputs, labels)

                # Backward pass
                loss.backward()
                self.optimizer.step()

                if current_step % self.log_frequency == 0:
                    logging.info(f"Epoch {epoch+1}, Iteration {current_step}, Loss: {loss.item()}")

                current_step += 1

            train_loss, train_accuracy = self.training_eval()
            val_loss, val_accuracy = self.validate()
            
            if val_accuracy > best_accuracy:
                best_accuracy = val_accuracy
                best_num_epochs = epoch + 1
                torch.save(self.model.state_dict(), self.model_path)

            logging.info(f"End of Epoch {epoch+1}")
            logging.info(f"Training accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
            logging.info(f"Validation accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")

            val_losses.append(val_loss)
            val_accuracies.append(val_accuracy)
            train_losses.append(train_loss)
            train_accuracies.append(train_accuracy)

            # Scheduler is None if learning rate is constant
            if self.scheduler is not None:
                self.scheduler.step()

        self.best_num_epochs = best_num_epochs
        logging.info(f"Best validation accuracy: {best_accuracy:.3f} at epoch {best_num_epochs}")

        self.training_results = TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies, best_num_epochs)
    
    def training_eval(self) -> EvaluationResult:
        losses, top_1_accuracies, _, _ = self.evaluate(self.trainloader)
        return losses, top_1_accuracies
    
    def validate(self) -> EvaluationResult:
        losses, top_1_accuracies, _, _ = self.evaluate(self.validloader)
        return losses, top_1_accuracies
    
    def test(self) -> EvaluationResult:
        
        self.model.load_state_dict(torch.load(self.model_path, weights_only=True))
        
        # Remove model file to free memory
        os.remove(self.model_path)
        test_result = self.evaluate(self.testloader)
        
        self.test_results = test_result

    @torch.no_grad()
    def evaluate(self, dataloader: DataLoader) -> EvaluationResult:
        
        self.model.eval()

        if self.device == "cuda":
            cudnn.benchmark

        losses = []
        data_len = 0
        corrects = 0
        for inputs, labels in dataloader:

            data_len += inputs.size(0)

            inputs = inputs.to(self.device)
            labels = labels.to(self.device)

            # Forward pass
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)

            losses.append(loss.item())

            # Calculate accuracy
            self.metrics.update(outputs, labels)
            predictions = torch.argmax(outputs, dim=1)
            corrects += torch.sum(predictions == labels).item()

        metrics = self.metrics.compute()
        self.metrics.reset()
        
        return EvaluationResult(mean(losses), metrics)
    
    def plot_results(self, name: str, save_path: str):
        
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
        
        plt.xticks(ticks=range(len(values)+1), labels=range(1, len(values)+2))
        plt.xlabel("Epochs")
        plt.ylabel(name)
        plt.grid()
        plt.legend()
        plt.xlim(0, len(values)+0.2)
        
        if name == "Accuracy":
            plt.ylim(-0.1,1.1)
            
        f.savefig(f"{save_path}/{name.lower()}.png")
    
    def save_results(self, cfg: Config, save_path: str):
        result = cfg.__dict__.copy()
        result.update(self.training_results.__dict__)
        result.update(self.test_results.__dict__)
        
        with open(f"{save_path}/config.json", "w") as f:
            json.dump(result, f, indent=4)