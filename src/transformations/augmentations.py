import torch
from torchvision.transforms import transforms
from sklearn.decomposition import PCA
import numpy as np
from PIL import Image


class LightingNoise:
    """
    Add PCA-based lighting noise to the image.
    
    Attributes:
    -----------
    alpha: float
        Scaling factor for the noise
    dim: int
        Number of features in the image
    """
    
    def __init__(self, alpha: float = 0.1, dim: int = 3):
        self.alpha = alpha
        self.dim = dim
        
    def __call__(self, img: Image.Image) -> Image.Image:
        img: torch.Tensor = transforms.ToTensor()(img)
        samples = img.view(self.dim, -1).numpy().T  # img of shape 3 x (H*W) -> (H*W) samples of 3 features
        
        # Apply PCA to the samples
        pca = PCA()
        pca.fit(samples)
        
        # Generate the noise using PCA eigenvectors and eigenvalues
        noise = pca.components_.T @ (self.alpha * np.random.randn(self.dim) * pca.explained_variance_)  # eigenvectors * (rnd[i] * eigenvalues[i])
        
        # Add the noise to the image
        img += torch.tensor(noise).view(self.dim, 1, 1)
        
        return transforms.ToPILImage()(img.clamp(0, 1))
    
    def __repr__(self):
        return f"LightingNoise(alpha={self.alpha}, dim={self.dim})"
    
    
class Augmentations:
    """
    Class to handle the augmentations for the input images.
    Each augmentation is applied independently with a certain probability and its flag.
    
    Attributes:
    -----------
    probabilities: list[float] | tuple[float]
        List of probabilities for each transformation
    mask: list[bool] | tuple[bool]
        List of flags to apply the transformations
    jitter_brightness: float
        Brightness for color jitter
    jitter_contrast: float
        Contrast for color jitter
    jitter_saturation: float
        Saturation for color jitter
    blur_size: tuple[int]
        Size of the Gaussian kernel for the blur
    blur_sigma: tuple[float]
        Standard deviation of the Gaussian kernel for the blur
    crop_scale: tuple[float]
        Scale of the crop for the geometric transformation
    crop_ratio: tuple[float]
        Aspect ratio of the crop for the geometric transformation
    """
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
        # Change color brightness, contrast and saturation
        color_jitter = transforms.ColorJitter(brightness=jitter_brightness, contrast=jitter_contrast, saturation=jitter_saturation)
        
        # PCA-based lighting noise, AlexNet style
        lighting_noise = LightingNoise()
        
        # Apply Gaussian kernel to blur the image
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