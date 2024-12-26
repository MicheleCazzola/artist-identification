import torch
from torchvision import transforms
from torchvision.models import resnet18, mobilenet_v3_small, efficientnet_b0, regnet_x_400mf, shufflenet_v2_x0_5, mnasnet0_5

import torch.nn as nn
import torch.nn.functional as F

from ..utils.utils import BackboneType

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
        self.sampler = lambda x, g: F.grid_sample(x, g, align_corners=False)

    def _make_loc_net(self):
        match self.backbone_type:
            case self.backbone_type.RESNET18:
                model = resnet18(weights="IMAGENET1K_V1")
                last_in_features = model.fc.in_features
                model.fc = nn.Linear(last_in_features, 6)
            case self.backbone_type.MOBILENET_V3_SMALL:
                model = mobilenet_v3_small(weights="IMAGENET1K_V1")
                last_in_features = model.classifier[3].in_features
                model.classifier[3] = nn.Linear(last_in_features, 6)
            case self.backbone_type.EFFICIENTNET_B0:
                model = efficientnet_b0(weights="IMAGENET1K_V1")
                last_in_features = model.classifier[1].in_features
                model.classifier[1] = nn.Linear(last_in_features, 6)
            case self.backbone_type.REGNET_X_400MF:
                model = regnet_x_400mf(weights="IMAGENET1K_V1")
                last_in_features = model.fc.in_features
                model.fc = nn.Linear(last_in_features, 6)
            case self.backbone_type.SHUFFLENET_V2_X0_5:
                model = shufflenet_v2_x0_5(weights="IMAGENET1K_V1")
                last_in_features = model.fc.in_features
                model.fc = nn.Linear(last_in_features, 6)
            case self.backbone_type.MNASNET0_5:
                model = mnasnet0_5(weights="IMAGENET1K_V1")
                last_in_features = model.classifier[1].in_features
                model.classifier[1] = nn.Linear(last_in_features, 6)
            case _:
                raise ValueError(f"Unknown backbone type: {self.backbone_type}")
        return model

    def forward(self, x: torch.Tensor) -> torch.Tensor:
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