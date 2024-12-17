import logging
import os
from src.config import Config
from src.dataset import create_datasets
from src.dataloader import create_dataloaders
from src.stats import compute_stats
from src.transformations import Transforms
from src.train import Trainer
from src.mutlti_branch_nn import MultibranchNetwork
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
        
    # Load datasets with base transformations (resize, crop, to tensor)
    transformations = Transforms(config=cfg)
    trainset, validset, testset = create_datasets(
        root, 
        train_split_size=cfg.train_split_size, 
        transforms=transformations.get(),
        reduction_factor=cfg.reduce_factor,
    )
    
    # Compute mean and standard deviation (only for training set) for normalization
    trainloader_stats = create_dataloaders([trainset], cfg.batch_size, shuffle=False, drop_last=False, num_workers=cfg.num_workers)
    mean, std = map(compute_stats(trainset, trainloader_stats, cfg.device, cfg.norm_stats_file).get, ["mean", "std"])
    transformations.set_norm(mean, std)
    
    # Create dataloaders for all the datasets: normalization applied during training
    trainloader, validloader, testloader = create_dataloaders(
        [trainset, validset, testset],
        cfg.batch_size,
        num_workers=cfg.num_workers
    )

    # Model definition
    model = MultibranchNetwork(out_classes=cfg.num_classes)
    
    logging.info(f"Training setup...")
    trainer = Trainer(model, trainloader, validloader, testloader)
    trainer.build(cfg)
    trainer.add_aug_transforms(transformations.get("aug"))
    
    logging.info(f"Training...")
    trainer.train()
    
    logging.info(f"Inference...")
    trainer.test()
    
    logging.info(f"Saving results...")
    trainer.save_results(cfg, cfg.results_root)
    
    os.remove(cfg.norm_stats_file)
    
    logging.info(f"Done!")

main()