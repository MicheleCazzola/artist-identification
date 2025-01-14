import torch
from torch.utils.data import DataLoader, Subset
from .dataset import ArtistDataset

def create_dataloaders(
    datasets: list[ArtistDataset | Subset],
    batch_size: int,
    shuffle: bool = True,
    drop_last: bool = True,
    num_workers: int = 0,
    worker_init_fn: callable = None,
    generator: torch.Generator = None
) -> tuple[DataLoader, DataLoader, DataLoader] | tuple[DataLoader, DataLoader] | DataLoader:
    
    assert batch_size > 0, f"Batch size must be strictly positive, found {batch_size}"
    
    assert 1 <= len(datasets) <= 3, f"Invalid number of datasets: found {len(datasets)}"
    
    trainloader = DataLoader(
        datasets[0], 
        batch_size=batch_size, 
        shuffle=shuffle, 
        drop_last=drop_last,
        num_workers=num_workers,
        worker_init_fn=worker_init_fn,
        generator=generator
    )
    
    # A single dataset is passed, so single dataloader
    # (here called trainloader, but it is a single dataloader for the whole dataset)
    if len(datasets) == 1:
        return trainloader
    
    dataloaders = [trainloader]
    for dataset in datasets[1:]:
        
        # Data from validation/test splits should not be shuffled or dropped 
        dataloader = DataLoader(
            dataset,
            batch_size=batch_size,
            shuffle=False,
            drop_last=False,
            num_workers=num_workers,
            worker_init_fn=worker_init_fn,
            generator=generator
        )
        
        dataloaders.append(dataloader)
    
    return tuple(dataloaders)