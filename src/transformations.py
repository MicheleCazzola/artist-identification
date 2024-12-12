from src.constants import Constants, Env
from torchvision.transforms import transforms
import json


def load_stats(filename: str):
    mean, devstd = map(json.load(open(filename, mode="r", encoding="utf-8")).get, ["mean", "devstd"])

    return mean, devstd

class Transforms:
    
    resizer = transforms.Resize
    cropper = transforms.CenterCrop
    to_tensor = transforms.ToTensor
    to_image = transforms.ToPILImage
    normalizer = transforms.Normalize

    sample_aug = transforms.RandomHorizontalFlip(p = 1)
    random_apply = transforms.RandomApply
    aug_transform = sample_aug
    
    def __init__(self, type: str = "model", constants: Constants = Env().constants):
        
        assert type in ["model", "stats"], f"Type must be either 'model' or 'stats', found {type} instead"
        self.type = type
        
        if type == "model":
            self.keys = ["train", "eval", "aug"]
            mean, devstd = load_stats(constants.stats_file)
            train_transforms = transforms.Compose([
                Transforms.resizer(constants.resize_dim),
                Transforms.cropper(constants.crop_dim),
                Transforms.to_tensor()
            ])
            eval_transforms = transforms.Compose([
                Transforms.resizer(constants.resize_dim),
                Transforms.cropper(constants.crop_dim),
                Transforms.to_tensor()
            ])
            aug_pipeline = transforms.Compose([
                Transforms.to_image(),
                Transforms.random_apply([Transforms.aug_transform], p = constants.aug_prob),
                Transforms.to_tensor(),
                Transforms.normalizer(mean, devstd)
            ])
            
            self.transforms = dict(zip(self.keys, [train_transforms, eval_transforms, aug_pipeline]))
        else:
            self.keys = ["tensor", "adjust"]
            to_tensor = transforms.Compose([
                Transforms.to_tensor()
            ])
            to_adjusted = transforms.Compose([
                Transforms.to_image(),
                Transforms.resizer(constants.resize_dim),
                Transforms.cropper(constants.crop_dim),
                Transforms.to_tensor()
            ])
            
            self.transforms = dict(zip(self.keys, [to_tensor, to_adjusted]))

    def get(self, name: str = None) -> dict | transforms.Compose:
        
        assert name is None or name in self.keys, f"Can get all or one transform into {self.keys}, found {name} instead"
                
        return self.transforms[name] if name is not None else self.transforms
            
            
            