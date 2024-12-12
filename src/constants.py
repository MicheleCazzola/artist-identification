from dataclasses import dataclass

@dataclass
class Constants:
    
    default_root: str = "./data/artist_dataset"
    stats_file: str = "./scripts/stats/stats.json"
        
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
        
        
class Env:
    def __init__(self, target: str = "colab"):
        
        assert target in ["local", "colab"], f"Target must be either 'local' or 'colab', found {target}"
        
        if target == "colab":
            self.constants = Constants()
        else:
            self.constants = Constants(
                default_root="./scripts/stats/images/artist_dataset",
                stats_file="./scripts/stats/stats.json",
                device="cpu",
                num_workers=0,
                batch_size=2,
                num_epochs=3,
                train_split_size=0.66
            ) 