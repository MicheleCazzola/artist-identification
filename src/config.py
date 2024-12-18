from dataclasses import dataclass
from src.network import BackboneType

@dataclass
class Config:
    
    default_root: str = "./data/artist_dataset"
    stats_file: str = "./scripts/stats/stats.json"
    norm_stats_file: str = "./temp/norm_stats.json"
    results_root: str = "."
    plots_dir: str = "."
    files_dir: str = "."
        
    device: str = "cuda"
    num_workers: int = 2
        
    resize_dim: int = 512
    crop_dim: int = 512
    aug_probs: tuple[float] = (0.2, 0.2, 0.2, 0.5)
    
    train_split_size: float = 0.75
    reduce_factor: float = 0.1
    batch_size: int = 4
    num_epochs: int = 10
    log_frequency: int = 100
        
    num_classes: int = 161
    lr: float = 1e-3
    momentum: float = 0.9
    weight_decay: float = 0
    scheduler_step_size: int = 7
    scheduler_gamma: float = 0.1
    criterion: str = "cross_entropy"
    optimizer: str = "sgd"
    scheduler: str = "step_lr"
    top_k: int = 5
    augment: bool = False
    train_accuracy: bool = False
    
    backbone_type = BackboneType = BackboneType.RESNET18
    use_handcrafted: bool = True
        
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
            "num_epochs": 3,
            "train_split_size": 0.66,
            "log_frequency": 1,
            "results_root": "./out",
            "plots_dir": "plots",
            "files_dir": "files",
            "num_classes": 3,
            "reduce_factor": None
        } if target == "local" else {}
        
        return Config(**params)
