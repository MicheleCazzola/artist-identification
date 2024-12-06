from sys import argv
from torch.utils.data import DataLoader
import torch
from src.dataset import ArtistDataset, create_datasets
from src.transformations import get_transforms
from src.dataloader import create_dataloaders

DEFAULT_ROOT = "./scripts/stats/images/artist_dataset"
root = argv[1] if len(argv) else DEFAULT_ROOT


transformations = get_transforms()
dataset = create_datasets(root, merge_datasets=True, transforms=transformations)
dataloader = create_dataloaders([dataset], shuffle=False, drop_last=False, num_workers=0)

def compute_stats(dataset: ArtistDataset, dataloader: DataLoader):
    
    assert isinstance(dataset, ArtistDataset), "Dataset must be of type ArtistDataset"
    
    print(list(dataset.categories))
    num_authors = len(dataset.categories)
        
    labels_dict = {}
    avg = torch.zeros((1,3))
    std = torch.zeros((1,3))
    dim = 0
    tot_pixels = 0
    
    assert len(dataloader) > 0, "Dataloader must contain some data"
    
    for inputs, labels in dataloader:
        
        # Count number of elements for each class
        for label in labels:
            labels_dict[label.item()] = labels_dict.get(label.item(), 0) + 1
        
        b, _, h, w = inputs.shape
        
        dim += b
        tot_pixels += b * h * w
        avg += torch.sum(inputs, dim=(0,2,3))
        std += torch.sum(inputs * inputs, dim=(0,2,3))
            
    avg /= tot_pixels
    std = torch.sqrt(std / tot_pixels - avg * avg)
    
    return num_authors, labels_dict, avg, std, dim

num_authors, labels, avg, std, dim = compute_stats(dataset, dataloader)
print(num_authors, labels, avg, std, dim)