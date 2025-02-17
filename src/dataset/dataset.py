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
        """
        Class for the Artist dataset
        
        Parameters:
        -----------
        root: str
            Root directory of the dataset
        split: str
            Split of the dataset, either "train", "val", "test" or None (all the dataset)
        transform: transforms
            Transform to apply to the images
        target_transform: transforms
            Transform to apply to the labels (not used here)
        
        Attributes:
        -----------
        split: str
            Split of the dataset
        categories: list[str]
            List of categories in the dataset, sorted alphabetically
        data: pd.DataFrame
            Dataframe containing the images paths and labels
        labels: torch.Tensor
            Tensor containing the labels of the dataset (for low-memory lookup)
        
        Methods:
        --------
        __len__() -> int
            Return the length of the dataset
        __getitem__(index: int) -> tuple[torch.Tensor, int]
            Return the image and the label at the given index
        __build_labels(file: str) -> torch.Tensor
            Build the labels from the file
        __get_data_split(split_file: str) -> tuple[list[str], list[int]]
            Get the data split from the file
        get_labels() -> torch.Tensor
            Return the labels of the dataset
        get_histogram(indices = None) -> torch.Tensor
            Return the histogram of the dataset
        create(...) -> ...
            Create the dataset
        """
        
        super(ArtistDataset, self).__init__(root, transform=transform, target_transform=target_transform)
        
        assert split is None or split in ["train", "val", "test"], "Split must be either training, validation or test, or include all the dataset"
                
        self.split = split

        images_paths, labels = [], []
        split_file = lambda s: f"{root}/../{s}.txt"
        
        split_name = "train" if split is None else split
        self.categories = self.__build_labels(split_file(split_name))
        
        # Retrieve images and labels from split files
        if split is None:
            images_paths_train, labels_train = self.__get_data_split(split_file("train"))
            images_paths_val, labels_val = self.__get_data_split(split_file("val"))
            images_paths_test, labels_test = self.__get_data_split(split_file("test"))
            images_paths, labels = images_paths_train + images_paths_val + images_paths_test, labels_train + labels_val + labels_test
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
            
        if self.target_transform is not None:
            label = self.target_transform(label)
            
        return img, label
    
    def __build_labels(self, file: str) -> torch.Tensor:
        """
        Gets the labels from the file
        
        file: str
            File containing the labels
            
        Returns: torch.Tensor
            Tensor containing the labels
        """
        all_labels = [line.split("/")[-2] for line in open(file, "r")]
        return sorted(list(set(all_labels)))
    
    def __get_data_split(self, split_file: str) -> tuple[list[str], list[int]]:
        """
        Gets the data split from the file.
        
        split_file: str
            File containing the split images
        
        Returns: tuple[list[str], list[int]]
            List of images paths and labels
        """
        
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
        """
        Gets the histogram of the dataset
        
        indices: list[int] | torch.Tensor | None
            Indices to consider for the histogram (useful for Subset)
        
        Returns: torch.Tensor
            Histogram of the dataset
        """
        indices = range(0, len(self)) if indices is None else indices
        indices = torch.tensor(indices) if not isinstance(indices, torch.Tensor) else indices
        return torch.tensor(pd.Series(self.labels[indices]).value_counts(normalize=True, sort=False).values, dtype=torch.float32)
        
    @staticmethod
    def create(
        root: str,
        merge_datasets: bool = False,
        augment: bool = False,
        transforms: dict | Compose = None,
        reduction_factor: float = None
    ) -> Union[tuple[Union[Subset, "ArtistDataset"], ...], Subset, "ArtistDataset"]:
        
        """
        Create the dataset
        
        root: str
            Root directory of the dataset
        merge_datasets: bool
            If True, the dataset is loaded in one single object
        augment: bool
            If True, the dataset is augmented
        transforms: dict | Compose
            Transforms to apply to the dataset
        reduction_factor: float
            Reduction factor for the dataset (downsampling)
        
        Returns: Union[tuple[Union[Subset, "ArtistDataset"], ...], Subset, "ArtistDataset"]
            Dataset(s) created
        """
        
        assert reduction_factor is None or 0 < reduction_factor <= 1, "Reduce factor must be a fraction"
        
        # Dataset is loaded into training and test set
        if not merge_datasets:
            
            if transforms:
                train_transforms, eval_transforms = map(transforms.get, ["train_norm" if not augment else "train_aug", "eval"])
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
        
        # Load all the dataset in one single object: useful for some statistics
        dataset = ArtistDataset(root, transform=transforms)
        
        if reduction_factor is not None and reduction_factor < 1:
            dataset = ArtistDataset._reduce(dataset, reduction_factor)
            
        return dataset

    @staticmethod
    def _reduce(
        dataset: "ArtistDataset",
        reduction_factor: float, 
        random_state: int = 42, 
        shuffle: bool = True
    ) -> Subset:
        """
        Reduce the dataset
        
        dataset: "ArtistDataset"
            Dataset to reduce
        reduction_factor: float
            Reduction factor for the dataset (downsampling)
            
        Returns: Subset
            Reduced dataset
        """

        indexes = range(0, len(dataset))
        stratify = dataset.get_labels() if isinstance(dataset, ArtistDataset) else None
        train_indexes, _ = train_test_split(
            indexes,
            train_size=reduction_factor,
            random_state=random_state, 
            shuffle=shuffle,
            stratify=stratify
        )

        trainset = Subset(dataset, train_indexes)
        
        return trainset
    
    @staticmethod
    def pil_loader(path: str) -> Image:
        """
        Load an image using PIL: convert to RGB directly
        """
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')