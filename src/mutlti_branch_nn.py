import time
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as T
from torchvision.models import resnet18
from skimage.feature import hog
import numpy as np


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1):
        super(ResidualBlock, self).__init__()
        bottleneck_channels = out_channels // 4

        self.conv1 = nn.Conv2d(in_channels, bottleneck_channels, kernel_size=1, stride=stride, bias=False)
        self.bn1 = nn.BatchNorm2d(bottleneck_channels)
        self.conv2 = nn.Conv2d(bottleneck_channels, bottleneck_channels, kernel_size=3, padding=1, bias=False)
        self.bn2 = nn.BatchNorm2d(bottleneck_channels)
        self.conv3 = nn.Conv2d(bottleneck_channels, out_channels, kernel_size=1, bias=False)
        self.bn3 = nn.BatchNorm2d(out_channels)

        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride, bias=False),
                nn.BatchNorm2d(out_channels)
            )

    def forward(self, x):
        out = F.relu(self.bn1(self.conv1(x)))
        out = F.relu(self.bn2(self.conv2(out)))
        out = self.bn3(self.conv3(out))
        out += self.shortcut(x)
        out = F.relu(out)
        return out

class ROIsProposal(nn.Module):
    def __init__(self, use_stn=True):
        super(ROIsProposal, self).__init__()
        self.use_stn = use_stn
        if use_stn:
            self.stn1 = self._make_stn()
            self.stn2 = self._make_stn()

    def _make_stn(self):
        # Using ResNet-18 as the localization network
        model = resnet18(weights="IMAGENET1K_V1")
        model.fc = nn.Linear(model.fc.in_features, 6)
        return model

    def forward(self, x):
        # Assume x is a batch of images resized to (512, 512)
        crops = []
        if self.use_stn:
            theta1 = self.stn1(x)
            grid1 = F.affine_grid(theta1.view(-1, 2, 3), size=(x.size(0), 3, 224, 224), align_corners=False)
            crops.append(F.grid_sample(x, grid1, align_corners=False))

            theta2 = self.stn2(x)
            grid2 = F.affine_grid(theta2.view(-1, 2, 3), size=(x.size(0), 3, 224, 224), align_corners=False)
            crops.append(F.grid_sample(x, grid2, align_corners=False))

        else:
            # Random cropping logic
            for _ in range(2):
                crop = T.RandomCrop(size=(224, 224))(x)
                crops.append(crop)

        # Low-resolution crop
        resized_x = T.Resize(size=(256, 256))(x)
        low_res = T.RandomCrop(size=(224, 224))(resized_x)
        crops.append(low_res)

        return crops

class HandCraftedFeatures(nn.Module):
    def __init__(self):
        super(HandCraftedFeatures, self).__init__()

    def forward(self, x):
        # Convert tensor to numpy for feature extraction
        x_np = x.cpu().numpy().transpose(0, 2, 3, 1)  # N, H, W, C
        features = []
        for img in x_np:
            gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
            hog_features = hog(gray, orientations=6, pixels_per_cell=(16, 16),
                               cells_per_block=(2, 2), block_norm='L2-Hys')
            features.append(hog_features)
        features = np.array(features)
        return torch.tensor(features, dtype=torch.float32, device=x.device)

class MultibranchNetwork(nn.Module):
    def __init__(
        self,
        out_classes: int,
        use_stn: bool = True,
        use_handcrafted: bool = True
    ):
        super(MultibranchNetwork, self).__init__()
        
        self.out_classes = out_classes
        self.use_stn = use_stn
        self.use_handcrafted = use_handcrafted

        # ROI proposal module
        self.roi_proposal = ROIsProposal(use_stn=use_stn)

        # Shared layers for three branches
        self.branch1 = self._make_branch()
        self.branch2 = self._make_branch()
        self.branch3 = self._make_branch()

        # Concatenation processing
        self.join_layer = ResidualBlock(768, 256, stride=1)

        # Common deep layers
        self.resblock1 = ResidualBlock(256, 512, stride=2)
        self.resblock2 = self._make_residual_block(512, 1024, num_blocks=5, stride=2)
        self.resblock3 = self._make_residual_block(1024, 2048, num_blocks=3, stride=2)

        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1))
        
        # Hand-crafted feature injection
        self.hand_crafted_features = HandCraftedFeatures() if use_handcrafted else None
        
        # Final classification layer
        self.fc_artist = nn.Linear(2048 + 4056, out_classes) if use_handcrafted else nn.Linear(2048, out_classes)

    def _make_branch(self):
        return nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
            self._make_residual_block(64, 256, num_blocks=3, stride=1)
        )

    def _make_residual_block(self, in_channels, out_channels, num_blocks, stride):
        strides = [stride] + [1] * (num_blocks - 1)
        layers = []
        for s in strides:
            layers.append(ResidualBlock(in_channels, out_channels, stride=s))
            in_channels = out_channels
        return nn.Sequential(*layers)

    def forward(self, x):
        # ROI proposal
        crops = self.roi_proposal(x)
        x1, x2, x3 = crops

        # Process each branch
        out1 = self.branch1(x1)
        out2 = self.branch2(x2)
        out3 = self.branch3(x3)

        # Concatenate feature maps along the channel dimension
        out = torch.cat([out1, out2, out3], dim=1)
        out = self.join_layer(out)

        # Common processing
        out = self.resblock1(out)
        out = self.resblock2(out)
        out = self.resblock3(out)
        
        out = self.avg_pool(out)
        out = torch.flatten(out, 1)

        # Hand-crafted features
        crop_size = 224
        x_cropped = T.CenterCrop(crop_size)(x)
        hand_crafted = self.hand_crafted_features(x_cropped)

        out = torch.cat([out, hand_crafted], dim=1)

        # Task-specific outputs
        artist = self.fc_artist(out)
        
        return artist
    
# model = MultibranchNetwork(out_classes=161)

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