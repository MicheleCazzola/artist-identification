from dataclasses import dataclass

from src.utils.utils import BackboneType


@dataclass
class PathConfig:
    """
    Configuration for paths
    
    root: str
        Root path of the dataset
    norm_stats_file: str
        Path to the normalization statistics file
    saved_model_path: str
        Path to save a given model/checkpoint
    saved_best_model_path: str
        Path to save the best model/checkpoint
    results_root: str
        Root path to save results folder
    trained_model_path: str
        Path to the trained model/checkpoint (if resuming training) or pretrained model (if inference only)
    """
    
    root: str = "./data/artist_dataset"
    norm_stats_file: str = "./data/norm_stats.json"
    saved_model_path: str = "./temp/model"
    saved_best_model_path: str = "./temp/best_model"
    results_root: str = "."
    trained_model_path: str = ""   # Change in case of custom inference-only model or training resume
    
@dataclass
class EnvConfig:
    """
    Configuration for environment
    
    device: str
        Device to use for training and inference
    num_workers: int
        Number of workers for the dataloaders
    seed: int
        Seed for reproducibility
    """
    device: str = "cuda"
    num_workers: int = 2
    seed: int = 42

@dataclass
class DataConfig:
    """
    Configuration for data processing
    
    pretrained_stats: bool
        Use normalization statistics of ImageNet
    resize_dim: int
        Resize dimension for the input image
    crop_dim: int
        Crop dimension for the input image
    aug_probs: tuple[float]
        Probabilities for each augmentation
    aug_mask: tuple[bool]
        Masks for each augmentation
    augment: bool
        Apply augmentations
    reduce_factor: float
        Reduce the dataset by a factor in (0, 1], constrained by data availability
    batch_size_model: int
        Batch size for the model runs
    batch_size_stats: int
        Batch size for the statistics computations (could be higher)
    """
    pretrained_stats: bool = False
    resize_dim: int = 512
    crop_dim: int = 512
    aug_probs: tuple[float] = (0.5, 0.5, 0.5, 0.5)
    aug_mask: tuple[bool] = (True, True, True, True)
    augment: bool = False
    reduce_factor: float = 1.0
    batch_size_model: int = 16
    batch_size_stats: int = 128

@dataclass
class TrainConfig:
    """
    Configuration for training
    
    num_epochs: int
        Number of epochs to train (included resumed ones)
    train_log_frequency: int
        Frequency to log training stats
    val_log_frequency: int
        Frequency to log validation stats
    train_accuracy: bool
        Compute training accuracy
    lr: float
        Learning rate
    momentum: float
        Momentum for the optimizer (SGD only)
    weight_decay: float
        Weight decay for the optimizer
    scheduler_milestones: tuple[int]
        Milestones for the scheduler (ignored if scheduler is constant or None): must be same length as factors
    scheduler_factors: tuple[float]
        Factors for the scheduler (ignored if scheduler is constant or None): must be same length as milestones, must be a single element if scheduler is multistep_lr
    criterion: str
        Loss function: either "cross_entropy" or "weighted_cross_entropy"
    optimizer: str
        Optimizer: either "sgd", "adam" or "adamw"
    scheduler: str
        Learning rate scheduler: either "multistep_lr", "custom_step_lr" or None (equivalent to "constant")
    top_k: int
        Top-k accuracy level
    sanity_check: bool
        Perform a sanity check before training
    save_models: bool
        Save models (or checkpoints) during training
    save_models_step: int
        Step for saving models (or checkpoints)
    train_only: bool
        Train only mode
    inference_only: bool
        Inference only mode: must provide a trained model path
    train_acc_only: bool
        Compute only accuracy on the training set: must provide a trained model path
    resume_training: bool
        Resume training from a checkpoint: must provide a trained model path, as checkpoint
    """
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
    resume_training: bool = False

@dataclass
class ModelConfig:
    """
    Configuration for the model
    
    use_default_init: bool
        Use default initialization (PyTorch)
    backbone_type: BackboneType
        Backbone type (random crop if not specified)
    use_handcrafted: bool
        Use handcrafted features (HOG, default is False)
    precision: int
        Floating-point precision (default 32 bit, PyTorch default)
    """
    use_default_init: bool = True
    backbone_type: BackboneType = None
    use_handcrafted: bool = False
    precision: int = 32

@dataclass
class HOGConfig:
    """
    Configuration for Histogram of Oriented Gradients (HOG)
    
    downsample_size: int
        Downsample size for the input image
    crop_size: int
        Center crop size for the input image
    channel_coefficients: tuple[float]    
        Channel coefficients to convert RGB to grayscale
    orientations: int
        Number of orientations
    pixels_per_cell: int
        Pixels per cell
    cells_per_block: int
        Cells per block, for normalization
    transform_sqrt: bool
        Enable square root transformation
    feature_vector: bool
        Output a 1-Dimensional feature vector
    normalization: str
        Normalization type
    """
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