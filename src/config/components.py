from dataclasses import dataclass

from ..utils.utils import BackboneType


@dataclass
class PathConfig:
    default_root: str = "./data/artist_dataset"
    test_root: str = "./data/kaggle_test"
    stats_file: str = "./scripts/stats/stats.json"
    norm_stats_file: str = "./temp/norm_stats.json"
    best_model_path: str = "./temp/best_model"
    results_root: str = "."
    trained_model_path: str = "./temp/best_model_3.pth"   # Change in case of custom inference-only model
    predictions_path: str = "./temp/predictions.csv"    # Change according to trained model used

@dataclass
class EnvConfig:
    device: str = "cuda"
    num_workers: int = 2

@dataclass
class DataConfig:
    pretrained_stats: bool = False
    resize_dim: int = 512
    crop_dim: int = 512
    aug_probs: tuple[float] = (0.2, 0.2, 0.2, 0.5)
    aug_mask: tuple[bool] = (True, True, True, True)
    augment: bool = False
    reduce_factor: float = 1.0
    batch_size_model: int = 16
    batch_size_stats: int = 256
    train_split_size: float = 0.75

@dataclass
class TrainConfig:
    num_epochs: int = 2
    train_log_frequency: int = 30
    val_log_frequency: int = 10
    train_accuracy: bool = False
    num_classes: int = 161
    lr: float = 3e-4
    momentum: float = 0.9
    weight_decay: float = 1e-5
    scheduler_step_size: int = 10
    scheduler_gamma: float = 0.1
    criterion: str = "cross_entropy"
    optimizer: str = "adam"
    scheduler: str = "step_lr"
    top_k: int = 5
    sanity_check: bool = False
    save_models: bool = True
    train_only: bool = False
    inference_only: bool = True
    save_predictions: bool = False

@dataclass
class ModelConfig:
    backbone_type: BackboneType = BackboneType.RESNET18
    use_handcrafted: bool = True
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