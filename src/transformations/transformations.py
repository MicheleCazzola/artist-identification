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
            self.keys = ["train", "eval", "aug"]
            
            base_transforms = transforms.Compose([
                Transforms.resizer(data_config.resize_dim),
                Transforms.cropper(data_config.crop_dim),
                Transforms.to_tensor()
            ])
            
            train_transforms = base_transforms
            eval_transforms = base_transforms
            
            aug_pipeline = {
                "train": transforms.Compose([
                    Transforms.to_image(),
                    Augmentations(data_config.aug_probs, data_config.aug_mask),
                    Transforms.to_tensor(), 
                    Transforms.normalizer(self.mean, self.std)
                ]),
                "val": transforms.Compose([
                    Transforms.normalizer(self.mean, self.std)
                ])
            } 
            
            self.transforms = dict(zip(self.keys, [train_transforms, eval_transforms, aug_pipeline]))
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

    def get(self, name: str = None) -> dict | transforms.Compose:
        
        assert name is None or name in self.keys, f"Can get all or one transform into {self.keys}, found {name} instead"
                
        return self.transforms[name] if name is not None else self.transforms
    
    def set_norm(self, mean: list[float], std: list[float]):
        self.mean = mean
        self.std = std  
        
        self.transforms.get("aug")["train"].transforms[-1] = Transforms.normalizer(self.mean, self.std)
        self.transforms.get("aug")["val"].transforms[-1] = Transforms.normalizer(self.mean, self.std)
        
    def __repr__(self):
        return f"Transforms(type={self.type}, keys={self.keys}, mean={self.mean}, std={self.std}, transforms={self.transforms})"
            
    def to_dict(self) -> dict:
        transforms_dict = {
            k: list(str(t) for t in v.transforms) for k, v in self.transforms.items() if isinstance(v, transforms.Compose)
        }
        transforms_dict.update({k: {t: list(str(tr) for tr in val.transforms)} for k, v in self.transforms.items() if isinstance(v, dict) for t, val in v.items() })
        
        return {
            "type": self.type,
            "keys": self.keys,
            "mean": self.mean,
            "std": self.std,
            "transforms": transforms_dict
        }        