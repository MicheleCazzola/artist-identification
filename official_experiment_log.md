# Official experiment log

Backbone Model | HOG | Batch size | Loss | Optimizer |Learning rate | Scheduler milestones | Scheduler gammas | Weight decay | Color jitter  | Lighting noise | Gaussian blur | Geometric transform  | Epochs | Reduction factor | Best validation loss| Best validation WT5-MCA (%) | Best epochs | Test loss | Top-1 accuracy (%) | Top-5 accuracy (%) | MCA (%) | Top-5 weighted MCA (%) | Kaggle score | Training time (mins) | GPU (type, GB) | Output folder |
|:--------------:|:---:|:--:|:----------:|:-----------:|:--:|:-------------:|:------------:|:--:|:------------:|:------:|:----------------:|:--------------:|:--------------:|:---:|:-------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ResNet18 | No | 16 | CE | AdamW | 1e-4 | 8,26 | 0.31622 | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 2.61 | 42.03 | 29 | 2.67 | 41.25 | 65.69 | 31.66 | 41.35 | 0.380 | 292 | L4,22 |[ResNet18](/out/official/resnet/) |
| ResNet18 | Yes | 16 | CE | AdamW | 1e-4 | 10,20 | 0.5 | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 2.64 | 42.89 | 27 | 2.67 | 41.66 | 66.16 | 32.83 | 42.31 | 0.400 | 330 | L4,22 |[ResNet + HOG](/out/official/resnet_hog/) |
| MobileNetV3-S | No | 16 | CE | AdamW | 1e-4 | 20 | 0.5 | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 2.37 | 48.15 | 30 | 2.44 | 45.39 | 70.90 | 36.99 | 46.97 | 0.436 | 241 | L4,22 |[MobileNetV3-S](/out/official/mobilenet/) |
| MobileNetV3-S | Yes | 16 | CE | AdamW | 1e-4 | 15 | 0.5 | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 2.73 | 42.1 | 29 | 2.76 | 40.00 | 65.88 | 30.87 | 41.07 | - | 257 | L4,22 |[MobileNetV3-S + HOG](/out/official/mobilenet_hog/) |
| RegNetX-400MF | No | 16 | CE | AdamW | 1e-4 | 10,25 | 0.5,0.25 | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 4.81 | 44.37 | 25 | 2.4 | 43.50 | 69.00 | 33.46 | 43.75 | 0.417 | 276 | L4,22 |[RegNetX-400MF](/out/official/regnet/) |
| RegNetX-400MF | Yes | 16 | CE | AdamW | 1e-4 | 10,20,25 | 0.5,0.5,0.25 | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 2.47 | 45.42 | 29 | 2.52 | 42.69 | 68.20 | 33.69 | 43.84 | 0.417 | 324 | L4,22 |[RegNetX-400MF + HOG](/out/official/regnet_hog/) |
| Random crop | No | 16 | CE | AdamW | 1e-4 | - | - | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 2.81 | 42.97 | 29 | 2.88 | 40.59 | 64.78 | 32.11 | 40.93 | 0.409 | 244 | L4,22 |[Random Crop](/out/official/random/) |
| Random crop | Yes | 16 | CE | AdamW | 1e-4 | - | - | 1e-4 | 0.5 | 0.5 | 0.5 | 0.5 | 30 | 1 | 3.45 | 40.65 | 30 |3.62 | 36.00 | 60.79 | 28.80 | 38.00 | - | 290 | L4,22  |[Rabdom Crop + Hog](/out/official/random_hog/) |





