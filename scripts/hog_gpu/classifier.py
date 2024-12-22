import os
from statistics import mean
import sys
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math
import time

import torchvision
from src.config import Config
from src.dataloader import create_dataloaders
from src.dataset import create_datasets
from skimage.feature import hog
from torchmetrics import Accuracy
import matplotlib.pyplot as plt

from src.transformations import Transforms


class HOGLayer(nn.Module):
    def __init__(self, **kwargs):
        super(HOGLayer, self).__init__()
        self.nbins = kwargs.get("nbins", 10)
        self.pool = kwargs.get("pool", 8)
        self.max_angle = kwargs.get("max_angle", math.pi)
        self.stride = kwargs.get("stride", 1)
        self.padding = kwargs.get("padding", 1)
        self.dilation = kwargs.get("dilation", 1)
        mat = torch.FloatTensor([[1, 0, -1],
                                 [2, 0, -2],
                                 [1, 0, -1]])
        mat = torch.cat((mat[None], mat.t()[None]), dim=0)
        self.weight = mat[:,None,:,:]
        #self.register_buffer("weight", mat[:,None,:,:], persistent=True)
        self.pooler = nn.AvgPool2d(self.pool, stride=self.pool, padding=0, ceil_mode=False, count_include_pad=True)

    def forward(self, x):
        with torch.no_grad():
            gxy = F.conv2d(x, self.weight.to(x.device), None, self.stride,
                            self.padding, self.dilation, 1)

            #2. Mag/ Phase
            mag = gxy.norm(dim=1)
            norm = mag[:,None,:,:]
            phase = torch.atan2(gxy[:,0,:,:], gxy[:,1,:,:])

            #3. Binning Mag with linear interpolation
            phase_int = phase / self.max_angle * self.nbins
            phase_int = phase_int[:,None,:,:]

            n, c, h, w = gxy.shape
            out = torch.zeros((n, self.nbins, h, w), dtype=torch.float, device=gxy.device)

            out.scatter_(1, phase_int.floor().long()%self.nbins, norm)
            out.scatter_add_(1, phase_int.ceil().long()%self.nbins, 1 - norm)

            return self.pooler(out)
  

class SkimageHOG(nn.Module):
    def __init__(
        self,
        **kwargs
    ):
        super(SkimageHOG, self).__init__()
        self.orientations = kwargs.get("orientations")
        self.pixels_per_cell = kwargs.get("pixels_per_cell")
        self.cells_per_block = kwargs.get("cells_per_block")
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return torch.tensor(np.array([
            hog(
                x_np,
                orientations=self.orientations,
                pixels_per_cell=self.pixels_per_cell,
                cells_per_block=self.cells_per_block
            )
            for x_np in x.cpu().numpy()[:,0,:,:]
        ]), device = x.device, dtype=torch.float32)


class HogFeatureExtractor(nn.Module):
    def __init__(self, type: str, transform: torchvision.transforms, **kwargs):
        super(HogFeatureExtractor, self).__init__()
        self.transform = transform
        self.hog = HOGLayer(**kwargs) if type == "gpu" else SkimageHOG(**kwargs)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.transform(x)
        return self.hog(x)


class LinearClassifier(nn.Module):
    def __init__(self, in_features, out_classes):
        super(LinearClassifier, self).__init__()
        
        self.fc1 = nn.Linear(in_features, in_features // 2)
        self.fc2 = nn.Linear(in_features // 2, in_features // 4)
        self.fc3 = nn.Linear(in_features // 4, out_classes)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        
        x = torch.flatten(x, 1)
        
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        
        return x
    
    
class HOGClassifier(nn.Module):
    def __init__(
        self,
        extractor_type: str,
        input_transform: torchvision.transforms,
        num_features: int,
        out_classes: int,
        **extraction_kwargs
    ):
        super(HOGClassifier, self).__init__()
        self.extractor = HogFeatureExtractor(extractor_type, input_transform, **extraction_kwargs)
        self.classifier = LinearClassifier(num_features, out_classes)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.extractor(x)
        x = self.classifier(x)
        return x    
    
    
def train(model: HOGClassifier, trainloader, validloader, criterion, optimizer, num_epochs, device, scheduler = None, log_frequency = 2):
    
    model = model.to(device)
    
    model.train()
    
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True
    
    best_epochs = 0
    train_losses, train_accuracies = [], []
    val_losses, val_accuracies = [], []
    for epoch in range(num_epochs):
        
        current_step = 0
        epoch_losses = []
        for inputs, labels in trainloader:
            
            inputs = inputs.to(device)
            labels = labels.to(device)
            
            optimizer.zero_grad()
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            epoch_losses.append(loss.item())
            
            loss.backward()
            optimizer.step()
            
            if (current_step+1) % log_frequency == 0:
                print(f"Epoch {epoch+1}/{num_epochs}, Iteration: {current_step+1} Loss: {loss.item()}")
            
            current_step += 1
        
        train_loss = mean(epoch_losses)
        val_loss, val_accuracy = evaluate(model, validloader, criterion, device, log_frequency=max(log_frequency // 3, 1))
        
        print(f"End of epoch {epoch+1}/{num_epochs}, Train loss: {train_loss}, Validation loss: {val_loss}, Validation accuracy: {val_accuracy}")
        
        if scheduler is not None:
            scheduler.step()
            
        train_losses.append(train_loss)
        val_losses.append(val_loss)
        val_accuracies.append(val_accuracy)
        
        if val_accuracy >= max(val_accuracies):
            best_epochs = epoch+1
            torch.save(model.state_dict(), f"best_model.pth")
            
    return {
        "trn_loss": train_losses,
        "val_loss": val_losses,
        "val_acc": val_accuracies,
        "best": best_epochs
    }

@torch.no_grad()
def evaluate(model, dataloader, criterion, device, log_frequency = 1):
    model = model.to(device)
    
    model.eval()
    
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True

    current_step = 0
    losses = []
    accuracy = Accuracy("multiclass", num_classes=cfg.num_classes).to(device)
    for inputs, labels in dataloader:
        inputs = inputs.to(device)
        labels = labels.to(device)
        
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        
        accuracy.update(outputs, labels)
        losses.append(loss.item())
        
        if (current_step+1) % log_frequency == 0:
            print(f"Eval. iteration: {current_step+1} Loss: {loss.item()}")
            
        current_step += 1
        
    return mean(losses), accuracy.compute().item()


if len(sys.argv) > 1:
    cfg = Config.create("colab")
    root = sys.argv[1]
else:
    cfg = Config.create("local")
    root = cfg.default_root
    
if len(sys.argv) > 2:
    train_model = sys.argv[2]
else:
    train_model = None

print(f"Info aquired - Root: '{root}', Train model: '{train_model}'")
    
transformations = Transforms(config=cfg)
trainset, validset, testset = create_datasets(
    cfg.default_root, 
    train_split_size=cfg.train_split_size, 
    transforms=transformations.get(),
    reduction_factor=cfg.reduce_factor
)

print(f"Datasets created, with sizes {len(trainset)}, {len(validset)}, {len(testset)}")

trainloader, validloader, testloader = create_dataloaders(
    [trainset, validset, testset],
    cfg.batch_size,
    num_workers=cfg.num_workers   
)

print(f"Dataloders created, with sizes {len(trainloader)}, {len(validloader)}, {len(testloader)}")
        
gray_custom = torchvision.transforms.Lambda(
    lambda img: torch.unsqueeze(
        0.299 * img[:, 0, :, :] + 0.587 * img[:, 1, :, :] + 0.114 * img[:, 2, :, :], 1
    )
)

GPU_HOG_FEATURES = 1536
SKLEARN_HOG_FEATURES = 1176
OUT_CLASSES = cfg.num_classes
NUM_EPOCHS = cfg.num_epochs

def train_hog_gpu():
    model = HOGClassifier("gpu", gray_custom, GPU_HOG_FEATURES, OUT_CLASSES, nbins=6, pool=8, stride=4)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
    
    start = time.time()
    result = train(model, trainloader, validloader, criterion, optimizer, NUM_EPOCHS, cfg.device, log_frequency = cfg.train_log_frequency)
    train_time = time.time() - start
    
    model.load_state_dict(torch.load("best_model.pth", weights_only=True))
    
    start = time.time()
    test_loss, test_acc = evaluate(model, testloader, criterion, cfg.device, log_frequency=cfg.val_log_frequency)
    test_time = time.time() - start 
    
    print(f"GPU Average test loss: {test_loss:.5f}, Test accuracy: {test_acc:.3f}")
    print(f"GPU Training time (per epoch): {train_time / NUM_EPOCHS:.5f} s, Test time: {test_time:.3f} s")
    
    plot_results(result, "GPU")
    
def train_hog_sklearn():
    model_official = HOGClassifier("sklearn", gray_custom, SKLEARN_HOG_FEATURES, OUT_CLASSES, orientations=6, pixels_per_cell=(64,64), cells_per_block=(2,2))
    criterion_official = nn.CrossEntropyLoss()
    optimizer_official = torch.optim.Adam(model_official.parameters(), lr = 0.001)
    
    start = time.time()
    result_official = train(model_official, trainloader, validloader, criterion_official, optimizer_official, NUM_EPOCHS, cfg.device, log_frequency=cfg.train_log_frequency)
    train_time = time.time() - start
    
    model_official.load_state_dict(torch.load("best_model.pth", weights_only=True))
    
    start = time.time()
    test_loss, test_acc = evaluate(model_official, testloader, criterion_official, cfg.device, log_frequency=cfg.val_log_frequency) 
    test_time = time.time() - start
    
    print(f"Sklearn Average test loss: {test_loss:.5f}, Test accuracy: {test_acc:.3f}")
    print(f"Sklearn Training time: {train_time / NUM_EPOCHS:.5f} s, Test time: {test_time:.3f} s")
    
    plot_results(result_official, "Sklearn")
    
    
def plot_results(result: dict, mode: str):
    fig, axs = plt.subplots(2, 1, figsize=(10, 10))
    
    fig.suptitle(f"HOG Classifier - {mode}")
    
    axs[0].plot(result["trn_loss"], label="Train loss")
    axs[0].plot(result["val_loss"], label="Validation loss")
    axs[0].set_title("Losses")
    axs[0].legend()
    
    axs[1].plot(result["val_acc"], label="Validation accuracy")
    axs[1].set_title("Validation accuracy")
    axs[1].legend()
    
    
if train_model == "gpu":
    
    print(f"GPU model")
    train_hog_gpu()
elif train_model == "sklearn":
    print(f"Sklearn model")
    train_hog_sklearn()
else:
    
    print(f"Both models")
    
    print("GPU model")
    train_hog_gpu()
    
    print("Sklearn model")
    train_hog_sklearn()
    
plt.show()