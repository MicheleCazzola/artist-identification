from dataclasses import dataclass, field

from src.utils.utils import BackboneType
from .components import PathConfig, EnvConfig, DataConfig, TrainConfig, ModelConfig, HOGConfig

@dataclass
class Config:

    path: PathConfig = field(default_factory=PathConfig)
    env: EnvConfig = field(default_factory=EnvConfig)
    data: DataConfig = field(default_factory=DataConfig)
    train: TrainConfig = field(default_factory=TrainConfig)
    model: ModelConfig = field(default_factory=ModelConfig)
    hog: HOGConfig = field(default_factory=HOGConfig)

    def __post_init__(self):
        self.train.top_k = min(5, self.train.num_classes)
        
    def to_dict(self) -> dict:
        return {
            "path": self.path.__dict__,
            "env": self.env.__dict__,
            "data": self.data.__dict__,
            "train": self.train.__dict__,
            "model": self.model.__dict__,
            "hog": self.hog.__dict__
        }
    
    @staticmethod
    def create(target: str = "colab") -> "Config":

        assert target in ["local", "colab"], f"Target must be either 'local' or 'colab', found {target}"

        if target == "local":
            return Config(
                path=PathConfig(
                    default_root="./scripts/stats/images/artist_dataset",
                    test_root="./scripts/stats/images/kaggle_test",
                    stats_file="./scripts/stats/stats.json",
                    results_root="./out",
                    trained_model_path="./temp/best_model.pth",
                ),
                env=EnvConfig(
                    device="cpu",
                    num_workers=0
                ),
                data=DataConfig(
                    pretrained_stats=True,
                    batch_size_model=2,
                    batch_size_stats=2,
                    train_split_size=0.66,
                    reduce_factor=1,
                    augment=True
                ),
                train=TrainConfig(
                    num_epochs=1,
                    train_log_frequency=2,
                    val_log_frequency=1,
                    num_classes=3,
                    train_only=False,
                    inference_only=False,
                    save_predictions=False,
                    criterion="cross_entropy",
                    resume_training=False
                ),
                model=ModelConfig(
                    precision=32,
                    use_handcrafted=False,
                    backbone_type=None
                )
            )
            
        return Config()
