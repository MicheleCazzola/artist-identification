from src.constants import Constants
from src.dataset import create_datasets
from src.dataloader import create_dataloaders
from src.transformations import get_transforms
import matplotlib.pyplot as plt
from torchvision.transforms import transforms
import sys


def check(*dataloaders):
    for dataloader in dataloaders:
        
        print(dataloader)
        tot_len = len(dataloader)
        for (step, (inputs, labels)) in enumerate(dataloader):
            
            inputs = inputs.to(Constants.Env.DEVICE)
            labels = labels.to(Constants.Env.DEVICE)
            
            print(f"Batch {step+1}/{tot_len}")
            
            print(type(inputs), inputs.shape, labels.shape)
            
            
            # images = [transforms.ToPILImage()(input) for input in inputs]
            # for img, label in zip(images, labels):
            #     plt.figure()
            #     plt.imshow(img)
            #     plt.title(f"Label {label}")
        print()
    #plt.show()


def main():
    
    root = sys.argv[1] if len(sys.argv) > 1 else Constants.Paths.DEFAULT_ROOT
        
    transformations = get_transforms()
    trainset, validset, testset = create_datasets(root, Constants.Train.TRAIN_SPLIT_SIZE, transforms=transformations)
    trainloader, validloader, testloader = create_dataloaders([trainset, validset, testset], drop_last=False)

    check(trainloader, validloader, testloader)

if __name__ == '__main__':
    main()
else:
    main()