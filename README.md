# Artist Identification
This project is a part of the course "Machine Learning for Vision and Multimedia" at the "Politecnico di Torino".
The goal of the project is to identify the artist of a painting based on the image of the painting. 

## Colab
This folder contains the notebooks used to train the models on Google Colab.

## Data
This folder contains the stats used to normalize the images.

## Kaggle
This folder contains the notebook used to submit the results on Kaggle.

## Out
This folder contains two main subfolders:
- Colab: all the experiments done in colab
- Official: all the official results presented in the report

## Scripts
This folder contains the scripts used to generate the stats.


## Src
This folder contains the code used to train the models:
- Config: contains the configuration of the models
- Dataset: contains the dataset and the dataloader
- Model: contains the models
- Trainer: contains the training loop
- Transformations: contains the transformations used in the dataset
- Utils: contains the utility functions

## Repository structure
```
.
├── colab
│   ├── classifier.ipynb
│   ├── clone.sh
│   ├── launch.ipynb
│   ├── resource.ipynb
│   └── stats.ipynb
├── data
│   ├── norm_stats.json
├── kaggle
│   ├── submit.ipynb
├── out
│   └── colab
|   |   ├── train 1
|   |   |   ├── accuracy.png
|   |   |   ├── confusion_matrix.png
|   |   |   ├── loss.png
|   |   |   ├── results.json
|   |   ├──
|   |   ├── train N
|   |       ├── accuracy.png
|   |       ├── confusion_matrix.png
|   |       ├── loss.png
|   |       ├── results.json
│   └── colab
|       ├── train 1
|       |   ├── accuracy.png
|       |   ├── confusion_matrix.png
|       |   ├── loss.png
|       |   ├── results.json
|       ├──
|       ├── train N
|           ├── accuracy.png
|           ├── confusion_matrix.png
|           ├── loss.png
|           ├── results.json
├── scripts
│   ├── hog
│   │   ├── hog.py
│   │   ├── hog2.py
│   │   ├── hog_stats.json
│   ├── print
│   │   ├── print.py
│   ├── resources
│   │   ├── results
│   │   │   ├── tests done with various models to verify latency and accuracy
│   │   ├── resources.py
│   ├── scales
│   │   ├── scales.ipynb
│   ├── stats
│   │   ├── stats.py
│   |   ├── stats_all.json
│   |   ├── stats_all.py
│   |   ├── stats_distr.ipynb
│   |   ├── images
│   |   |   ├── kaggle test
│   |   |   |   ├── images for tests
│   |   |   ├── img_distr.png
│   |   |   ├── test.txt
│   |   |   ├── train.txt
│   |   |   ├── val.txt
│   ├── src
│   │   ├── config
|   |   |   ├── _init_.py
|   |   |   ├── components.py
|   |   |   ├── config.py
│   │   ├── dataset
|   |   |   ├── _init_.py
|   |   |   ├── dataloader.py
|   |   |   ├── dataset.py
│   │   ├── model
|   |   |   ├── _init_.py
|   |   |   ├── backbone.py
|   |   |   ├── components.py
|   |   |   ├── network.py
│   │   ├── trainer
|   |   |   ├── _init_.py
|   |   |   ├── metrics.py
|   |   |   ├── scheduler.py
|   |   |   ├── train.py
│   │   ├── tranformations
|   |   |   ├── _init_.py
|   |   |   ├── augmentations.py
|   |   |   ├── transformations.py
│   │   ├── utils
|   |   |   ├── _init_.py
|   |   |   ├── parser.py
|   |   |   ├── utils.py
│   │   ├── init.py
├── README.md
```