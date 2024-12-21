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

from src.transformations import Transforms


def timeit(x, func, iter=10):
	torch.cuda.synchronize()
	start = time.time()
	for _ in range(iter):
		y = func(x)
	torch.cuda.synchronize()
	runtime = (time.time()-start)/iter
	return runtime

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
        self.register_buffer("weight", mat[:,None,:,:])
        self.pooler = nn.AvgPool2d(self.pool, stride=self.pool, padding=0, ceil_mode=False, count_include_pad=True)

    def forward(self, x):
        with torch.no_grad():
            gxy = F.conv2d(x, self.weight, None, self.stride,
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


class HOGLayerMoreComplicated(nn.Module):
    def __init__(self, nbins=10, pool=8, max_angle=math.pi, stride=1, padding=1, dilation=1,
                 mean_in=False, max_out=False):
        super(HOGLayerMoreComplicated, self).__init__()
        self.nbins = nbins
        self.stride = stride
        self.padding = padding
        self.dilation = dilation
        self.pool = pool
        self.max_angle = max_angle
        self.max_out = max_out
        self.mean_in = mean_in

        mat = torch.FloatTensor([[1, 0, -1],
                                 [2, 0, -2],
                                 [1, 0, -1]])
        mat = torch.cat((mat[None], mat.t()[None]), dim=0)
        self.register_buffer("weight", mat[:,None,:,:])
        self.pooler = nn.AvgPool2d(pool, stride=pool, padding=0, ceil_mode=False, count_include_pad=True)

    def forward(self, x):
        if self.mean_in:
            return self.forward_v1(x)
        else:
            return self.forward_v2(x)

    def forward_v1(self, x):
        if x.size(1) > 1:
            x = x.mean(dim=1)[:,None,:,:]

        gxy = F.conv2d(x, self.weight, None, self.stride,
                       self.padding, self.dilation, 1)
        # 2. Mag/ Phase
        mag = gxy.norm(dim=1)
        norm = mag[:, None, :, :]
        phase = torch.atan2(gxy[:, 0, :, :], gxy[:, 1, :, :])

        # 3. Binning Mag with linear interpolation
        phase_int = phase / self.max_angle * self.nbins
        phase_int = phase_int[:, None, :, :]

        n, c, h, w = gxy.shape
        out = torch.zeros((n, self.nbins, h, w), dtype=torch.float, device=gxy.device)
        out.scatter_(1, phase_int.floor().long() % self.nbins, norm)
        out.scatter_add_(1, phase_int.ceil().long() % self.nbins, 1 - norm)

        return self.pooler(out)

    def forward_v2(self, x):
        batch_size, in_channels, height, width = x.shape
        weight = self.weight.repeat(3, 1, 1, 1)
        gxy = F.conv2d(x, weight, None, self.stride,
                        self.padding, self.dilation, groups=in_channels)

        gxy = gxy.view(batch_size, in_channels, 2, height, width)

        if self.max_out:
            gxy = gxy.max(dim=1)[0][:,None,:,:,:]

        #2. Mag/ Phase
        mags = gxy.norm(dim=2)
        norms = mags[:,:,None,:,:]
        phases = torch.atan2(gxy[:,:,0,:,:], gxy[:,:,1,:,:])

        #3. Binning Mag with linear interpolation
        phases_int = phases / self.max_angle * self.nbins
        phases_int = phases_int[:,:,None,:,:]

        out = torch.zeros((batch_size, in_channels, self.nbins, height, width),
                          dtype=torch.float, device=gxy.device)
        out.scatter_(2, phases_int.floor().long()%self.nbins, norms)
        out.scatter_add_(2, phases_int.ceil().long()%self.nbins, 1 - norms)

        out = out.view(batch_size, in_channels * self.nbins, height, width)
        out = torch.cat((self.pooler(out), self.pooler(x)), dim=1)

        return out
    
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
    
transformations = Transforms(config=cfg)
trainset, validset, testset = create_datasets(
    cfg.default_root, 
    train_split_size=cfg.train_split_size, 
    transforms=transformations.get(),
    reduction_factor=cfg.reduce_factor
)

trainloader, validloader, testloader = create_dataloaders(
    [trainset, validset, testset],
    cfg.batch_size,
    num_workers=cfg.num_workers   
)

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
    
    
def train(model, trainloader, validloader, transform, criterion, optimizer, num_epochs, device, scheduler = None, log_frequency = 2):
    
    model = model.to(device)
    
    model.train()
    
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True
    
    best_epochs = 0
    train_losses, train_accuracies = [], []
    val_losses, val_accuracies = [], []
    for epoch in range(num_epochs):
        
        current_step = 0
        for inputs, labels in trainloader:
            
            inputs = inputs.to(device)
            labels = labels.to(device)
            
            optimizer.zero_grad()
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            loss.backward()
            optimizer.step()
            
            if (current_step+1) % log_frequency == 0:
                print(f"Epoch {epoch+1}/{num_epochs}, Iteration: {current_step+1} Loss: {loss.item()}")
            
        current_step += 1
        
        train_loss, train_accuracy = evaluate(model, trainloader, transform, criterion, device)
        val_loss, val_accuracy = evaluate(model, validloader, transform, criterion, device)
        
        if scheduler is not None:
            scheduler.step()
            
        train_losses.append(train_loss)
        train_accuracies.append(train_accuracy)
        val_losses.append(val_loss)
        val_accuracies.append(val_accuracy)
        
        if val_accuracy >= max(val_accuracies):
            best_epochs = epoch+1
            
            torch.save(model.state_dict(), f"best_model.pth")
            
        return {
            "trn_loss": train_losses,
            "trn_acc": train_accuracies,
            "val_loss": val_losses,
            "val_acc": val_accuracies,
            "best": best_epochs
        }

@torch.no_grad()
def evaluate(model, dataloader, transform, criterion, device, log_frequency = 1):
    model = model.to(device)
    
    model.eval()
    
    if torch.cuda.is_available():
        torch.backends.cudnn.benchmark = True

    current_step = 0
    losses = []
    accuracy = Accuracy("multiclass", num_classes=161)
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
        
gray_custom = torchvision.transforms.Lambda(
    lambda img: torch.unsqueeze(
        0.299 * img[:, 0, :, :] + 0.587 * img[:, 1, :, :] + 0.114 * img[:, 2, :, :], 1
    )
)

INPUT_SIZE = cfg.crop_dim
OUT_CLASSES = 161
NUM_EPOCHS = cfg.num_epochs

model = HOGClassifier("gpu", gray_custom, 1536, 161, nbins=6, pool=8, stride=4)
model_official = HOGClassifier("sklearn", gray_custom, 1176, 161, orientations=6, pixels_per_cell=(64,64), cells_per_block=(2,2))

if train_model == "gpu":
    
    model = HOGClassifier("gpu", gray_custom, 1536, 161, nbins=6, pool=8, stride=4)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
    
    start = time.time()
    result = train(model, trainloader, validloader, gray_custom, criterion, optimizer, NUM_EPOCHS, cfg.device)
    train_time = time.time() - start
    
    model.load_state_dict(torch.load("best_model.pth", weights_only=True))
    
    start = time.time()
    test_loss, test_acc = evaluate(model, testloader, gray_custom, criterion, cfg.device)
    test_time = time.time() - start 
    
    print(f"GPU Average test loss: {test_loss}, Test accuracy: {test_acc}")
    print(f"GPU Training time: {train_time}, Test time: {test_time}")
elif train_model == "sklearn":
    
    model_official = HOGClassifier("sklearn", gray_custom, 1176, 161, orientations=6, pixels_per_cell=(64,64), cells_per_block=(2,2))
    criterion_official = nn.CrossEntropyLoss()
    optimizer_official = torch.optim.Adam(model_official.parameters(), lr = 0.001)
    
    start = time.time()
    result_official = train(model_official, trainloader, validloader, gray_custom, criterion_official, optimizer_official, NUM_EPOCHS, cfg.device)
    train_time = time.time() - start
    
    model_official.load_state_dict(torch.load("best_model.pth", weights_only=True))
    
    start = time.time()
    test_loss, test_acc = evaluate(model_official, testloader, gray_custom, criterion_official, cfg.device) 
    test_time = time.time() - start
    
    print(f"Sklearn Average test loss: {test_loss}, Test accuracy: {test_acc}")
    print(f"Sklearn Training time: {train_time}, Test time: {test_time}")
else:
    model = HOGClassifier("gpu", gray_custom, 1536, 161, nbins=6, pool=8, stride=4)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr = 0.001)
    
    start = time.time()
    result = train(model, trainloader, validloader, gray_custom, criterion, optimizer, NUM_EPOCHS, cfg.device)
    train_time = time.time() - start
    
    model.load_state_dict(torch.load("best_model.pth", weights_only=True))
    
    start = time.time()
    test_loss, test_acc = evaluate(model, testloader, gray_custom, criterion, cfg.device) 
    test_time = time.time() - start
    
    print(f"GPU Average test loss: {test_loss}, Test accuracy: {test_acc}")
    print(f"GPU Training time: {train_time}, Test time: {test_time}")
    
    model_official = HOGClassifier("sklearn", gray_custom, 1176, 161, orientations=6, pixels_per_cell=(64,64), cells_per_block=(2,2))
    criterion_official = nn.CrossEntropyLoss()
    optimizer_official = torch.optim.Adam(model_official.parameters(), lr = 0.001)
    
    start = time.time()
    result_official = train(model_official, trainloader, validloader, gray_custom, criterion_official, optimizer_official, NUM_EPOCHS, cfg.device)
    train_time = time.time() - start
    
    model_official.load_state_dict(torch.load("best_model.pth", weights_only=True))
    
    start = time.time()
    test_loss, test_acc = evaluate(model_official, testloader, gray_custom, criterion_official, cfg.device) 
    test_time = time.time() - start
    
    print(f"Sklearn Average test loss: {test_loss}, Test accuracy: {test_acc}")
    print(f"Sklearn Training time: {train_time}, Test time: {test_time}")