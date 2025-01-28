import argparse
from src.config.config import Config, PathConfig, EnvConfig, DataConfig, TrainConfig, ModelConfig, HOGConfig

def parse_args(cfg: Config):
    parser = argparse.ArgumentParser()
    
    # cfg.env arguments
    parser.add_argument('--root', type=str, default=cfg.path.root, help="Root directory")
    parser.add_argument('--test-root', type=str, default=cfg.path.test_root, help="Test root directory (only for submission on Kaggle)")
    parser.add_argument('--stats-file', type=str, default=cfg.path.stats_file, help="Stats file path")
    parser.add_argument('--norm-stats-file', type=str, default=cfg.path.norm_stats_file, help="Normalization stats file path")
    parser.add_argument('--saved-model-path', type=str, default=cfg.path.saved_model_path, help="Path to save model or checkpoint")
    parser.add_argument('--saved-best-model-path', type=str, default=cfg.path.saved_best_model_path, help="Path to save best model or checkpoint")
    parser.add_argument('--results-root', type=str, default=cfg.path.results_root, help="Results directory")
    parser.add_argument('--trained-model-path', type=str, default=cfg.path.trained_model_path, help="Path to trained model or checkpoint")
    parser.add_argument('--predictions-path', type=str, default=cfg.path.predictions_path, help="Path to save predictions (only for submission on Kaggle)")

    parser.add_argument('--device', type=str, default=cfg.env.device, help="Device for computation (cpu or cuda)")
    parser.add_argument('--num-workers', type=int, default=cfg.env.num_workers, help="Number of workers for data loading (0 if working on cpu)")
    parser.add_argument('--seed', type=int, default=cfg.env.seed, help="Random seed")

    # cfg.data arguments
    parser.add_argument('--pretrained-stats', action='store_true', default=cfg.data.pretrained_stats, help="Use pretrained stats (ImageNet if true)")
    parser.add_argument('--resize-dim', type=int, default=cfg.data.resize_dim, help="Resize dimension (image preprocessing)")
    parser.add_argument('--crop-dim', type=int, default=cfg.data.crop_dim, help="Crop dimension (image preprocessing)")
    parser.add_argument('--aug-probs', type=float, nargs=4, default=cfg.data.aug_probs, help="Augmentation probabilities (color jitter, lighting noise, blur, random resized crop)")
    parser.add_argument('--aug-mask', type=bool, nargs=4, default=cfg.data.aug_mask, help="Augmentation mask (color jitter, lighting noise, blur, random resized crop)")
    parser.add_argument('--augment', action='store_true', default=cfg.data.augment, help="Enable augmentation")
    parser.add_argument('--reduce-factor', type=float, default=cfg.data.reduce_factor, help="Reduction factor for dataset")
    parser.add_argument('--batch-size-model', type=int, default=cfg.data.batch_size_model, help="Batch size for model")

    # cfg.train arguments
    parser.add_argument('--num-epochs', type=int, default=cfg.train.num_epochs, help="Number of epochs (resume included, if present)")
    parser.add_argument('--train-log-frequency', type=int, default=cfg.train.train_log_frequency, help="Train log frequency")
    parser.add_argument('--val-log-frequency', type=int, default=cfg.train.val_log_frequency, help="Validation log frequency")
    parser.add_argument('--train-accuracy', action='store_true', default=cfg.train.train_accuracy, help="Enable train accuracy calculation (not recommended, very slow)")
    parser.add_argument('--lr', type=float, default=cfg.train.lr, help="Learning rate")
    parser.add_argument('--momentum', type=float, default=cfg.train.momentum, help="Momentum (used in SGD)")
    parser.add_argument('--weight-decay', type=float, default=cfg.train.weight_decay, help="Weight decay")
    parser.add_argument('--scheduler-milestones', type=int, nargs='+', default=cfg.train.scheduler_milestones, help="Scheduler milestones for LR decay (same length as factors)")
    parser.add_argument('--scheduler-factors', type=float, nargs='+', default=cfg.train.scheduler_factors, help="Scheduler factors LR decay (same length as milestones)")
    parser.add_argument('--criterion', type=str, default=cfg.train.criterion, help="Criterion")
    parser.add_argument('--optimizer', type=str, default=cfg.train.optimizer, help="Optimizer")
    parser.add_argument('--scheduler', type=str, default=cfg.train.scheduler, help="Scheduler")
    parser.add_argument('--top-k', type=int, default=cfg.train.top_k, help="Top-k accuracy level")
    parser.add_argument('--sanity-check', action='store_true', default=cfg.train.sanity_check, help="Enable sanity check before training (very slow)")
    parser.add_argument('--save-models', action='store_true', default=cfg.train.save_models, help="Save all models (or checkpoints)")
    parser.add_argument('--save-models-step', type=int, default=cfg.train.save_models_step, help="Step for saving models (or checkpoints)")
    parser.add_argument('--train-only', action='store_true', default=cfg.train.train_only, help="Train only mode")
    parser.add_argument('--inference-only', action='store_true', default=cfg.train.inference_only, help="Inference only mode")
    parser.add_argument('--train-acc-only', action='store_true', default=cfg.train.train_acc_only, help="Compute only accuracy on training set")
    parser.add_argument('--save-predictions', action='store_true', default=cfg.train.save_predictions, help="Save predictions (only for submission on Kaggle)")
    parser.add_argument('--resume-training', action='store_true', default=cfg.train.resume_training, help="Resume training from checkpoint")

    # cfg.model arguments
    parser.add_argument('--use-default-init', action='store_true', default=cfg.model.use_default_init, help="Use default initialization (PyTorch)")
    parser.add_argument('--backbone-type', type=str, default=cfg.model.backbone_type, help="Backbone type (random crop if not specified)")
    parser.add_argument('--use-handcrafted', action='store_true', default=cfg.model.use_handcrafted, help="Use handcrafted features (HOG, default is False)")
    parser.add_argument('--precision', type=int, default=cfg.model.precision, help="Floating-point precision (default is 32)")

    # cfg.hog arguments
    parser.add_argument('--downsample-size', type=int, default=cfg.hog.downsample_size, help="HOG: downsample size")
    parser.add_argument('--crop-size', type=int, default=cfg.hog.crop_size, help="HOG: center crop size")
    parser.add_argument('--channel-coefficients', type=float, nargs=3, default=cfg.hog.channel_coefficients, help="HOG: channel coefficient to convert RGB to grayscale")
    parser.add_argument('--orientations', type=int, default=cfg.hog.orientations, help="Number of orientations")
    parser.add_argument('--pixels-per-cell', type=int, default=cfg.hog.pixels_per_cell, help="Pixels per cell")
    parser.add_argument('--cells-per-block', type=int, default=cfg.hog.cells_per_block, help="Cells per block")
    parser.add_argument('--transform-sqrt', action='store_true', default=cfg.hog.transform_sqrt, help="Enable square root transformation (not recommended)")
    parser.add_argument('--feature-vector', action='store_true', default=cfg.hog.feature_vector, help="Enable feature vector")
    parser.add_argument('--normalization', type=str, default=cfg.hog.normalization, help="Normalization type")

    return parser


def encapsulate_args(args):
    return Config(
        path=PathConfig(
            root=args.root,
            test_root=args.test_root,
            stats_file=args.stats_file,
            norm_stats_file=args.norm_stats_file,
            saved_model_path=args.saved_model_path,
            saved_best_model_path=args.saved_best_model_path,
            results_root=args.results_root,
            trained_model_path=args.trained_model_path,
            predictions_path=args.predictions_path,
        ),
        env=EnvConfig(
            device=args.device,
            num_workers=args.num_workers,
            seed=args.seed,
        ),
        data=DataConfig(
            pretrained_stats=args.pretrained_stats,
            resize_dim=args.resize_dim,
            crop_dim=args.crop_dim,
            aug_probs=tuple(args.aug_probs),
            aug_mask=tuple(args.aug_mask),
            augment=args.augment,
            reduce_factor=args.reduce_factor,
            batch_size_model=args.batch_size_model
        ),
        train=TrainConfig(
            num_epochs=args.num_epochs,
            train_log_frequency=args.train_log_frequency,
            val_log_frequency=args.val_log_frequency,
            train_accuracy=args.train_accuracy,
            lr=args.lr,
            momentum=args.momentum,
            weight_decay=args.weight_decay,
            scheduler_milestones=tuple(args.scheduler_milestones),
            scheduler_factors=tuple(args.scheduler_factors),
            criterion=args.criterion,
            optimizer=args.optimizer,
            scheduler=args.scheduler,
            top_k=args.top_k,
            sanity_check=args.sanity_check,
            save_models=args.save_models,
            save_models_step=args.save_models_step,
            train_only=args.train_only,
            inference_only=args.inference_only,
            train_acc_only=args.train_acc_only,
            save_predictions=args.save_predictions,
            resume_training=args.resume_training,
        ),
        model=ModelConfig(
            use_default_init=args.use_default_init,
            backbone_type=args.backbone_type,
            use_handcrafted=args.use_handcrafted,
            precision=args.precision,
        ),
        hog=HOGConfig(
            downsample_size=args.downsample_size,
            crop_size=args.crop_size,
            channel_coefficients=tuple(args.channel_coefficients),
            orientations=args.orientations,
            pixels_per_cell=args.pixels_per_cell,
            cells_per_block=args.cells_per_block,
            transform_sqrt=args.transform_sqrt,
            feature_vector=args.feature_vector,
            normalization=args.normalization,
        )
    )

def get_config(default_cfg: Config) -> Config:
    parser = parse_args(default_cfg)
    args = parser.parse_args()
    return encapsulate_args(args)