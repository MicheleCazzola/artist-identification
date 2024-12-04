from src.dataset import create_datasets
from src.dataloader import create_dataloaders
from src.transformations import get_transforms
import matplotlib.pyplot as plt
from torchvision.transforms import transforms
import sys



def check(*dataloaders):
    for dataloader in dataloaders:
        for inputs, labels in dataloader:
            images = [transforms.ToPILImage()(input) for input in inputs]
            for img, label in zip(images, labels):
                plt.figure()
                plt.imshow(img)
                plt.title(f"Label {label}")
                
    plt.show()

def main():
    
    ROOT = "./scripts/create_labels/images"
    TRAIN_SPLIT = 0.75
    
    if len(sys.argv) > 1:
        ROOT = sys.argv[1]
    
    transformations = get_transforms()
    trainset, validset, testset = create_datasets(ROOT, TRAIN_SPLIT, transformations)
    trainloader, validloader, testloader = create_dataloaders(trainset, validset, testset)

    check(trainloader, validloader, testloader)

if __name__ == '__main__':
    main()
else:
    main()