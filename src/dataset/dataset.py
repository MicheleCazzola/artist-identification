import os
from typing import Union
import pandas as pd
import torch
from torchvision.datasets import VisionDataset
from torchvision.transforms import transforms, Compose
from torch.utils.data import Subset
from sklearn.model_selection import train_test_split
from PIL import Image


class ArtistDataset(VisionDataset):
    def __init__(
        self,
        root: str,
        split: str = None,
        transform: transforms = None,
        target_transform: transforms = None
    ):
        super(ArtistDataset, self).__init__(root, transform=transform, target_transform=target_transform)
        
        assert split is None or split in ["train", "val", "test"], "Split must be either training, validation or test, or include all the dataset"
                
        self.split = split
        self.categories = os.listdir(self.root)

        images_paths, labels = [], []
        split_file = lambda s: f"{root}/../{s}.txt"
        
        if split is None:
            images_paths_train, labels_train = self.__get_data_split(split_file("train"))
            images_paths_val, labels_val = self.__get_data_split(split_file("val"))
            images_paths_test, labels_test = self.__get_data_split(split_file("test"))
            images_paths, labels = images_paths_train + images_paths_test, labels_train + labels_test
        else:
            images_paths, labels = self.__get_data_split(split_file(split))

        labels = torch.tensor(labels, dtype=torch.uint8)
        self.data = pd.DataFrame(zip(images_paths, labels), columns = ["image_path", "label"])
        
        # For stratification, avoiding to load all the dataset in memory
        self.labels = labels
    
    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index) -> tuple[torch.Tensor, int]:
        img_path = self.data["image_path"].iloc[index]
        img, label = ArtistDataset.pil_loader(img_path), self.data["label"].iloc[index]
        
        if self.transform is not None:
            img = self.transform(img)
            
        return img, label
    
    def __get_data_split(self, split_file: str) -> tuple[list[str], list[int]]:
        images_paths, labels = [], []
        for path in open(split_file):
            path = path.replace("\n", "")
            category = path.split("/")[0]
            image_path = self.root + "/" + path
            images_paths.append(image_path)
            labels.append(self.categories.index(category))
        
        return images_paths, labels
    
    def get_labels(self) -> torch.Tensor:
        return self.labels
    
    def get_histogram(self, indices = None) -> torch.Tensor:
        indices = range(0, len(self)) if indices is None else indices
        indices = torch.tensor(indices) if not isinstance(indices, torch.Tensor) else indices
        return torch.tensor(pd.Series(self.labels[indices]).value_counts(normalize=True, sort=False).values, dtype=torch.float32)
        
    @staticmethod
    def create(
        root: str,
        train_split_size: float = None,
        merge_datasets: bool = False,
        transforms: dict | Compose = None,
        reduction_factor: float = None
    ) -> Union[tuple[Union[Subset, "ArtistDataset"], ...], Subset, "ArtistDataset"]:
        
        assert not merge_datasets and not (train_split_size is None) or \
            merge_datasets and (train_split_size is None), \
            f"Something went wrong in parameter definition " + \
            f"(merge_datasets:{merge_datasets}, train_split_size: {train_split_size:.2f}"
            
        assert train_split_size is None or 0 <= train_split_size <= 1, "Train split size must be a fraction"
        assert reduction_factor is None or 0 < reduction_factor <= 1, "Reduce factor must be a fraction"
        
        # Dataset is loaded into training and test set
        if not merge_datasets:
            
            if transforms:
                train_transforms, eval_transforms = map(transforms.get, ["train", "eval"])
            else:
                train_transforms, eval_transforms = None, None
            
            trainset = ArtistDataset(root, "train", transform=train_transforms)
            validset = ArtistDataset(root, "val", transform=eval_transforms)
            testset = ArtistDataset(root, "test", transform=eval_transforms)
    
            if reduction_factor is not None and reduction_factor < 1:
                trainset = ArtistDataset._reduce(trainset, reduction_factor)
                validset = ArtistDataset._reduce(validset, reduction_factor)
                testset = ArtistDataset._reduce(testset, reduction_factor)
                
            return trainset, validset, testset
        
        # Load all the dataset in one single object: useful for statistics
        # Applied only basic evaluation transformations
        dataset = ArtistDataset(root, transform=transforms)
        
        if reduction_factor is not None and reduction_factor < 1:
            dataset = ArtistDataset._reduce(dataset, reduction_factor)
            
        return dataset

    @staticmethod
    def _split(
        dataset: Union["ArtistDataset", Subset],
        train_size: float, 
        random_state: int = 42, 
        shuffle: bool = True
    ) -> tuple[Subset, Subset]:

        indexes = range(0, len(dataset))
        stratify = dataset.get_labels() if isinstance(dataset, ArtistDataset) else None
        train_indexes, val_indexes = train_test_split(
            indexes,
            train_size=train_size,
            random_state=random_state, 
            shuffle=shuffle,
            stratify=stratify
        )

        trainset = Subset(dataset, train_indexes)
        validset = Subset(dataset, val_indexes)
        
        return trainset, validset

    @staticmethod
    def _reduce(dataset: Union["ArtistDataset", Subset], reduction_factor: float) -> Subset:

        reduced_dataset, _ = ArtistDataset._split(dataset, reduction_factor)

        return reduced_dataset
    
    @staticmethod
    def pil_loader(path: str) -> Image:
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')
        

class UnlabeledArtistDataset(VisionDataset):
    def __init__(self, root: str, transform: transforms = None):
        super(UnlabeledArtistDataset, self).__init__(root, transform=transform)
        
        self.images_paths = [f"{root}/{image}" for image in os.listdir(root)]
        
    def __len__(self) -> int:
        return len(self.images_paths)
    
    def __getitem__(self, index) -> torch.Tensor:
        img_path = self.images_paths[index]
        img = ArtistDataset.pil_loader(img_path)
        
        if self.transform is not None:
            img = self.transform(img)
            
        return img, img_path