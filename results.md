# Training results

## Model resource consumption

| Backbone Model | HOG | Latency (ms) | FPS | Parameters (M) | Accuracy (%) (*) |
|:-------:|:---------:|:---:|:-----:|:------------:|:---:|
| Random crop | No | 10.4 | 96 | 27.4 | 0.1 (**)  |
| Random crop | 81 | 15.7 | 64 | 27.4 | 0.1 (**) |
| Random crop | 4056 | 18.9 | 53 | 28.05 | 0.1 (**) |
| ResNet18 | No | 19.5 | 51 | 48.75 |69.8 |
| ResNet18 | 81 | 24.7 | 40.4 | 48.77 |69.8 |
| ResNet18 | 4056 | 27.2 | 36.7 | 49.38 |69.8 |
| MobileNetV3-S | No | 21 | 47 | 30.3 |67.7 |
| MobileNetV3-S | 81 | 27.8 | 36 | 30.3 |67.7 |
| MobileNetV3-S | 4056 | 30 | 33.4 | 31 |67.7 |
| EfficientNet-B0 | No | 27.5 | 36.5 | 35.1 |76.3 |
| EfficientNet-B0 | 81 | 33.8 | 29.6 | 35.1 |76.3 |
| EfficientNet-B0 | 4056 | 36.4 | 27.5 |35.7 |76.3 |
| RegNetX-400MF | No | 30 | 33.4 | 37.15 |77.6 |
| RegNetX-400MF | 81 | 36.5 | 27.4 | 37.16 |77.6 |
| RegNetX-400MF | 4056 | 39 | 25.6 | 37.78 |77.6 |
| ShuffleNetV2-X0.5 | No | 23.7 | 42.5 | 28.1 |60.3 |
| ShuffleNetV2-X0.5 | 81 | 30.5 | 33 | 28.1 |60.3 |
| ShuffleNetV2-X0.5 | 4056 | 33.8 | 29.6 | 28.7 |60.3 |
| MNasNet-X0.5 | No | 20.7 | 48.3 | 29.2 |68.9 |
| MNasNet-X0.5 | 81 | 26.5 | 37.7 | 29.2 |68.9 |
| MNasNet-X0.5 | 4056 | 29 | 34.5 | 29.9 |68.9 |


(*) Top-1 accuracy of the backbone model alone, as measured on ImageNet  
(**) Intended as the top-1 accuracy of a random guesser, as measured on ImageNet (1000 classes)

## Trial results

**Notes**:
- metrics are computed on a test set by default, otherwise look for (*)
- HOG features are extracted from a 224x224 center-cropped image, obtained from a 256x256 downsampled image (original is 512x512)

| Backbone Model | HOG | Batch size | Loss | Learning rate | Scheduler step | Scheduler factor | Weight decay | Color jitter (**) | Lighting noise (**) | Gaussian blur (**) | Geometric transform (**) | Epochs | Reduction factor | Test loss | Test epochs | Top-1 accuracy (%) | Top-5 accuracy (%) | MCA (%) | Top-5 weighted MCA (%) | Training time (mins) (***) | Output folder |
|:--------------:|:---:|:--:|:----------:|:-------------:|:------------:|:------------:|:------:|:----------------:|:--------------:|:--------------:|:---:|:-------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Random crop | No | 32 |  |  |  |  |  | | | | |  |  |  |  |  | | | | |[link]() |
| Random crop | No | 32 | CE | 1e-3 | - | - | 1e-6 | - | - | - | - | 2 | 1 | 4.3 | 2 | 10.4 | 26.6 | 2.7 | 5.3 | ~20 |[link](./out/official/20241229_184457/) |
| Random crop | No | 32 | CE | 1e-4 | - | - | 1e-6 | - | - | - | - | 2 | 1 | 3.9 | 2 | 16.2 | 35.4 | 6.65 | 11.1 | ~21 |[link](./out/official/20241230_175101/) |
| Random crop | No | 32 | CE | 1e-4 | - | - | 1e-6 | - | - | - | - | 2 | 1 | 3.8 | 2 | 18.4 | 37.4 | 7.4 | 12.3 | ~21 |[link](./out/official/20241229_184711/) |
| Random crop | No | 32 | WCE | 1e-4 | - | - | 1e-6 | - | - | - | - | 2 | 1 | 3.98 | 2 | 13.6 | 30.8 | 6.4 | 10.4 | ~19 |[link](./out/official/20241230_000332/) |
| Random crop | No | 32 | WCE | 1e-4 | - | - | 1e-6 | - | - | - | - | 2 | 1 | 3.8 | 2 | 14 | 30.3 | 7.04 | 11.1 | ~20 |[link](./out/official/20241230_185001/) |
| Random crop | No | 32 | WCE | 1e-4 | - | - | 1e-5 | - | - | - | - | 2 | 1 | 3.81 | 2 | 13.6 | 30.7 | 6.76 | 11 | ~20 |[link](./out/official/20241230_192513/) |
| Random crop | No | 32 | CE | 1e-4 | - | - | 1e-6 | - | - | - | - | 6 | 1 | 3.4 | 6 | 25 | 48.5 | 14.9 | 22.4 | 60 |[link](./out/official/20241230_225438/) |
| Random crop | No | 32 | WCE | 1e-4 | - | - | 1e-6 | - | - | - | - | 2 | 1 | 3.9 | 2 | 13.8 | 29.8 | 4.77 | 8.13 | ~21 |[link](./out/official/20241230_003603/) |
| ResNet18 | 81 | 16 | CE | 1e-4 | - | - | 1e-5 | - | - | - | - | 2 | 1 | 3.91 | 2 | 16.35 | 36.17 | 6 | 10.6 | ~33 |[link](/out/official/20241229_184539/) |
| ResNet18 | 81 | 16 | WCE | 1e-4 | - | - | 1e-5 | - | - | - | - | 2 | 1 | 3.92 | 2 | 12.3 | 29.4 | 5.7 | 10.1 | ~33 |[link](/out/official/20241230_210424/) |
| ResNet18 | No | 16 | CE | 1e-4 | - | - | 1e-5 | - | - | - | - | 2 | 1 | 4 | 2 | 14.5 | 33.5 | 5.5 | 9.84 | ~28 |[link](/out/official/20241229_182211/) |
| ResNet18 | No | 16 | WCE | 1e-4 | - | - | 1e-5 | - | - | - | - | 2 | 1 | 3.9 | 2 | 13.3 | 29.7 | 6.08 | 10 | ~29 |[link](/out/official/20241230_205642/) |
| ResNet18 | No | 16 | | | | | | | | | | | | | | | | | | |[link]() |
| ResNet18 | 81 | 16 | | | | | | | | | | | | | | | | | | |[link]() |
| MobileNetV3-S | No | 24 | || | | | | | | | | | | | | | | | |[link]() |
| MobileNetV3-S | 81 | 24 | || | | | | | | | | | | | | | | | |[link]() |
| EfficientNet-B0 | No | 8 | || | | | | | | | | | | | | | | | |[link]() |
| EfficientNet-B0 | 81 | 8 | || | | | | | | | | | | | | | | | | [link]() |
| RegNetX-400MF | No | 16 | || | | | | | | | | | | | | | | | | [link]() |
| RegNetX-400MF | 81 | 16 | | || | | | | | | | | | | | | | | |[link]() |
| ShuffleNetV2-X0.5 | No | 24 | || | | | | | | | | | | | | | | | |[link]() |
| ShuffleNetV2-X0.5 | 81 | 24 | || | | | | | | | | | | | | | | | |[link]() |
| MNasNet-X0.5 | No | 16 | | | | || | | | | | | | | | | | | |[link]() |
| MNasNet-X0.5 | 81 | 16 | | | || | | | | | | | | | | | | | |[link]() |

(\*) Value computed on training set  
(*\*) In the form "probability - (param1, param2, ...)"  
(\***) Global training time