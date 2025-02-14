import torch
import torch.nn as nn

from src.utils.utils import BackboneType
from src.config.config import HOGConfig
from src.model.backbone import ROIsProposal
from src.model.components import BottleneckBlock, JoinModule, HandCraftedFeatures


class MultiBranchArtistNetwork(nn.Module):
    """
    Network architecture with three parallel branches, used for our task
    Each branch is a ResNet-like architecture based on bottleneck blocks
    The branches are joined and passed through additional residual blocks, designed as the previous ones
    The output layer is a fully connected layer with the number of classes
    
    Attributes:
    -----------
    num_classes: int
        Number of classes in the classification task
    stn: BackboneType
        Backbone type for the Spatial Transformer Network (if None, no STN is used)
    use_handcrafted: bool
        Whether to use handcrafted features in the network
    hog_params: HOGConfig
        Configuration for the HOG feature extractor
    use_default_init: bool
        Whether to use the default (PyTorch) initialization for the weights and biases
    precision: int
        Precision of the network weights and biases (32, 16, 8, 64), 32 bit is the default (as in PyTorch)
    
    Methods:
    --------
    _init_weights()
        Initialize the weights and biases of the network, as in the ResNet architecture
    _get_dtype(precision: int) -> torch.dtype
        Get the data type based on the precision
    _make_branch(in_channels: int, out_channels: int) -> nn.Sequential
        Create a single branch of the network
    _make_residual_blocks(in_channels: int, out_channels: int, num_blocks: int, stride: int) -> nn.Sequential
        Create a sequence of residual blocks: the first block could have a different stride
    forward(x: torch.Tensor) -> torch.Tensor
        Forward pass of the network
    """
    def __init__(
        self,
        num_classes: int,
        stn: BackboneType = None,
        use_handcrafted: bool = True,
        hog_params: HOGConfig = None, 
        use_default_init: bool = False,
        precision: int = 32
    ):
        super(MultiBranchArtistNetwork, self).__init__()
        
        if precision != 32 and stn:
            raise ValueError("STN only supported with 32-bit precision")
        
        assert not use_handcrafted or hog_params is not None, "HOG configuration must be provided if handcrafted features are used"
        
        self.num_classes = num_classes
        self.dtype = self._get_dtype(precision)
        
        # Region of Interests proposal module
        self.roi_extractor = ROIsProposal(256, 224, stn=stn).type(self.dtype)
        
        # Parallel branches
        self.branch1 = self._make_branch(3, 256).type(self.dtype)
        self.branch2 = self._make_branch(3, 256).type(self.dtype)
        self.branch3 = self._make_branch(3, 256).type(self.dtype)
        
        # Joining module
        self.join = JoinModule(256 * 3).type(self.dtype)
        
        # Residual blocks to process the joined branches
        self.resblock1 = self._make_residual_blocks(256, 512, 3, 2).type(self.dtype)
        self.resblock2 = self._make_residual_blocks(512, 1024, 6, 2).type(self.dtype)
        self.resblock3 = self._make_residual_blocks(1024, 2048, 4, 2).type(self.dtype)
        
        # Final average pooling
        self.avg_pool = nn.AdaptiveAvgPool2d((1, 1)).type(self.dtype)
        
        # Handcrafted features and corresponding classifier
        if use_handcrafted:
            self.handcrafted = HandCraftedFeatures(hog_params, dtype=self.dtype)
            self.classifier = nn.Linear(2048 + hog_params.output_size, num_classes, dtype=self.dtype)
        else:
            self.handcrafted = None
            self.classifier = nn.Linear(2048, num_classes, dtype=self.dtype)
            
        # Custom initialization of the weights and biases
        if not use_default_init:
            self._init_weights()
                        
    def _init_weights(self):
        # Same initialization as ResNet (Kaiming normal, constant for BatchNorm)
        for m in self.modules():
            if m not in self.roi_extractor.modules():
                if isinstance(m, nn.Conv2d):
                    nn.init.kaiming_normal_(m.weight, mode="fan_out", nonlinearity="relu")
                elif isinstance(m, nn.BatchNorm2d):
                    nn.init.constant_(m.weight, 1)
                    nn.init.constant_(m.bias, 0)
                
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
        """
        Build a single branch of the network: it is a sequence of residual blocks, with possible downsampling and variation in the
        number of channels and residual blocks, and an initial input layer performing aggressive downsampling
        
        in_channels: int
            Number of input channels
        out_channels: int
            Number of output channels
        """
        
        # Initial layer: aggressive downsampling
        initial = nn.Sequential(
            nn.Conv2d(in_channels, 64, kernel_size=7, stride=1, padding=3, bias=False),
            nn.BatchNorm2d(64, dtype=self.dtype),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1)
        )
        
        # Residual blocks: 3 blocks with 2x downsampling in the first block and variable number of output channels
        resblocks = self._make_residual_blocks(64, out_channels, num_blocks=3, stride=2)
        
        return nn.Sequential(initial, resblocks)

    def _make_residual_blocks(self, in_channels: int, out_channels: int, num_blocks: int, stride: int) -> nn.Sequential:
        """
        Build a sequence of residual blocks: the first block could have a different stride (downsampling) and it could also perform
        a change in the number of channels.
        
        in_channels: int
            number of input channels
        out_channels: int
            number of output channels
        num_blocks: int
            number of residual blocks
        stride: int
            stride of the first block (downsampling factor)
        """
        layers = [BottleneckBlock(in_channels, out_channels, stride=stride)]
        layers.extend([BottleneckBlock(out_channels, out_channels) for _ in range(num_blocks - 1)])
        return nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        
        # Extract regions of interest
        x1, x2, x3 = self.roi_extractor(x)
        
        # Process each region with the corresponding branch
        b1 = self.branch1(x1)
        b2 = self.branch2(x2)
        b3 = self.branch3(x3)
        
        # Join the branches
        joined = self.join(b1, b2, b3)
        
        # Process the joined branches with residual blocks
        out = self.resblock1(joined)
        out = self.resblock2(out)
        out = self.resblock3(out)
        out = self.avg_pool(out)
        
        out = torch.flatten(out, 1)
        
        # Add handcrafted features if needed
        if self.handcrafted is not None:
            hand_crafted = self.handcrafted(x)
            out = torch.cat((out, hand_crafted), dim=1)
        
        # Final classification
        out = self.classifier(out)
        return out