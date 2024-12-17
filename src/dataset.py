import os
import logging
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
        
        assert split is None or split in ["train", "test"], "Split must be either training or test, or include all the dataset"
                
        self.split = split
        self.categories = os.listdir(self.root)

        images_paths, labels = [], []
        split_file = lambda s: f"{root}/../{s}.txt"
        
        if split is None:
            images_paths_train, labels_train = self.__get_data_split(split_file("train"))
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
        img, label = ArtistDataset.__pil_loader(img_path), self.data["label"].iloc[index]
        
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
    
    @staticmethod
    def __pil_loader(path: str) -> Image:
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')


def create_datasets(
    root: str,
    train_split_size: float = None,
    merge_datasets: bool = False,
    transforms: dict | Compose = None,
    validation: bool = True,
    reduction_factor: float = None
) -> tuple[Subset, Subset, ArtistDataset] | tuple[ArtistDataset, ArtistDataset] | ArtistDataset:
    
    assert not merge_datasets and not validation and (train_split_size is None) or \
        not merge_datasets and validation and not (train_split_size is None) or \
        merge_datasets and validation and (train_split_size is None), \
        f"Something went wrong in parameter definition " + \
        f"(merge_datasets:{merge_datasets}, validation_enabled:{validation}), train_split_size: {train_split_size:.2f}"
        
    assert train_split_size is None or 0 <= train_split_size <= 1, "Train split size must be a fraction"
    assert reduction_factor is None or 0 <= reduction_factor <= 1, "Reduce factor must be a fraction"
    
    # Dataset is loaded into training and test set
    if not merge_datasets:
        
        if transforms:
            train_transforms, eval_transforms = map(transforms.get, ["train", "eval"])
        else:
            train_transforms, eval_transforms = None, None
        
        trainset = ArtistDataset(root, "train", transform=train_transforms)
        testset = ArtistDataset(root, "test", transform=eval_transforms)
 
        if reduction_factor is not None:
            trainset = reduce_dataset(trainset, reduction_factor)
            testset = reduce_dataset(testset, reduction_factor)
            
        # A validation split is generated out of the train set
        if validation:
            trainset, validset = split_dataset(trainset, train_split_size)
            return trainset, validset, testset
        
        return trainset, testset
    
    # Load all the dataset in one single object: useful for statistics
    # Applied only basic evaluation transformations
    dataset = ArtistDataset(root, transform=transforms)
    
    if reduction_factor is not None:
        dataset = reduce_dataset(dataset)
        
    return dataset


def split_dataset(
    dataset: ArtistDataset | Subset, 
    train_size: float, 
    random_state: int = 42, 
    shuffle: bool = True
) -> tuple[Subset, Subset]:

    indexes = range(0, len(dataset))
    train_indexes, val_indexes = train_test_split(
        indexes,
        train_size=train_size,
        random_state=random_state, 
        shuffle=shuffle,
        stratify=dataset.get_labels() if not isinstance(dataset, Subset) else None
    )

    trainset = Subset(dataset, train_indexes)
    validset = Subset(dataset, val_indexes)
    
    return trainset, validset


def reduce_dataset(
    dataset: ArtistDataset,
    reduction_factor: float
) -> Subset:

    reduced_dataset, _ = split_dataset(
        dataset,
        reduction_factor
    )

    return reduced_dataset