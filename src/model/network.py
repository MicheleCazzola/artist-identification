import torch
import torch.nn as nn

from ..utils.utils import BackboneType
from ..config.config import HOGConfig
from .backbone import ROIsProposal
from .components import BottleneckBlock, JoinModule, HandCraftedFeatures


class MultiBranchArtistNetwork(nn.Module):
    def __init__(
        self,
        num_classes: int,
        stn: BackboneType = None,
        use_handcrafted: bool = True,
        hog_params: HOGConfig = None, 
        precision: int = 32
    ):
        super(MultiBranchArtistNetwork, self).__init__()
        
        if precision != 32 and stn:
            raise ValueError("STN only supported with 32-bit precision")
        
        assert not use_handcrafted or hog_params is not None, "HOG configuration must be provided if handcrafted features are used"
        
        self.num_classes = num_classes
        self.dtype = self._get_dtype(precision)
        
        self.roi_extractor = ROIsProposal(256, 224, stn=stn).type(self.dtype)
        
        self.branch1 = self._make_branch(3, 256).type(self.dtype)
        self.branch2 = self._make_branch(3, 256).type(self.dtype)
        self.branch3 = self._make_branch(3, 256).type(self.dtype)
        
        self.join = JoinModule(256 * 3).type(self.dtype)
        
        self.resblock1 = self._make_residual_blocks(256, 512, 3, 2).type(self.dtype)
        self.resblock2 = self._make_residual_blocks(512, 1024, 6, 2).type(self.dtype)
        self.resblock3 = self._make_residual_blocks(1024, 2048, 4, 2).type(self.dtype)
        
        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1)).type(self.dtype)
        
        if use_handcrafted:
            self.handcrafted = HandCraftedFeatures(hog_params, dtype=self.dtype)
            self.classifier = nn.Linear(2048 + hog_params.output_size, num_classes, dtype=self.dtype)
        else:
            self.handcrafted = None
            self.classifier = nn.Linear(2048, num_classes, dtype=self.dtype)
            
    def _get_dtype(self, precision: int) -> torch.dtype:
        if precision == 16:
            return torch.float16
        if precision == 32:
            return torch.float32
        if precision == 64:
            return torch.float64
        if precision == 8:
            return torch.float8_e5m2
        
        raise ValueError(f"Precision {precision} not supported")

    def _make_branch(self, in_channels: int, out_channels: int) -> nn.Sequential:
        initial = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=7, stride=1, padding=3, bias=False),
            nn.BatchNorm2d(64, dtype=self.dtype),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        resblocks = self._make_residual_blocks(64, out_channels, num_blocks=3, stride=2)
        
        return nn.Sequential(initial, resblocks)

    def _make_residual_blocks(self, in_channels: int, out_channels: int, num_blocks: int, stride: int) -> nn.Sequential:
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