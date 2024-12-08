from dataclasses import dataclass

@dataclass
class Constants:
    
    @dataclass
    class Paths:
        DEFAULT_ROOT: str = "./data/artist_dataset"
        STATS_FILE: str = "./scripts/stats/stats.json"
        
    @dataclass
    class Env:
        DEVICE: str = "cuda"
        NUM_WORKERS: int = 4
        
    @dataclass
    class Img:
        RESIZE_DIM: int = 256
        CROP_DIM: int = 224
        AUG_PROB: float = 0.5
    
    @dataclass
    class Train:    
        TRAIN_SPLIT_SIZE: float = 0.75
        BATCH_SIZE: int = 256