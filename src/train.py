from dataclasses import dataclass
import os
from statistics import mean
import torch
import torch.optim as optim
import torch.nn as nn
from torch.backends import cudnn
from src.evaluate import evaluate
from src.network import MultibranchNetwork
from src.constants import Env
from torch.utils.data import DataLoader

@dataclass
class TrainingResult:
    train_losses: list
    train_accuracies: list
    val_losses: list
    val_accuracies: list
    
    def __iter__(self):
        return iter((self.train_losses, self.train_accuracies, self.val_losses, self.val_accuracies))
    
    
@dataclass
class EvaluationResult:
    eval_loss: float
    eval_accuracy: float

    def __iter__(self):
        return iter((self.eval_loss, self.eval_accuracy))

class Trainer: 
    def __init__(
        self,
        model: MultibranchNetwork, 
        trainloader: DataLoader,
        validloader: DataLoader,
        testloader: DataLoader,
        device: torch.device,
        log_frequency: int
    ):
        self.model = model.to(device)
        self.trainloader = trainloader
        self.validloader = validloader
        self.testloader = testloader
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
        
        self.best_num_epochs = self.num_epochs
        
        self.model_path = "best_model.pth"
        
    def set_params(
        self,
        num_epochs: int,
        lr: float,
        momentum: float,
        step_size: int,
        gamma: float,
        weight_decay: float
    ):
        self.num_epochs = num_epochs
        self.lr = lr
        self.momentum = momentum
        self.step_size = step_size
        self.gamma = gamma
        self.weight_decay = weight_decay
        
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
        
        for epoch in range(self.num_epochs):
            for (inputs, labels) in self.trainloader:
                inputs = inputs.to(self.device)
                labels = labels.to(self.device)

                # Forward pass
                self.optimizer.zero_grad()
                
                outputs = self.model(inputs)
                loss = self.criterion(outputs, labels)

                # Backward pass
                loss.backward()
                self.optimizer.step()

                if current_step % self.log_frequency == 0:
                    print(f"Epoch {epoch+1}, Iteration {current_step}, Loss: {loss.item()}")

                current_step += 1

            train_loss, train_accuracy = self.training_eval()
            val_loss, val_accuracy = self.validate()
            
            if val_accuracy > best_accuracy:
                best_accuracy = val_accuracy
                best_num_epochs = epoch + 1
                torch.save(self.model.state_dict(), self.model_path)

            print(f"End of Epoch {epoch+1}")
            print(f"Training accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
            print(f"Validation accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")

            val_losses.append(val_loss)
            val_accuracies.append(val_accuracy)
            train_losses.append(train_loss)
            train_accuracies.append(train_accuracy)

            # Scheduler is None if learning rate is constant
            if self.scheduler is not None:
                self.scheduler.step()

        self.best_num_epochs = best_num_epochs
        print(f"Best validation accuracy: {best_accuracy:.3f} at epoch {best_num_epochs}")

        return TrainingResult(train_losses, train_accuracies, val_losses, val_accuracies)
    
    def training_eval(self) -> EvaluationResult:
        train_result = self.evaluate(self.trainloader)
        return train_result
    
    def validate(self) -> EvaluationResult:
        valid_result = self.evaluate(self.validloader)
        return valid_result
    
    def test(self) -> EvaluationResult:
        
        self.model.load_state_dict(torch.load(self.model_path, weights_only=True))
        
        # Remove model file to free memory
        os.remove(self.model_path)
        test_result = self.evaluate(self.testloader)
        
        return test_result

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
            predictions = torch.argmax(outputs, dim=1)
            corrects += torch.sum(predictions == labels).item()

        accuracy = corrects / data_len
        
        assert sum(losses) / len(losses) == mean(losses)
        
        return EvaluationResult(sum(losses) / len(losses), accuracy)