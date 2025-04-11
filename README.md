# Artist Identification

## Authors:
- [Michele Cazzola](https://github.com/MicheleCazzola)
- [Giuseppe Arbore](https://github.com/GiuseppeArbore)

## General information
**Course**: `Machine Learning for Vision and Multimedia` (`Polytechnic of Turin`)  
**Academic Year**: 2024-25, developed from December 2024 to February 2025  
**Main teachers**: Fabrizio Lamberti, Lia Morra, Francesco Manigrasso  
**Topic**: implementation of a neural network for painting classification

## Repository structure
```
.
├── colab
│   ├── notebooks used to train the models on Google Colab.
├── data
│   ├── stats used to normalize the images.
├── kaggle
│   ├── notebook used to submit the results on Kaggle (quick and dirty).
├── out
│   └── colab
|   |   ├── experiments done in colab
│   └── official
|       ├── official experiments with results presented in the report
├── scripts
│   ├── general code used to perform unofficial tests and calculate statistics
├── src
│   ├── code used to train the models
├── README.md
```

## Details
We trained multiple neural networks, using several configurations, whose results are summarized in the [experiment log](official_experiment_log.md).

We implemented the codebase from scratch, without using external repositories, except for Python packages. However, we do not claim the design as ours; see the section [Main references](#main-references) for details. We modified some details to adapt the original approach to our task and our computational resources.

We do not claim the dataset as our own. It is hosted on Kaggle and provided together with the competition specifications ([Main references](#main-references) for details). We moved the images to our repository [artist-identification-dataset](https://github.com/MicheleCazzola/artist-identification-dataset) to better adapt data to our needs. 

As hardware, we used GPUs from Google Colab environment, mainly T4 (15 GB). The final runs have been performed with L4 (22 GB), to have higher time availability.

We explained our work and showed some results in the project report [[PDF](report.pdf)].

## Main references
This project is inspired by the following Kaggle competition: "BYU AI Association. [Artist Identification](https://kaggle.com/competitions/artist-identification). 2024. Kaggle."

The original design of the network is explained in the following paper: "Simone Bianco, Davide Mazzini, Paolo Napoletano, and Raimondo Schettini. Multitask painting categorization by deep multibranch neural network, 2018." [[PDF](https://arxiv.org/pdf/1812.08052)]
