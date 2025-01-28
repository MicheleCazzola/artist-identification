from dataclasses import dataclass

from src.utils.utils import BackboneType


@dataclass
class PathConfig:
    root: str = "./data/artist_dataset"
    test_root: str = "./data/kaggle_testset"
    stats_file: str = "./scripts/stats/stats.json"
    norm_stats_file: str = "./data/norm_stats.json"
    saved_model_path: str = "./temp/model"
    saved_best_model_path: str = "./temp/best_model"
    results_root: str = "."
    trained_model_path: str = "/content/drive/MyDrive/mlvm_shared/20250114_185257/temp/model_20.pth.tar"   # Change in case of custom inference-only model
    predictions_path: str = "/content/drive/MyDrive/mlvm_shared/20241230_225438/predictions.csv"    # Change according to trained model used

@dataclass
class EnvConfig:
    device: str = "cuda"
    num_workers: int = 2
    seed: int = 42

@dataclass
class DataConfig:
    pretrained_stats: bool = False
    resize_dim: int = 512
    crop_dim: int = 512
    aug_probs: tuple[float] = (0.5, 0.5, 0.5, 0.5)
    aug_mask: tuple[bool] = (True, True, True, True)
    augment: bool = True
    reduce_factor: float = 1.0
    batch_size_model: int = 16
    batch_size_stats: int = 128

@dataclass
class TrainConfig:
    num_epochs: int = 30
    train_log_frequency: int = 30
    val_log_frequency: int = 10
    train_accuracy: bool = False
    lr: float = 1e-4
    momentum: float = 0.9
    weight_decay: float = 1e-4
    scheduler_milestones: tuple[int] = (10,)
    scheduler_factors: tuple[float] = (0.1,)
    criterion: str = "cross_entropy"
    optimizer: str = "adamw"
    scheduler: str = None
    top_k: int = 5
    sanity_check: bool = False
    save_models: bool = False
    save_models_step: int = 5
    train_only: bool = False
    inference_only: bool = False
    train_acc_only: bool = False
    save_predictions: bool = False
    resume_training: bool = False

@dataclass
class ModelConfig:
    use_default_init: bool = True
    backbone_type: BackboneType = None
    use_handcrafted: bool = False
    precision: int = 32

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