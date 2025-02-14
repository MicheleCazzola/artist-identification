from src.config.components import DataConfig
from torchvision.transforms import transforms
from src.transformations.augmentations import Augmentations


class Transforms:
    """
    Transforms class to handle the transformations for the input images.
    
    Class Attributes:
    -----------
    resizer: callable
        Resize transformation
    cropper: callable
        Crop transformation
    to_tensor: callable
        Convert image to tensor transformation
    to_image: callable
        Convert tensor to image transformation
        
    Instance attributes:
    --------------------
    type: str
        Type of the transformation (either 'model' or 'stats')
    keys: list[str]
        List of possible transformations
    normalizer: callable
        Normalization function
    mean: list[float]
        Mean values for normalization
    std: list[float]
        Standard deviation values for normalization
    normalizer: callable
        Normalize tensor transformation
    preprocessing: list[callable]
        Preprocessing transformations
    augmentations: Augmentations
        Augmentation transformations
    transforms: dict
        Dictionary of transformations applied on the image
        
    Methods:
    --------
    get(name: str | list[str] = None) -> dict | transforms.Compose
        Get the transformation(s) by name
    set_norm(mean: list[float], std: list[float])
        Set the normalization values
    to_dict() -> dict
        Convert the transformations to a dictionary
    """
    
    resizer = transforms.Resize
    cropper = transforms.CenterCrop
    to_tensor = transforms.ToTensor
    to_image = transforms.ToPILImage
    
    def __init__(self, type: str = "model", data_config: DataConfig = None):
        
        assert type in ["model", "stats"], f"Type must be either 'model' or 'stats', found {type} instead"
        assert data_config is not None, "No config found"
        
        self.type = type
        
        # Default values for normalization (ImageNet)
        # Not used in reality, we compute ours
        self.mean = [0.485, 0.456, 0.406]
        self.std = [0.229, 0.224, 0.225]
        
        # Preprocessing when using the model
        if type == "model":
            self.keys = ["train_base", "train_norm", "train_aug", "eval"]
            self.normalizer = lambda m, s: transforms.Normalize(m, s)
            
            self.preprocessing = [
                Transforms.resizer(data_config.resize_dim),
                Transforms.cropper(data_config.crop_dim)
            ]
            self.augmentations = Augmentations(data_config.aug_probs, data_config.aug_mask)
            
            # Downsample + center crop
            train_transforms_base = transforms.Compose([*self.preprocessing, Transforms.to_tensor()])
            
            # Downsample + center crop + normalize
            train_transforms_norm = transforms.Compose([*self.preprocessing, Transforms.to_tensor(), self.normalizer(self.mean, self.std)])
            
            # Downsample + center crop + augmentation + normalize
            train_transforms_aug = transforms.Compose([*self.preprocessing, self.augmentations, Transforms.to_tensor(), self.normalizer(self.mean, self.std)])
            
            # Downsample + center crop + normalize (evaluation)
            eval_transforms = transforms.Compose([*self.preprocessing, Transforms.to_tensor(), self.normalizer(self.mean, self.std)])
            
            self.transforms = dict(zip(self.keys, [train_transforms_base, train_transforms_norm, train_transforms_aug, eval_transforms]))
        
        # Preprocessing when computing the stats
        else:
            self.keys = ["tensor", "adjust"]
            
            # Only conversion to tensor: used when computing shape stats
            to_tensor = transforms.Compose([
                Transforms.to_tensor()
            ])
            
            # Conversion to tensor + resizing + center cropping: used when computing normalization stats
            to_adjusted = transforms.Compose([
                Transforms.to_image(),
                Transforms.resizer(data_config.resize_dim),
                Transforms.cropper(data_config.crop_dim),
                Transforms.to_tensor()
            ])
            
            self.transforms = dict(zip(self.keys, [to_tensor, to_adjusted]))

    def get(self, name: str | list[str] = None) -> dict | transforms.Compose:
        """Get the transformation(s) by name"""
        
        assert name is None or name in self.keys or all(name) in self.keys, f"Can get all or one transform into {self.keys}, found {name} instead"
                
        if isinstance(name, list):
            return {k: self.transforms[k] for k in name}
        elif name is not None:
            return self.transforms[name]
        else:
            return self.transforms
    
    def set_norm(self, mean: list[float], std: list[float]):
        """Set the normalization values. Necessary to modify the transformation pipelines"""
        self.mean = mean
        self.std = std
        
        self.transforms["train_aug"].transforms[-1] = self.normalizer(self.mean, self.std)
        self.transforms["train_norm"].transforms[-1] = self.normalizer(self.mean, self.std)
        self.transforms["eval"].transforms[-1] = self.normalizer(self.mean, self.std)
        
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