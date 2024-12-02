import random
import os
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from torchvision.datasets import VisionDataset
from torchvision.transforms import transforms
from torch.utils.data import DataLoader, Subset
from sklearn.model_selection import train_test_split
from PIL import Image

class ArtistDataset(VisionDataset):
    def __init__(self, root, split: str = "train", transform = None, target_transform = None):
        super(ArtistDataset, self).__init__(root, transform=transform, target_transform=target_transform)
                
        self.split = split

        images_paths = []
        labels = []

        self.categories = os.listdir(self.root)

        split_file = f"{root}/{split}.txt"
        for path in open(split_file):
            path = path.replace("\n", "")
            category = path.split("/")[0]
            image_path = self.root + "/" + path
            images_paths.append(image_path)
            labels.append(self.categories.index(category))

        self.data = pd.DataFrame(zip(images_paths, labels), columns = ["image_path", "label"])
    
    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img_path = self.data["image_path"].iloc[index]
        img, label = self.pil_loader(img_path), self.data["label"].iloc[index]
        
        if self.transform is not None:
            img = self.transform(img)
            
        return img, label
    
    def pil_loader(self, path):
        with open(path, 'rb') as f:
            img = Image.open(f)
            return img.convert('RGB')


ROOT = "./scripts/images"
BATCH_SIZE = 2
WORKERS = 0
train_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

eval_transforms = transforms.Compose([
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.ToTensor()
])

# Datasets
trainset = ArtistDataset(ROOT, "train", transform=train_transforms)
testset = ArtistDataset(ROOT, "test", transform=eval_transforms)

# Train/Validation split
indexes = range(0, len(trainset))
train_indexes, val_indexes = train_test_split(indexes, train_size=0.75, random_state=42, shuffle=True)

trainset = Subset(trainset, train_indexes)
validset = Subset(trainset, val_indexes)

# Dataloaders
trainloader = DataLoader(trainset, batch_size=BATCH_SIZE, shuffle=True, drop_last=True, num_workers=WORKERS)
validloader = DataLoader(validset, batch_size=BATCH_SIZE, shuffle=False, num_workers=WORKERS)
testloader = DataLoader(testset, batch_size=BATCH_SIZE, shuffle=False, num_workers=WORKERS)

# Check
def check(dataloader):
    for inputs, labels in dataloader:
        images = [transforms.ToPILImage()(input) for input in inputs]
        for img, label in zip(images, labels):
            plt.figure()
            plt.imshow(img)
            plt.title(f"Label {label}")

check(trainloader)
# check(validloader)
# check(testloader)

plt.show()