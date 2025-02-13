import json
import logging
from torch.utils.data import DataLoader
import torch

from src.config.config import Config
from src.dataset.dataloader import create_dataloaders
from src.dataset.dataset import ArtistDataset
from src.transformations.transformations import Transforms

@torch.no_grad()
def compute_stats(dataloader: DataLoader, device: torch.device, out_file: str) -> dict:
    
    avg = torch.zeros((1,3)).to(device)
    std = torch.zeros((1,3)).to(device)
    data_len = 0
    tot_pixels = 0
    
    assert len(dataloader) > 0, "Dataloader must contain some data"
    
    tot_batches = len(dataloader)
    
    for (step, (inputs, labels)) in enumerate(dataloader):
        
        inputs = inputs.to(device)
        labels = labels.to(device)
        
        logging.info(f"Processing batch {step+1}/{tot_batches}")
        
        b, _, h, w = inputs.shape
        
        data_len += b
        tot_pixels += b * h * w
        avg += torch.sum(inputs, dim=(0,2,3))
        std += torch.sum(inputs * inputs, dim=(0,2,3))
            
    avg /= tot_pixels
    std = torch.sqrt(std / tot_pixels - avg * avg)
    
    result = {
        "mean": avg.flatten().tolist(),
        "std": std.flatten().tolist()
    }
    
    json.dump(result, open(out_file, "w"), indent=4)

logging.basicConfig(level=logging.INFO)

cfg = Config.create("colab")
transformations = Transforms("model", data_config=cfg.data).get("train_base")
trainset_stats = ArtistDataset(cfg.path.root, "train", transform=transformations)
trainloader_stats = create_dataloaders(
    [trainset_stats],
    cfg.data.batch_size_stats,
    shuffle=False,
    drop_last=False,
    num_workers=cfg.env.num_workers
)
print(trainloader_stats.dataset.transforms)
compute_stats(trainloader_stats, cfg.env.device, cfg.path.norm_stats_file)