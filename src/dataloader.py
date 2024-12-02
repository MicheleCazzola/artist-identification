from torch.utils.data import DataLoader

BATCH_SIZE = 2
WORKERS = 0

def create_dataloaders(trainset, validset, testset):
    trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True, drop_last=True, num_workers=WORKERS)
    validloader = DataLoader(validset, batch_size=BATCH_SIZE, shuffle=False, num_workers=WORKERS)
    testloader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False, num_workers=WORKERS)
    
    return trainloader, validloader, testloader