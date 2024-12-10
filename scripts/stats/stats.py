from sys import argv
from torch.utils.data import DataLoader
import torch
from src.dataset import ArtistDataset, create_datasets
from src.transformations import get_transforms
from src.dataloader import create_dataloaders
from statistics import mean
import json

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
NUM_WORKERS = 2 if DEVICE == "cuda" else 0
DEFAULT_ROOT = "./scripts/stats/images/artist_dataset"
OUTFILE = "stats.json"

def load_data():
    
    if len(argv) > 1:
        root = argv[1]
        
        if DEVICE != "cuda":
            print("Warning: running on complete dataset - Please use GPU acceleration\nCPU may take a long time...")
    else:
        root = DEFAULT_ROOT
        print("Warning: not official run - Running on sample dataset")
        
    transformations = get_transforms()
    dataset = create_datasets(root, merge_datasets=True, transforms=transformations)
    dataloader = create_dataloaders([dataset], shuffle=False, drop_last=False, num_workers=NUM_WORKERS)
    
    return dataset, dataloader

def compute_stats(dataset: ArtistDataset, dataloader: DataLoader):
    
    assert isinstance(dataset, ArtistDataset), "Dataset must be of type ArtistDataset"
    
    keys = ["data_length", "categories_length", "avg_categories_size", "categories_size", "mean", "devstd"]
    
    num_authors = len(dataset.categories)
    
    category = lambda l: dataset.categories[l]
        
    labels_counts = {}
    avg = torch.zeros((1,3)).to(DEVICE)
    std = torch.zeros((1,3)).to(DEVICE)
    data_len = 0
    tot_pixels = 0
    
    assert len(dataloader) > 0, "Dataloader must contain some data"
    
    tot_batches = len(dataloader)
    
    for (step, (inputs, labels)) in enumerate(dataloader):
        
        inputs = inputs.to(DEVICE)
        labels = labels.to(DEVICE)
        
        print(f"Processing batch {step+1}/{tot_batches}")
        
        # Count number of elements for each class
        for label in labels:
            labels_counts[category(label.item())] = labels_counts.get(category(label.item()), 0) + 1
        
        b, _, h, w = inputs.shape
        
        data_len += b
        tot_pixels += b * h * w
        avg += torch.sum(inputs, dim=(0,2,3))
        std += torch.sum(inputs * inputs, dim=(0,2,3))
            
    avg /= tot_pixels
    std = torch.sqrt(std / tot_pixels - avg * avg)
    
    return dict(zip(keys, [data_len, num_authors, mean(labels_counts.values()), labels_counts, avg.tolist(), std.tolist()]))

print(f"Device: {DEVICE}\nWorkers: {NUM_WORKERS}")

dataset, dataloader = load_data()
stats = compute_stats(dataset, dataloader)
with open(OUTFILE, "w") as fout:
    json.dump(stats, fout, indent=4)