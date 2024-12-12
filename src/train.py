import torch
import torch.optim as optim
import torch.nn as nn
from torch.backends import cudnn
from src.evaluate import evaluate
from src.network import MultibranchNetwork
from src.constants import Env
from torch.utils.data import DataLoader


def train_setup(model):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    scheduler = optim.lr_scheduler.StepLR(optimizer, 5, 0.01)
    
    return criterion, optimizer, scheduler

def train():
    pass


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
        self.model = model
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
        criterion: nn.Module,
        optimizer: optim.Optimizer,
        scheduler: optim.lr_scheduler.LRScheduler
    ):
        self.criterion = criterion()
        self.optimizer = optimizer(lr=self.lr, momentum=self.momentum, weight_decay=self.weight_decay)
        self.scheduler = scheduler(step=self.step_size, gamma=self.gamma)

    def train(self):
        self.model = self.model.to(self.device)
        self.model.train()

        val_losses, val_accuracies = [], []
        train_losses, train_accuracies = [], []
        if self.device == "cuda":
            cudnn.benchmark

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

            train_accuracy, train_loss = evaluate(self.model, self.trainloader, self.criterion, self.device)
            val_accuracy, val_loss = evaluate(self.model, self.validloader, self.criterion, self.device)

            print(f"End of Epoch {epoch+1}")
            print(f"Training_accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
            print(f"Validation_accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")

            val_losses.append(val_loss)
            val_accuracies.append(val_accuracy)
            train_losses.append(train_loss)
            train_accuracies.append(train_accuracy)

            self.scheduler.step()

        return train_losses, train_accuracies, val_losses, val_accuracies

    @torch.no_grad()
    def evaluate(self):
        self.model.eval()

        if self.device == "cuda":
            cudnn.benchmark

        losses = []
        dim = 0
        corrects = 0
        for inputs, labels in self.testloader:

            dim += inputs.size(0)

            inputs = inputs.to(self.device)
            labels = labels.to(self.device)

            # Forward pass
            outputs = self.model(inputs)
            loss = self.criterion(outputs, labels)

            losses.append(loss.item())

            # Calculate accuracy
            predictions = torch.argmax(outputs, dim=1)
            corrects += torch.sum(predictions == labels).item()

        accuracy = corrects / dim
        return accuracy, sum(losses) / len(losses)