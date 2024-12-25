# Training results

## Model resource consumption

| Backbone Model | HOG | Latency (ms) | FPS | Parameters (M) | Accuracy (%) (*) |
|:-------:|:---------:|:---:|:-----:|:------------:|:---:|
| Random crop | No | 9.5 | 105.5 | 27.4 | 0.1 (**)  |
| Random crop | 81 | 17.5 | 57 | 27.4 | 0.1 (**) |
| Random crop | 4056 | 19.5 | 51 | 28.05| 0.1 (**) |
| ResNet18 | No | 16 | 62 | 48.75 |69.8 |
| ResNet18 | 81 | 26 | 38.5 | 48.77 |69.8 |
| ResNet18 | 4056 | 28 | 36 | 49.38 |69.8 |
| MobileNetV3-S | No | 21 | 47 | 30.3 |67.7 |
| MobileNetV3-S | 81 | 30 | 33 | 30.3 |67.7 |
| MobileNetV3-S | 4056 | 32 | 31 | 31 |67.7 |
| EfficientNet-B0 | No | 28 | 36 | 35.1 |76.3 |
| EfficientNet-B0 | 81 | 36 | 28 | 35.1 |76.3 |
| EfficientNet-B0 | 4056 | 39.5 | 25.5 |35.7 |76.3 |
| RegNetX-400MF | No | 32 | 31.5 | 37.15 |77.6 |
| RegNetX-400MF | 81 | 39 | 25.5 | 37.16 |77.6 |
| RegNetX-400MF | 4056 | 42.7 | 23.5 | 37.78 |77.6 |
| ShuffleNetV2-X0.5 | No | 25 | 40 | 28.1 |60.3 |
| ShuffleNetV2-X0.5 | 81 | 33 | 30.5 | 28.1 |60.3 |
| ShuffleNetV2-X0.5 | 4056 | 37 | 27 | 28.7 |60.3 |
| MNasNet-X0.5 | No | 21 | 47 | 29.2 |68.9 |
| MNasNet-X0.5 | 81 | 29 | 34.5 | 29.2 |68.9 |
| MNasNet-X0.5 | 4056 | 32 | 31 | 29.9 |68.9 |


(*) Top-1 accuracy of the backbone model alone, as measured on ImageNet  
(**) Intended as the top-1 accuracy of a random guesser, as measured on ImageNet (1000 classes)

## Trial results

**Notes**:
- metrics are computed on a test set by default, otherwise look for (*)
- HOG features are extracted from a 224x224 center-cropped image, obtained from a 256x256 downsampled image (original is 512x512)
- 

| Backbone Model | HOG | Batch size | Learning rate | Scheduler step | Scheduler factor | Weight decay | Color jitter | Lighting noise | Gaussian blur| Geometric transform | Epochs | Reduction factor | Top-1 accuracy (%) | Top-5 accuracy (%) | MCA (%) | Training time (mins) |
|:--------------:|:---:|:----------:|:-------------:|:------------:|:------------:|:------:|:----------------:|:--------------:|:--------------:|:---:|:-------------:|:--:|:--:|:--:|:--:|:--:|
| Random crop | No | | | | | | | | | | | | | | | |
| Random crop | 81 | | | | | | | | | | | | | | | |
| ResNet18 | No | | | | | | | | | | | | | | | |
| ResNet18 | 81 | | | | | | | | | | | | | | | |
| MobileNetV3-S | No | | | | | | | | | | | | | | |
| MobileNetV3-S | 81 | | | | | | | | | | | | | | |
| EfficientNet-B0 | No | | | | | | | | | | | | | | |
| EfficientNet-B0 | 81 | | | | | | | | | | | | | | |
| RegNetX-400MF | No | | | | | | | | | | | | | | |
| RegNetX-400MF | 81 | | | | | | | | | | | | | | |
| ShuffleNetV2-X0.5 | No | | | | | | | | | | | | | | |
| ShuffleNetV2-X0.5 | 81 | | | | | | | | | | | | | | |
| MNasNet-X0.5 | No | | | | | | | | | | | | | | |
| MNasNet-X0.5 | 81 | | | | | | | | | | | | | | |

(*) value computed on training set  
(**) in the form "probability - (param1, param2, ...)"