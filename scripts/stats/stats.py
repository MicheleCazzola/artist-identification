from sys import argv
from torch.utils.data import DataLoader
from torchvision import transforms
import torch
from src.dataset import ArtistDataset, create_datasets
from src.transformations import Transforms
from src.dataloader import create_dataloaders
from statistics import mean
import json

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
NUM_WORKERS = 2 if DEVICE == "cuda" else 0
DEFAULT_ROOT = "./scripts/stats/images/artist_dataset"
OUTFILE = "stats_all.json"

def load_data():
    
    if len(argv) > 1:
        root = argv[1]
        
        if DEVICE != "cuda":
            print("Warning: running on complete dataset - Please use GPU acceleration\nCPU may take a long time...")
    else:
        root = DEFAULT_ROOT
        print("Warning: not official run - Running on sample dataset")
        
        
    transformations = Transforms(type = "stats").get("tensor")
    dataset = create_datasets(root, merge_datasets=True, transforms=transformations)
    dataloader = create_dataloaders([dataset], batch_size=1, shuffle=False, drop_last=False, num_workers=NUM_WORKERS)
    
    return dataset, dataloader

@torch.no_grad()
def compute_stats(dataset: ArtistDataset, dataloader: DataLoader):
    
    assert isinstance(dataset, ArtistDataset), "Dataset must be of type ArtistDataset"
    
    keys = ["data_length", "categories_length", "avg_categories_size",
             "categories_size", "mean", "std", "dimensions",
             "min_height", "max_height", "min_width", "max_width"]
    
    num_authors = len(dataset.categories)
    
    category = lambda l: dataset.categories[l]
        
    labels_counts = {}
    dimensions = {}
    avg = torch.zeros((1,3)).to(DEVICE)
    std = torch.zeros((1,3)).to(DEVICE)
    data_len = 0
    tot_pixels = 0
    h_min, h_max = 10_000, 0
    w_min, w_max = 10_000, 0
    
    assert len(dataloader) > 0, "Dataloader must contain some data"
    
    tot_batches = len(dataloader)
    img_adjust = Transforms("stats").get("adjust")
    
    for (step, (inputs, labels)) in enumerate(dataloader):
        
        img_inputs = torch.stack([img_adjust(input) for input in inputs])
        img_inputs = img_inputs.to(DEVICE)
        labels = labels.to(DEVICE)
        
        _, _, h, w = inputs.shape
        h_min, h_max = min(h_min, h), max(h_max, h)
        w_min, w_max = min(w_min, w), max(w_max, w)
        dimensions[f"{int(h*w / 100_000)}00k"] = dimensions.get(f"{int(h*w / 100_000)}00k", 0) + 1
        
        print(f"Processing batch {step+1}/{tot_batches}")
        
        # Count number of elements for each class
        for label in labels:
            labels_counts[category(label.item())] = labels_counts.get(category(label.item()), 0) + 1
        
        b, _, h, w = img_inputs.shape
        
        data_len += b
        tot_pixels += b * h * w
        avg += torch.sum(img_inputs, dim=(0,2,3))
        std += torch.sum(img_inputs * img_inputs, dim=(0,2,3))
            
    avg /= tot_pixels
    std = torch.sqrt(std / tot_pixels - avg * avg)
    
    return dict(zip(
        keys, 
        [
            data_len, num_authors, mean(labels_counts.values()),
            labels_counts, avg.flatten().tolist(), std.flatten().tolist(),
            dimensions, h_min, h_max, w_min, w_max]
    ))

print(f"Device: {DEVICE}\nWorkers: {NUM_WORKERS}")

dataset, dataloader = load_data()
stats = compute_stats(dataset, dataloader)
with open(OUTFILE, "w") as fout:
    json.dump(stats, fout, indent=4)