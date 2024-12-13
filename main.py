from src.constants import Constants, Env
from src.dataset import create_datasets
from src.dataloader import create_dataloaders
from src.transformations import Transforms
from src.train import Trainer
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
    
    if len(sys.argv) > 1:
        constants = Env("colab").constants
        root = sys.argv[1]
    else:
        constants = Env("local").constants
        root = constants.default_root
    
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
    
    trainer = Trainer(model, trainloader, validloader, testloader, constants.device, constants.log_frequency)
    trainer.set_params(
        constants.num_epochs,
        constants.lr,
        constants.momentum,
        constants.scheduler_step_size,
        constants.scheduler_gamma,
        constants.weight_decay
    )
    trainer.build_trainer(
        constants.criterion,
        constants.optimizer,
        constants.scheduler
    )
    train_losses, train_acc, val_losses, val_acc = trainer.train()
    test_loss, test_acc = trainer.test()
    
    loss_fig = plot_metric([train_losses, val_losses], ["training loss", "validation loss"], name="Loss")
    acc_fig = plot_metric([train_acc, val_acc], ["training accuracy", "validation accuracy"], name="Accuracy")
    
    loss_fig.savefig(f"{constants.results_plot_path}/loss.png")
    acc_fig.savefig(f"{constants.results_plot_path}/accuracy.png")
    
    print(f"Test: accuracy {100 * test_acc:.2f}%, loss: {test_loss}")

main()