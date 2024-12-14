import logging
from src.config import Config
from src.dataset import create_datasets
from src.dataloader import create_dataloaders
from src.transformations import Transforms
from src.train import Trainer
from src.network import MultibranchNetwork
import sys


# def check(*dataloaders):
#     for dataloader in dataloaders:
        
#         print(dataloader)
#         tot_len = len(dataloader)
#         for (step, (inputs, labels)) in enumerate(dataloader):
            
#             inputs = inputs.to(Constants.Env.DEVICE)
#             labels = labels.to(Constants.Env.DEVICE)
            
#             print(f"Batch {step+1}/{tot_len}")
            
#             print(type(inputs), inputs.shape, labels.shape)
            
            
#             # images = [transforms.ToPILImage()(input) for input in inputs]
#             # for img, label in zip(images, labels):
#             #     plt.figure()
#             #     plt.imshow(img)
#             #     plt.title(f"Label {label}")
#         print()
#     #plt.show()


def main():
    
    logging.basicConfig(level=logging.INFO)
    
    if len(sys.argv) > 1:
        cfg = Config.create("colab")
        root = sys.argv[1]
    else:
        cfg = Config.create("local")
        root = cfg.default_root
    
    logging.info(cfg.__dict__)
        
    transformations = Transforms(config=cfg).get()
    trainset, validset, testset = create_datasets(
        root, 
        train_split_size=cfg.train_split_size, 
        transforms=transformations
    )
    trainloader, validloader, testloader = create_dataloaders(
        [trainset, validset, testset],
        cfg.batch_size,
        drop_last=True,
        num_workers=cfg.num_workers
    )

    model = MultibranchNetwork(out_classes=cfg.num_classes)
    
    logging.info(f"Training setup...")
    trainer = Trainer(model, trainloader, validloader, testloader, transformations["aug"], cfg.device, cfg.log_frequency)
    trainer.set_params(
        cfg.num_epochs,
        cfg.lr,
        cfg.momentum,
        cfg.scheduler_step_size,
        cfg.scheduler_gamma,
        cfg.weight_decay,
        cfg.top_k
    )
    trainer.build_trainer(
        cfg.criterion,
        cfg.optimizer,
        cfg.scheduler
    )
    
    logging.info(f"Training...")
    trainer.train()
    
    logging.info(f"Inference...")
    trainer.test()
    
    logging.info(f"Saving results...")
    trainer.plot_results("Loss", cfg.results_plot_path)
    trainer.plot_results("Accuracy", cfg.results_plot_path)
    
    trainer.save_results(cfg, cfg.results_file_path)
    
    logging.info(f"Done!")

main()