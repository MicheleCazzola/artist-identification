from dataclasses import dataclass

@dataclass
class Config:
    
    default_root: str = "./data/artist_dataset"
    stats_file: str = "./scripts/stats/stats.json"
    results_plot_path: str = "."
    results_file_path: str = "."
        
    device: str = "cuda"
    num_workers: int = 2
        
    resize_dim: int = 256
    crop_dim: int = 224
    aug_prob: float = 0.5
    
    train_split_size: float = 0.75
    batch_size: int = 30
    num_epochs: int = 10
    log_frequency: int = 100
        
    num_classes: int = 161
    lr: float = 1e-3
    momentum: float = 0.9
    weight_decay: float = 1e-4
    scheduler_step_size: int = 7
    scheduler_gamma: float = 0.1
    criterion: str = "cross_entropy"
    optimizer: str = "sgd"
    scheduler: str = "step_lr"
    top_k: int = 5
        
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
            "results_plot_path": "./out/plots",
            "results_file_path": "./out/files",
            "num_classes": 3
        } if target == "local" else {}
        
        return Config(**params)
