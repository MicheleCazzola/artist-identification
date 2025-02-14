import torch
from torch.utils.data import DataLoader, Subset
from src.dataset.dataset import ArtistDataset

def create_dataloaders(
    datasets: list[ArtistDataset | Subset],
    batch_size: int,
    shuffle: bool = True,
    drop_last: bool = True,
    num_workers: int = 0,
    worker_init_fn: callable = None,
    generator: torch.Generator = None
) -> tuple[DataLoader, DataLoader, DataLoader] | tuple[DataLoader, DataLoader] | DataLoader:
    
    """
    Create dataloaders for the given datasets
    
    datasets: list[ArtistDataset | Subset]
        List of datasets to create the dataloaders from
    batch_size: int
        Batch size for the dataloaders
    shuffle: bool
        Whether to shuffle the data
    drop_last: bool
        Whether to drop the last incomplete batch
    num_workers: int
        Number of workers for the dataloaders
    worker_init_fn: callable
        Worker initialization function
    generator: torch.Generator
        Random generator for the dataloaders
        
    Returns:
        - A single DataLoader if a single dataset is passed
        - A tuple of DataLoaders if multiple datasets are passed
    """
    
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
    # (here called trainloader, but it is a single dataloader)
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