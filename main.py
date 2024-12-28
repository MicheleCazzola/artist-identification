import logging
import os

import torch

from src.config.config import Config
from src.dataset.dataset import ArtistDataset
from src.dataset.dataloader import create_dataloaders
from src.utils.stats import compute_stats
from src.transformations.transformations import Transforms
from src.trainer.train import Trainer
from src.model.network import MultiBranchArtistNetwork
import sys


# def check(*dataloaders):
#     for dataloader in dataloaders:
        
#         print(dataloader)
#         tot_len = len(dataloader)
#         for (step, (inputs, labels)) in enumerate(dataloader):
#             print(f"Step {step+1}/{tot_len}")
#             images = [torchvision.transforms.ToPILImage()(input) for input in inputs]
#             for img, label in zip(images, labels):
#                 plt.figure()
#                 plt.imshow(img)
#                 plt.title(f"Label {label}")
#         print()
#     plt.show()


def main():
    
    logging.basicConfig(level=logging.INFO)
    
    if len(sys.argv) > 1:
        cfg = Config.create("colab")
        root = sys.argv[1]
    else:
        cfg = Config.create("local")
        root = cfg.path.default_root
    
    logging.info(cfg.__dict__)
        
    # Load datasets with base transformations (resize, crop, to tensor)
    transformations = Transforms(data_config=cfg.data)
    trainset, validset, testset = ArtistDataset.create(
        root, 
        train_split_size=cfg.data.train_split_size, 
        transforms=transformations.get(),
        reduction_factor=cfg.data.reduce_factor,
    )
    
    if not cfg.data.pretrained_stats:
        # Compute mean and standard deviation (only for training set) for normalization
        trainloader_stats = create_dataloaders(
            [trainset],
            cfg.data.batch_size,
            shuffle=False,
            drop_last=False,
            num_workers=cfg.env.num_workers
        )
        mean, std = map(
            compute_stats(trainset, trainloader_stats, cfg.env.device, cfg.path.norm_stats_file).get, 
            ["mean", "std"]
        )
    else:
        mean, std = transformations.mean, transformations.std
    
    transformations.set_norm(mean, std)
    
    logging.info(transformations.to_dict())
    
    # Create dataloaders for all the datasets: normalization applied during training
    trainloader, validloader, testloader = create_dataloaders(
        [trainset, validset, testset],
        cfg.data.batch_size,
        num_workers=cfg.env.num_workers
    )

    # Model definition
    model = MultiBranchArtistNetwork(
        num_classes=cfg.train.num_classes,
        stn=cfg.model.backbone_type,
        use_handcrafted=cfg.model.use_handcrafted,
        hog_params=cfg.hog,
        precision=cfg.model.precision
    )
    
    logging.info(f"Training setup...")
    
    trainer = Trainer(model, trainloader, validloader, testloader)
    trainer.build(cfg)
    trainer.add_aug_norm_transforms(transformations.get("aug"))
    
    training_time = test_time = None
    
    if not cfg.train.inference_only:
        logging.info(f"Training...")
        
        trainer.train()
        training_time = trainer.train.time
        
    if not cfg.train.train_only:
        logging.info(f"Inference...")
        
        if cfg.train.inference_only:
            model_path = f"{cfg.path.best_model_path}.pth"
            trainer.test(model_path)
        else:
            trainer.test()
            
        test_time = trainer.test.time
        
        print(f"Test accuracy: {trainer.test_results.metrics['top-1_accuracy']:.3f}, Test loss: {trainer.test_results.loss:.5f}")
        
    logging.info(f"Saving results...")
    
    trainer.save_results(
        cfg, 
        cfg.path.results_root, 
        transformations, 
        training_time,
        test_time,
        cfg.train.train_only,
        cfg.train.inference_only
    )
    
    os.remove(cfg.path.norm_stats_file)
    
    logging.info(f"Done!")

main()