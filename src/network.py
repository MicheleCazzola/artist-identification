import sys
import time
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torchvision.models import resnet18, mobilenet_v3_small, efficientnet_b0, regnet_x_400mf, efficientnet_v2_s
from skimage.feature import hog
from enum import Enum
from torchvision.models import shufflenet_v2_x0_5
from torchvision.models import mnasnet0_5

class BackboneType(Enum):
    RESNET18 = "resnet18"
    MOBILENET_V3_SMALL = "mobilenet_v3_small"
    EFFICIENTNET_B0 = "efficientnet_b0"
    REGNET_X_400MF = "regnet_x_400mf"
    SHUFFLENET_V2_X0_5 = "shufflenet_v2_x0_5"
    MNASNET0_5 = "mnasnet0_5"

class BottleneckBlock(nn.Module):
    """
    Classical bottleneck block
    """
    def __init__(self, in_channels: int, out_channels: int, stride: int = 1):
        super(BottleneckBlock, self).__init__()
        bottleneck_channels = out_channels // 4
        
        # Convolutions and batch normalization
        # No bias since batch norm is used
        
        # Reduce dimensionality and downsampling, according to original implementation
        self.conv1 = nn.Conv2d(in_channels, bottleneck_channels, kernel_size=1, stride=stride, bias=False)
        self.bn1 = nn.BatchNorm2d(bottleneck_channels)
        
        # No dimensionality change, no downsampling
        self.conv2 = nn.Conv2d(bottleneck_channels, bottleneck_channels, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(bottleneck_channels)
        
        # Dimensionality increase
        self.conv3 = nn.Conv2d(bottleneck_channels, out_channels, kernel_size=1, bias=False)
        
        # Skip connection with convolution if input and output dimensions are different
        if stride != 1 or in_channels != out_channels:
            self.skip = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False)
        else:
            self.skip = nn.Identity()
        
        # Applied after the residual addition
        self.bn3 = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = F.relu(self.bn2(self.conv2(out)))
        
        # Batch normalization applied after the residual addition
        out = self.bn3(self.conv3(out) + self.skip(x))
        
        return F.relu(out)
    
class CroppingModule(nn.Module):
    def __init__(self, crop_size: int, downsample_size: int = None):
        super(CroppingModule, self).__init__()
        self.crop_size = crop_size
        self.downsample_size = downsample_size
        
    def forward(self, x):
        if self.downsample_size is not None:
            x = transforms.Resize((self.downsample_size, self.downsample_size))(x)
        return transforms.RandomCrop((self.crop_size, self.crop_size), pad_if_needed=True)(x)
    
class SpatialTransformerNetwork(nn.Module):
    def __init__(self, crop_size: int, backbone_type: BackboneType):
        super(SpatialTransformerNetwork, self).__init__()
        self.crop_size = crop_size
        self.backbone_type = backbone_type
        self.loc_net = self._make_loc_net()
        self.sampling_grid = lambda t: F.affine_grid(t.view(-1, 2, 3), size=(t.size(0), 3, self.crop_size, self.crop_size), align_corners=False)
        self.sampler = lambda x,g: F.grid_sample(x, g, align_corners=False)
        
    def _make_loc_net(self):
        # Using ResNet-18 as the localization network
        if self.backbone_type == self.backbone_type.RESNET18:
            model = resnet18(weights="IMAGENET1K_V1")
            last_in_features = model.fc.in_features     # 1024
            model.fc = nn.Linear(last_in_features, 6)
        # Using MobileNetV3-Small as the localization network
        elif self.backbone_type == self.backbone_type.MOBILENET_V3_SMALL:
            model = mobilenet_v3_small(weights="IMAGENET1K_V1")
            last_in_features = model.classifier[3].in_features      # 512
            model.classifier[3] = nn.Linear(last_in_features, 6)
        elif self.backbone_type == self.backbone_type.EFFICIENTNET_B0:
            model = efficientnet_b0(weights="IMAGENET1K_V1")
            last_in_features = model.classifier[1].in_features
            model.classifier[1] = nn.Linear(last_in_features, 6)
        elif self.backbone_type == self.backbone_type.REGNET_X_400MF:
            model = regnet_x_400mf(weights="IMAGENET1K_V1")
            last_in_features = model.fc.in_features
            model.fc = nn.Linear(last_in_features, 6)   
        elif self.backbone_type == self.backbone_type.SHUFFLENET_V2_X0_5:
            model = shufflenet_v2_x0_5(weights="IMAGENET1K_V1")
            last_in_features = model.fc.in_features
            model.fc = nn.Linear(last_in_features, 6)
        elif self.backbone_type == self.backbone_type.MNASNET0_5:
            model = mnasnet0_5(weights="IMAGENET1K_V1")
            last_in_features = model.classifier[1].in_features
            model.classifier[1] = nn.Linear(last_in_features, 6)
        else:
            raise ValueError(f"Unknown backbone type: {self.backbone_type}")
        
        return model
    
    def forward(self, x):
        theta = self.loc_net(x)
        grid = self.sampling_grid(theta)
        return self.sampler(x, grid)
    
class ROIsProposal(nn.Module):
    def __init__(self, crop_size: int, downsample_size: int, stn: BackboneType = None):
        super(ROIsProposal, self).__init__()
        self.stn = stn
        self.crop_size = crop_size
        self.downsample_size = downsample_size
        
        self.downsample_cropper = CroppingModule(crop_size, downsample_size)
        
        if stn is not None:
            self.extractor1 = SpatialTransformerNetwork(crop_size, stn)
            self.extractor2 = SpatialTransformerNetwork(crop_size, stn)
        else:
            self.extractor1 = CroppingModule(crop_size)
            self.extractor2 = CroppingModule(crop_size)
    
    def forward(self, x):
        downsampled_crop = self.downsample_cropper(x)
        
        roi1 = self.extractor1(x)
        roi2 = self.extractor2(x)
        
        return roi1, roi2, downsampled_crop

class JoinModule(nn.Module):
    def __init__(self, input_channels: int):
        super(JoinModule, self).__init__()
        self.join_block = BottleneckBlock(input_channels, input_channels // 3)

    def forward(self, *branches: list[torch.Tensor]) -> torch.Tensor:
        x = torch.cat(branches, dim=1)
        x = self.join_block(x)
        return x
    
class HandCraftedFeatures(nn.Module):
    def __init__(self, downsample_size: int, crop_size: int):
        super(HandCraftedFeatures, self).__init__()
        
        self.downsample_size = downsample_size
        self.crop_size = crop_size

    def forward(self, x):
        
        x = transforms.Compose([
            transforms.Resize((self.downsample_size, self.downsample_size)),
            transforms.RandomCrop((self.crop_size, self.crop_size), pad_if_needed=True)
        ])(x)
        
        # Convert tensor to numpy for feature extraction
        x_np = x.cpu().numpy().transpose(0, 2, 3, 1)  # N, H, W, C
        gray = lambda img: 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
        return torch.tensor(np.array([
            hog(gray(img), orientations=6, pixels_per_cell=(16, 16), 
                cells_per_block=(2, 2), block_norm='L2-Hys')
            for img in x_np
        ]), dtype=torch.float32, device=x.device)

class MultiBranchArtistNetwork(nn.Module):
    def __init__(self, num_classes: int, stn: BackboneType = None, use_handcrafted: bool = True):
        super(MultiBranchArtistNetwork, self).__init__()
        
        self.roi_extractor = ROIsProposal(256, 224, stn=stn)
        
        self.branch1 = self._make_branch(3, 256)
        self.branch2 = self._make_branch(3, 256)
        self.branch3 = self._make_branch(3, 256)
        
        self.join = JoinModule(256 * 3)
        
        self.resblock1 = self._make_residual_block(256, 512, 3, 2)
        self.resblock2 = self._make_residual_block(512, 1024, 6, 2)
        self.resblock3 = self._make_residual_block(1024, 2048, 4, 2)
        
        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))
        
        if use_handcrafted:
            self.handcrafted = HandCraftedFeatures(256, 224)
            self.classifier = nn.Linear(2048 + 4056, num_classes)
        else:
            self.handcrafted = None
            self.classifier = nn.Linear(2048, num_classes)
        
    def _make_branch(self, in_channels: int, out_channels: int) -> nn.Sequential:
        initial = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=7, stride=1, padding=3, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        resblocks = self._make_residual_block(64, out_channels, num_blocks=3, stride=2)
        
        return nn.Sequential(initial, resblocks)
        
    def _make_residual_block(self, in_channels: int, out_channels: int, num_blocks: int, stride: int) -> nn.Sequential:
        layers = [BottleneckBlock(in_channels, out_channels, stride=stride)]
        layers.extend([BottleneckBlock(out_channels, out_channels) for _ in range(num_blocks - 1)])
        
        return nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x1, x2, x3 = self.roi_extractor(x)
        
        b1 = self.branch1(x1)
        b2 = self.branch2(x2)
        b3 = self.branch3(x3)
        
        joined = self.join(b1, b2, b3)
        
        out = self.resblock1(joined)
        out = self.resblock2(out)
        out = self.resblock3(out)
        
        out = self.avg_pool(out)
        
        out = torch.flatten(out, 1)
        
        if self.handcrafted is not None:
            hand_crafted = self.handcrafted(x)
            out = torch.cat((out, hand_crafted), dim=1)
        
        out = self.classifier(out)
        
        return out

# Example usage:
# model = MultiBranchArtistNetwork(num_classes=161, stn=BackboneType.RESNET18)

# modules = [(name, sum(p.numel() for p in module.parameters())) for name, module in model.named_children()]

# for name, size in modules:
#     print(f"{name}: {size * 4 / 1024**2:.2f} MB")

# tot_params = sum(p.numel() for p in model.parameters())
# print(f"Total size: {tot_params * 4 / 1024**2:.2f} MB")

# x = [torch.randn(4, 3, 512, 512) for _ in range(10)]

# logelapsed = 0
# start = time.time()
# with torch.no_grad():
#     for (step, batch) in enumerate(x):
#         model(batch)
        
#         logtime = time.time()
#         if (step + 1) % 2 == 0:
#             print(f"Batch {step + 1}/{len(x)}") 
#         logelapsed += time.time() - logtime
    

# print(f"Elapsed time per-batch: {(time.time() - start) / len(x):.3f} s, for log: {logelapsed:.3f} s")
