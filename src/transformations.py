from src.constants import Constants
from torchvision.transforms import transforms
import json

mean, devstd = map(json.load(open(Constants.Paths.STATS_FILE, mode="r", encoding="utf-8")).get, ["mean", "devstd"])

resizer = transforms.Resize(Constants.Img.RESIZE_DIM)
cropper = transforms.CenterCrop(Constants.Img.CROP_DIM)
to_tensor = transforms.ToTensor()
to_image = transforms.ToPILImage()
normalizer = transforms.Normalize(mean, devstd)

sample_aug = transforms.RandomHorizontalFlip(p = 1)
random_apply = transforms.RandomApply

aug_transform = sample_aug

train_transforms = transforms.Compose([
    resizer,
    cropper,
    to_tensor
])

eval_transforms = transforms.Compose([
    resizer,
    cropper,
    to_tensor
])

aug_pipeline = transforms.Compose([
    to_image,
    random_apply([aug_transform], p=Constants.Img.AUG_PROB),
    to_tensor,
    normalizer
])

def get_transforms():
    return {
        "train": train_transforms,
        "test": eval_transforms,
        "aug": aug_pipeline
    }