import os
import pandas as pd
import torch
from torchvision.datasets import VisionDataset
from torchvision.transforms import transforms
from torch.utils.data import Subset
from sklearn.model_selection import train_test_split
from PIL import Image

class ArtistDataset(VisionDataset):
    def __init__(
        self,
        root: str,
        split: str = "train",
        transform: transforms = None,
        target_transform: transforms = None
    ):
        super(ArtistDataset, self).__init__(root, transform=transform, target_transform=target_transform)
                
        self.split = split

        images_paths, labels = [], []
        self.categories = os.listdir(self.root)

        split_file = f"{root}/{split}.txt"
        for path in open(split_file):
            path = path.replace("\n", "")
            category = path.split("/")[0]
            image_path = self.root + "/" + path
            images_paths.append(image_path)
            labels.append(self.categories.index(category))

        self.data = pd.DataFrame(zip(images_paths, labels), columns = ["image_path", "label"])
    
    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index) -> tuple[torch.Tensor, int]:
        img_path = self.data["image_path"].iloc[index]
        img, label = ArtistDataset.pil_loader(img_path), self.data["label"].iloc[index]
        
        if self.transform is not None:
            img = self.transform(img)
            
        return img, label
    
    @staticmethod
    def pil_loader(path: str) -> Image:
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')


def create_datasets(root: str, train_split: float, datasets_transforms: dict) -> tuple[Subset, Subset, ArtistDataset]:
    train_transforms, eval_transforms = map(datasets_transforms.get, ["train", "test"])
    trainset = ArtistDataset(root, "train", transform=train_transforms)
    testset = ArtistDataset(root, "test", transform=eval_transforms)
    
    trainset, validset = split_dataset(trainset, train_split)
    
    return trainset, validset, testset


def split_dataset(dataset: ArtistDataset, train_size: float, random_state: int = 42, shuffle: bool = True) -> tuple[Subset, Subset]:
    indexes = range(0, len(dataset))
    train_indexes, val_indexes = train_test_split(indexes, train_size=train_size, random_state=random_state, shuffle=shuffle)

    trainset = Subset(dataset, train_indexes)
    validset = Subset(dataset, val_indexes)
    
    return trainset, validset