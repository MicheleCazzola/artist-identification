from ..config.components import DataConfig
from torchvision.transforms import transforms
from .augmentations import Augmentations


class Transforms:
    
    resizer = transforms.Resize
    cropper = transforms.CenterCrop
    to_tensor = transforms.ToTensor
    to_image = transforms.ToPILImage
    normalizer = transforms.Normalize
    
    def __init__(self, type: str = "model", data_config: DataConfig = None):
        
        assert type in ["model", "stats"], f"Type must be either 'model' or 'stats', found {type} instead"
        assert data_config is not None, "No config found"
        
        self.type = type
        
        # Default values for normalization (ImageNet)
        self.mean = [0.485, 0.456, 0.406]
        self.std = [0.229, 0.224, 0.225]
        
        if type == "model":
            self.keys = ["train_base", "train_norm", "train_aug", "eval"]
            self.normalizer = lambda m, s: Transforms.normalizer(m, s)
            
            preprocessing = [
                Transforms.resizer(data_config.resize_dim),
                Transforms.cropper(data_config.crop_dim)
            ]
            augmentations = Augmentations(data_config.aug_probs, data_config.aug_mask)
            
            train_transforms_base = transforms.Compose([*preprocessing, Transforms.to_tensor()])
            train_transforms_norm = transforms.Compose([*preprocessing, Transforms.to_tensor(), self.normalizer(self.mean, self.std)])
            train_transforms_aug = transforms.Compose([*preprocessing, augmentations, Transforms.to_tensor(), self.normalizer(self.mean, self.std)])
            eval_transforms = transforms.Compose([*preprocessing, Transforms.to_tensor(), self.normalizer(self.mean, self.std)])
            
            self.transforms = dict(zip(self.keys, [train_transforms_base, train_transforms_norm, train_transforms_aug, eval_transforms]))
        else:
            self.keys = ["tensor", "adjust"]
            to_tensor = transforms.Compose([
                Transforms.to_tensor()
            ])
            to_adjusted = transforms.Compose([
                Transforms.to_image(),
                Transforms.resizer(data_config.resize_dim),
                Transforms.cropper(data_config.crop_dim),
                Transforms.to_tensor()
            ])
            
            self.transforms = dict(zip(self.keys, [to_tensor, to_adjusted]))

    def get(self, name: str | list[str] = None) -> dict | transforms.Compose:
        
        assert name is None or name in self.keys or all(name) in self.keys, f"Can get all or one transform into {self.keys}, found {name} instead"
                
        if isinstance(name, list):
            return {k: self.transforms[k] for k in name}
        elif name is not None:
            return self.transforms[name]
        else:
            return self.transforms
    
    def set_norm(self, mean: list[float], std: list[float]):
        self.mean = mean
        self.std = std
        
    def __repr__(self):
        return f"Transforms(type={self.type}, keys={self.keys}, mean={self.mean}, std={self.std}, transforms={self.transforms})"
            
    def to_dict(self) -> dict:
        transforms_dict = {
            k: list(str(t) for t in v.transforms) for k, v in self.transforms.items()
        }
        
        return {
            "type": self.type,
            "keys": self.keys,
            "mean": self.mean,
            "std": self.std,
            "transforms": transforms_dict
        }        