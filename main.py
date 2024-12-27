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
    
    logging.info(f"Training...")
    
    trainer.train()
    training_time = trainer.train.time
    
    logging.info(f"Inference...")
    
    trainer.test()
    test_time = trainer.test.time
    
    print(f"Test accuracy: {trainer.test_results.metrics['top-1_accuracy']:.3f}, Test loss: {trainer.test_results.loss:.5f}")
    
    logging.info(f"Saving results...")
    
    trainer.save_results(cfg, cfg.path.results_root, transformations, training_time, test_time)
    
    os.remove(cfg.path.norm_stats_file)
    
    classifier = trainer.model.classifier.state_dict()
    weights, biases = classifier["weight"], classifier["bias"]
    net_weights, hog_features = weights[:, :2048], weights[:, 2048:]
    print(net_weights.shape, hog_features.shape, biases.shape)
    net_mean, net_std, net_min, net_max = net_weights.mean(), net_weights.std(), net_weights.min(), net_weights.max()
    hog_mean, hog_std, hog_min, hog_max = hog_features.mean(), hog_features.std(), hog_features.min(), hog_features.max()
    
    print(net_max)
    
    print(f"Net width: {net_max - net_min:.3f}, Net mean: {net_mean:.3f}, Net std: {net_std:.3f}")
    print(f"HOG width: {hog_max - hog_min:.3f}, HOG mean: {hog_mean:.3f}, HOG std: {hog_std:.3f}")
    
    logging.info(f"Done!")

main()