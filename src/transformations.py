from dataclasses import dataclass
import logging

import torch
from src.config import Config
from torchvision.transforms import transforms
import json
from sklearn.decomposition import PCA
import numpy as np
from PIL import Image


def load_stats(filename: str):
    mean, devstd = map(json.load(open(filename, mode="r", encoding="utf-8")).get, ["mean", "devstd"])

    return mean, devstd


class LightingNoise:
    
    def __init__(self, alpha: float = 0.1, dim: int = 3):
        self.alpha = alpha
        self.dim = dim
        
    def __call__(self, img: Image.Image) -> Image.Image:
        img: torch.Tensor = transforms.ToTensor()(img)
        samples = img.view(self.dim, -1).numpy().T  # img of shape 3 x (H*W) -> (H*W) samples of 3 features
        
        pca = PCA()
        pca.fit(samples)
        
        noise = pca.components_.T @ (self.alpha * np.random.randn(self.dim) * pca.explained_variance_)  # eigenvectors * (rnd[i] * eigenvalues[i])
        
        img += torch.tensor(noise).view(self.dim, 1, 1)
        
        return transforms.ToPILImage()(img.clamp(0, 1))
    
class Augmentations:
    def __init__(
        self,
        probabilities: list[float] | tuple[float],
        jitter_brightness: float = 0.1, 
        jitter_contrast: float = 0.1,
        jitter_saturation: float = 0.1,
        blur_size: tuple[int] = (5, 5), 
        blur_sigma: tuple[float] = (0.5, 1.5), 
        crop_scale: tuple[float] = (0.85, 1.0), 
        crop_ratio: tuple[float] = (0.8, 1.25)
    ):
        # Not too much, palette is already colorful
        color_jitter = transforms.ColorJitter(brightness=jitter_brightness, contrast=jitter_contrast, saturation=jitter_saturation)
        # PCA-based lighting noise, AlexNet style
        lighting_noise = LightingNoise()
        # 5x5 kernel since image is 512x512, wide sigma interval to have slight increasing blur
        gaussian_blur = transforms.GaussianBlur(kernel_size=blur_size, sigma=blur_sigma)
        # 512x512 to preserve image dimension, 0.85 to 1.0 to have slight zoom in, 0.8 to 1.25 to have slight change in proportions
        geometric_transform = transforms.RandomResizedCrop(size=(512, 512), scale=crop_scale, ratio=crop_ratio)
        
        self.probabilities = probabilities
        self.transformations = [color_jitter, lighting_noise, gaussian_blur, geometric_transform]
        
    def __call__(self, img: Image) -> Image:   
        transform_chain = transforms.Compose([
            transforms.RandomApply([aug], p) for aug, p in zip(self.transformations, self.probabilities)
        ])
        return transform_chain(img)


class Transforms:
    
    resizer = transforms.Resize
    cropper = transforms.CenterCrop
    to_tensor = transforms.ToTensor
    to_image = transforms.ToPILImage
    normalizer = transforms.Normalize
    
    def __init__(self, type: str = "model", config: Config = None):
        
        assert type in ["model", "stats"], f"Type must be either 'model' or 'stats', found {type} instead"
        assert config is not None, "No config found"
        
        self.type = type
        
        # Default values for normalization (ImageNet)
        self.mean = [0.485, 0.456, 0.406]
        self.std = [0.229, 0.224, 0.225]
        
        if type == "model":
            self.keys = ["train", "eval", "aug"]
            
            base_transforms = transforms.Compose([
                Transforms.resizer(config.resize_dim),
                Transforms.cropper(config.crop_dim),
                Transforms.to_tensor()
            ])
            
            train_transforms = base_transforms
            eval_transforms = base_transforms
            
            aug_pipeline = {
                "train": transforms.Compose([
                    Transforms.to_image(),
                    Augmentations(config.aug_probs),
                    Transforms.to_tensor(), 
                    transforms.Normalize(mean=self.mean, std=self.std)
                ]),
                "val": Transforms.normalizer(self.mean, self.std)
            } 
            
            self.transforms = dict(zip(self.keys, [train_transforms, eval_transforms, aug_pipeline]))
        else:
            self.keys = ["tensor", "adjust"]
            to_tensor = transforms.Compose([
                Transforms.to_tensor()
            ])
            to_adjusted = transforms.Compose([
                Transforms.to_image(),
                Transforms.resizer(config.resize_dim),
                Transforms.cropper(config.crop_dim),
                Transforms.to_tensor()
            ])
            
            self.transforms = dict(zip(self.keys, [to_tensor, to_adjusted]))

    def get(self, name: str = None) -> dict | transforms.Compose:
        
        assert name is None or name in self.keys, f"Can get all or one transform into {self.keys}, found {name} instead"
                
        return self.transforms[name] if name is not None else self.transforms
    
    def set_norm(self, mean: list[float], std: list[float]):
        self.mean = mean
        self.std = std  
            
            