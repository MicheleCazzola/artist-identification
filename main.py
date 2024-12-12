from src.constants import Constants, Env
from src.dataset import create_datasets
from src.dataloader import create_dataloaders
from src.transformations import Transforms
from src.train import train, train_setup
from src.evaluate import evaluate
from src.network import MultibranchNetwork
from src.display import plot_metric
import matplotlib.pyplot as plt
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
    
    constants = Env("local").constants
    root = sys.argv[1] if len(sys.argv) > 1 else constants.default_root
    
    print(constants)
        
    transformations = Transforms(constants=constants).get()
    trainset, validset, testset = create_datasets(
        root, 
        train_split_size=constants.train_split_size, 
        transforms=transformations
    )
    trainloader, validloader, testloader = create_dataloaders(
        [trainset, validset, testset],
        batch_size=constants.batch_size,
        drop_last=True,
        num_workers=constants.num_workers
    )

    model = MultibranchNetwork(out_classes=constants.num_classes)
    criterion, optimizer, scheduler = train_setup(model)
    
    train_losses, train_acc, val_losses, val_acc = train(model, trainloader, validloader, criterion, optimizer, scheduler,
          constants.num_epochs, constants.device, constants.log_frequency)
    
    test_acc, test_loss = evaluate(model, testloader, criterion, constants.device)
    
    plot_metric([train_losses, val_losses], ["train loss", "validation loss"], name="Loss")
    plot_metric([train_acc, val_acc], ["train accuracy", "validation accuracy"], name="Accuracy")
    
    print(f"Test: accuracy {100 * test_acc:.2f}%, loss: {test_loss}")
    
    plt.show()

main()