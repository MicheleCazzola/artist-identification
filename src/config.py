from dataclasses import dataclass, field, asdict
from src.utils import BackboneType
import json

@dataclass
class HOGConfig:
    downsample_size: int = 256
    crop_size: int = 224
    channel_coefficients: tuple[float] = (0.2989, 0.5870, 0.1140)
    orientations: int = 9
    pixels_per_cell: int = crop_size // 3
    cells_per_block: int = 1
    transform_sqrt: bool = False        # DO NOT CHANGE: images could have negative values after normalization
    feature_vector: bool = True         # DO NOT CHANGE: want to use HOG as feature extractor
    normalization: str = "L2-Hys"
    
    def __post_init__(self):
        self.output_size = self.orientations * \
            self.cells_per_block ** 2 * \
            (self.crop_size // self.pixels_per_cell - self.cells_per_block + 1) ** 2

@dataclass
class Config:
    
    default_root: str = "./data/artist_dataset"
    stats_file: str = "./scripts/stats/stats.json"
    norm_stats_file: str = "./temp/norm_stats.json"
    results_root: str = "."
        
    device: str = "cuda"
    num_workers: int = 2
        
    pretrained_stats: bool = False
    resize_dim: int = 512
    crop_dim: int = 512
    aug_probs: tuple[float] = (0.2, 0.2, 0.2, 0.5)
    aug_mask: tuple[bool] = (True, False, True, True)
    
    train_split_size: float = 0.75
    reduce_factor: float = 1.0
    batch_size: int = 4
    num_epochs: int = 10
    train_log_frequency: int = 100
    val_log_frequency: int = 10
        
    num_classes: int = 161
    lr: float = 1e-3
    momentum: float = 0.9
    weight_decay: float = 0
    scheduler_step_size: int = 10
    scheduler_gamma: float = 0.1
    criterion: str = "cross_entropy"
    optimizer: str = "adam"
    scheduler: str = "step_lr"
    top_k: int = 5
    augment: bool = False
    train_accuracy: bool = False
    
    backbone_type: BackboneType = BackboneType.RESNET18
    use_handcrafted: bool = True
    
    hog_params: HOGConfig = field(default_factory=HOGConfig)
    
    precision: int = 32
        
    def __post_init__(self):
        self.top_k = min(5, self.num_classes)

    @staticmethod
    def create(target: str = "colab") -> "Config":
            
        assert target in ["local", "colab"], f"Target must be either 'local' or 'colab', found {target}"
        
        params = {
            "default_root": "./scripts/stats/images/artist_dataset",
            "stats_file": "./scripts/stats/stats.json",
            "device": "cpu",
            "num_workers": 0,
            "batch_size": 2,
            "num_epochs": 2,
            "train_split_size": 0.66,
            "train_log_frequency": 2,
            "val_log_frequency": 1,
            "results_root": "./out",
            "num_classes": 3,
            "reduce_factor": 1.0,
            "precision": 32
        } if target == "local" else {}
        
        return Config(**params)
