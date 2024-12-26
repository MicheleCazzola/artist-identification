import torch
from torchvision.transforms import transforms
from sklearn.decomposition import PCA
import numpy as np
from PIL import Image


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
    
    def __repr__(self):
        return f"LightingNoise(alpha={self.alpha}, dim={self.dim})"
    
    
class Augmentations:
    def __init__(
        self,
        probabilities: list[float] | tuple[float],
        mask: list[bool] | tuple[bool],
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
        
        self.probabilities = [probability * flag for probability, flag in zip(probabilities, mask)]
        self.transformations = [color_jitter, lighting_noise, gaussian_blur, geometric_transform]
        
    def __call__(self, img: Image) -> Image:   
        transform_chain = transforms.Compose([
            transforms.RandomApply([aug], p) for aug, p in zip(self.transformations, self.probabilities)
        ])
        return transform_chain(img)
    
    def __repr__(self):
        return f"Augmentations(probabilities={self.probabilities}, transformations={self.transformations})"

