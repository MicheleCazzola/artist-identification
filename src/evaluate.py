import torch
from torch.backends import cudnn

from statistics import mean

@torch.no_grad()
def evaluate(model, testloader, criterion, device):
    model.eval()

    if device == "cuda":
        cudnn.benchmark

    losses = []
    dim = 0
    corrects = 0
    for inputs, labels in testloader:

        dim += inputs.size(0)

        inputs = inputs.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, labels)

        losses.append(loss.item())

        # Calculate accuracy
        predictions = torch.argmax(outputs, dim=1)
        corrects += torch.sum(predictions == labels).item()

    accuracy = corrects / dim
    return accuracy, mean(losses)