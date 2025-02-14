import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import numpy as np

from skimage.feature import hog

from src.config.config import HOGConfig

class BottleneckBlock(nn.Module):
    """
    Residual block with bottleneck architecture, used in our network
    Designed similarly to the ResNet architecture
    
    Attributes:
    ----------
    in_channels: int
        Number of input channels
    out_channels: int
        Number of output channels
    stride: int
        Stride of the first convolutional layer
    dtype: torch.dtype
        Data type of the weights and biases
    
    Methods:
    --------
    forward(x: torch.Tensor) -> torch.Tensor
        Forward pass of the block
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1, dtype=torch.float32):
        super(BottleneckBlock, self).__init__()
        
        self.dtype = dtype
        bottleneck_channels = out_channels // 4
        
        # Downsample if needed and reduce number of channels
        self.conv1 = nn.Conv2d(in_channels, bottleneck_channels, kernel_size=1, stride=stride, bias=False, dtype=self.dtype)
        self.bn1 = nn.BatchNorm2d(bottleneck_channels, dtype=self.dtype)
        
        # No dimensionality modification
        self.conv2 = nn.Conv2d(bottleneck_channels, bottleneck_channels, kernel_size=3, stride=1, padding=1, bias=False, dtype=self.dtype)
        self.bn2 = nn.BatchNorm2d(bottleneck_channels, dtype=self.dtype)
        
        # Increase number of channels
        self.conv3 = nn.Conv2d(bottleneck_channels, out_channels, kernel_size=1, bias=False, dtype=self.dtype)
        
        # Skip connection: downsample if needed and modify number of channels
        if stride != 1 or in_channels != out_channels:
            self.skip = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False, dtype=self.dtype)
        else:
            self.skip = nn.Identity()
            
        # Last batch normalization: applied after the addition
        self.bn3 = nn.BatchNorm2d(out_channels, dtype=self.dtype)

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = F.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out) + self.skip(x))
        return F.relu(out)

class JoinModule(nn.Module):
    """
    Module to join the branches of the network
    
    Attributes:
    ----------
    join_block: BottleneckBlock
        Block to join the three branches and process them using convolutions
    """
    def __init__(self, input_channels: int):
        super(JoinModule, self).__init__()
        
        # The output of the branches is concatenated and then reduced in channel dimension by a factor of 3
        self.join_block = BottleneckBlock(input_channels, input_channels // 3)

    def forward(self, *branches: list[torch.Tensor]) -> torch.Tensor:
        x = torch.cat(branches, dim=1)
        x = self.join_block(x)
        return x

class HandCraftedFeatures(nn.Module):
    """
    Perform HOG feature extraction on the input images
    
    Attributes:
    ----------
    downsample_size: int
        Size to downsample the input images
    crop_size: int
        Size to center crop the downsampled images
    channel_coefficients: np.ndarray
        Coefficients to convert the RGB images to grayscale
    orientations: int
        Number of orientations for the HOG descriptor
    pixels_per_cell: int
        Number of pixels per cell for the HOG descriptor
    cells_per_block: int
        Number of cells per block for the HOG descriptor (used in normalization)
    transform_sqrt: bool
        Whether to apply power law compression to the HOG descriptor
    feature_vector: bool
        Whether to flatten the HOG descriptor
    normalization: str
        Type of normalization for the HOG descriptor
    """
    def __init__(self, hog_params: HOGConfig, dtype=torch.float32):
        super(HandCraftedFeatures, self).__init__()
        self.downsample_size: int = hog_params.downsample_size
        self.crop_size: int = hog_params.crop_size
        self.channel_coefficients: np.ndarray = np.array(hog_params.channel_coefficients)
        self.orientations: int = hog_params.orientations
        self.pixels_per_cell: int = hog_params.pixels_per_cell
        self.cells_per_block: int = hog_params.cells_per_block
        self.transform_sqrt: bool = hog_params.transform_sqrt
        self.feature_vector: bool = hog_params.feature_vector
        self.normalization: str = hog_params.normalization
        self.dtype: torch.dtype = dtype

    def forward(self, x):
        
        # Image preprocessing: downsample and center crop
        x = transforms.Compose([
            transforms.Resize((self.downsample_size, self.downsample_size)),
            transforms.CenterCrop((self.crop_size, self.crop_size))
        ])(x)
        
        
        x_np = x.cpu().numpy().transpose(0, 2, 3, 1)
        
        return torch.tensor(np.array([
            
            # Apply HOG feature extraction to each image in the batch
            # Works on grayscale images and only on CPU -> Slow
            hog(
                img @ self.channel_coefficients,
                orientations=self.orientations,
                pixels_per_cell=(self.pixels_per_cell, self.pixels_per_cell), 
                cells_per_block=(self.cells_per_block, self.cells_per_block),
                transform_sqrt=self.transform_sqrt,
                feature_vector=self.feature_vector,
                block_norm=self.normalization
            )
            for img in x_np
        ]), dtype=self.dtype, device=x.device)