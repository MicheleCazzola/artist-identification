import logging
import os

from src.config.config import Config
from src.dataset.dataset import ArtistDataset, UnlabeledArtistDataset
from src.dataset.dataloader import create_dataloaders
from src.transformations.transformations import Transforms
from src.trainer.train import Trainer
from src.model.network import MultiBranchArtistNetwork
from src.utils.utils import load_stats, init_seed
from src.utils.parser import get_config
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
    
    LOCAL = True
    default_cfg = Config.create("local" if LOCAL else "colab")
    
    cfg = get_config(default_cfg)
    
    logging.info(cfg.__dict__)
    
    dataloader_worker_init_fun, dataloader_generator = init_seed(cfg.env.seed)
    
    transformations = Transforms(data_config=cfg.data)
        
    if not cfg.data.pretrained_stats:
        mean, std = load_stats(cfg.path.norm_stats_file)
    else:
        mean, std = transformations.mean, transformations.std
    
    transformations.set_norm(mean, std)
    
    logging.info(f"Normalization stats: mean {transformations.mean}, std {transformations.std}")
    
    if not cfg.data.augment:
        logging.info("No augmentation found, only normalization will be applied")
        
    logging.info(transformations.to_dict())
    
    trainset, validset, testset = ArtistDataset.create(
        cfg.path.root, 
        transforms=transformations.get(),
        augment=cfg.data.augment,
        reduction_factor=cfg.data.reduce_factor,
    )
    
    if cfg.data.reduce_factor is None or cfg.data.reduce_factor == 1:
        assert trainset.categories == validset.categories == testset.categories, "Categories mismatch"
    else:
        assert trainset.dataset.categories == validset.dataset.categories == testset.dataset.categories, "Categories mismatch"
    
    categories = testset.categories if isinstance(testset, ArtistDataset) else testset.dataset.categories
    num_classes = len(categories)
    
    logging.info(categories)
    
    # Create dataloaders for all the datasets: normalization applied during training
    trainloader, validloader, testloader = create_dataloaders(
        [trainset, validset, testset],
        cfg.data.batch_size_model,
        num_workers=cfg.env.num_workers,
        worker_init_fn=dataloader_worker_init_fun,
        generator=dataloader_generator
    )
    
    # Model definition
    model = MultiBranchArtistNetwork(
        num_classes=num_classes,
        stn=cfg.model.backbone_type,
        use_handcrafted=cfg.model.use_handcrafted,
        hog_params=cfg.hog,
        use_default_init=cfg.model.use_default_init,
        precision=cfg.model.precision
    )
    
    logging.info(f"Training setup...")
    
    trainer = Trainer(model, trainloader, validloader, testloader, categories)
    trainer.build(cfg)
    
    training_time = test_time = None
    
    if not (cfg.train.inference_only or cfg.train.train_acc_only):
        logging.info(f"Training...")
        
        trainer.train()
        training_time = trainer.train.time
        
    if not cfg.train.train_only:
        logging.info(f"Inference...")
        
        if cfg.train.inference_only:
            if cfg.train.save_predictions:
                testset = UnlabeledArtistDataset(
                    cfg.path.test_root, 
                    transform=transformations.get("eval")
                )
                testloader = create_dataloaders(
                    [testset],
                    cfg.data.batch_size_model,
                    shuffle=False,
                    drop_last=False,
                    num_workers=cfg.env.num_workers
                )
                trainer.test(cfg.path.trained_model_path, testloader, cfg.path.predictions_path)
            else:
                trainer.test(cfg.path.trained_model_path)
        elif cfg.train.train_acc_only:
            trainset_eval = ArtistDataset.create(
                cfg.path.root,
                transforms=transformations.get(),
                augment=False,
                reduction_factor=cfg.data.reduce_factor,
            )
            trainloader_eval = create_dataloaders(
                [trainset_eval],
                cfg.data.batch_size_model,
                shuffle=False,
                drop_last=False,
                num_workers=cfg.env.num_workers
            )
            trainer.test(cfg.path.trained_model_path, trainloader_eval)        
        else:
            trainer.test()
            
        test_time = trainer.test.time
        
        if not cfg.train.save_predictions:
            print(f"Test accuracy: {trainer.test_results.metrics.get(f'weighted_top-{cfg.train.top_k}_mca'):.3f}, Test loss: {trainer.test_results.loss:.5f}")
        
    logging.info(f"Saving results...")
    
    trainer.save_results(
        cfg, 
        cfg.path.results_root, 
        transformations, 
        training_time,
        test_time,
        cfg.train.train_only,
        cfg.train.inference_only or cfg.train.train_acc_only
    )
    
    logging.info(f"Done!")

main()