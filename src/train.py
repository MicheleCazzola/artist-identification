import torch.optim as optim
import torch.nn as nn
from torch.backends import cudnn
from src.evaluate import evaluate

def train(model, trainloader, validloader, criterion, optimizer, scheduler, num_epochs, device, log_frequency):
    model = model.to(device)
    model.train()

    val_losses, val_accuracies = [], []
    train_losses, train_accuracies = [], []
    if device == "cuda":
        cudnn.benchmark

    current_step = 0
    for epoch in range(num_epochs):
        for (inputs, labels) in trainloader:
            inputs = inputs.to(device)
            labels = labels.to(device)

            # Forward pass
            optimizer.zero_grad()
            
            outputs = model(inputs)
            
            loss = criterion(outputs, labels)

            # Backward pass
            loss.backward()
            optimizer.step()

            if current_step % log_frequency == 0:
                print(f"Epoch {epoch+1}, Iteration {current_step}, Loss: {loss.item()}")

            current_step += 1

        train_accuracy, train_loss = evaluate(model, trainloader, criterion, device)
        
        val_accuracy, val_loss = evaluate(model, validloader, criterion, device)

        print(f"End of Epoch {epoch+1}")
        print(f"Training_accuracy: {train_accuracy:.3f}, Training loss: {train_loss:.5f}")
        print(f"Validation_accuracy: {val_accuracy:.3f}, Validation loss: {val_loss:.5f}")

        val_losses.append(val_loss)
        val_accuracies.append(val_accuracy)
        train_losses.append(train_loss)
        train_accuracies.append(train_accuracy)

        scheduler.step()

    return train_losses, train_accuracies, val_losses, val_accuracies


def train_setup(model):
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    scheduler = optim.lr_scheduler.StepLR(optimizer, 5, 0.01)
    
    return criterion, optimizer, scheduler