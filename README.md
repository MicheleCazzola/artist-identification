# Machine Learning for Vision and Multimedia - Project
## Topic
Artist identification in paintings

### Characteristics
Classification task
Source: https://www.kaggle.com/competitions/artist-identification/

### Scientific reference
[Viswanathan, N. (2017), Artist Identification with Convolutional Neural Networks, Stanford](https://cs231n.stanford.edu/reports/2017/pdfs/406.pdf)

[Ke Xu (2024), Automated Artist Identification Using Deep Learning and Transfer Learning Techniques, Dean & Francis, _Vol. 1 No. 8 (2024): Issue 8_](https://www.deanfrancispress.com/index.php/te/article/view/974/TE002092.pdf)

[Krishnaraja S., Prasad M. (2024), Identifying Artists from Paintings using Deep Learning Models, _ICSSEECC_](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10649467)


## Tasks
In priority order:
1) fine-tuning of a CV backbone (from papers)
2) comparison among different setups (hyperparameter tuning)
3) comparison among different backbones

### Dataset
Dataset from Kaggle: https://www.kaggle.com/competitions/artist-identification/data

Dimension: ~25.2k images (~8.5 GB)

Train-Test split already performed by Kaggle: ~21k/4k 

Train-Validation split performed 80-20, even if other options are yet to be considered after a further data analysis.  
Due to huge dimension of dataset and low computational resources available, it may be necessary to sample it, taking only a portion. In this case, the split would be more unbalanced to the validation split (70-30 or 60-40), to have enough data for validation and testing.

### Data preprocessing
Perform some data augmentation on training set only.

Focus on particular transformations, since some of them could be ineffective for this task (ex. those related to colors and style).

### Training
Take a pretrained model, fine-tune using transfer learning and performing hyperparameter tuning.  

Operations:
1) Try different optimizers: SGD, Adam  
2) Try different learning rates:
   - LR + momentum
   - scheduling: step (used together with LR and momentum, if needed), cosine (`optional`), linear (`optional`)
   - different values of LR wrt layers (`optional`)
3) Evaluate top-1 global accuracy wrt epochs
4) Apply regularization (L2, weight decay) to achieve better generalization

Repeat these operations for different backbones (as explained in the papers, 3-5 depending on computational resources and model size).

### Metrics
Possible evaluation metrics:
- global accuracy (top-1)
- mean class accuracy (MCA): average of accuracies for each artist
- (`optional`) top-k accuracy (k = 3, 5), per class, averaged (not weighted) on classes
- (`optional`) Kaggle scoring: $\frac{1}{k}$ point for top-k accuracy, with k <= 5. An average score will be calculated for each artist across their paintings.
- (`optional`) Kaggle submission: it uses Kaggle scoring on both public and private test instances. The former are those in the provided test set, the latter are not disclosed: it is necessary to submit a properly formatted .csv file on Kaggle competition portal to get this evaluation. It could be interesting to compare this work wrt what done by other teams during the challenge period. 

Validation workflow: single-fold validation. Cross validation would be too resource and time consuming; moreover, it seems dataset is large enough.

### Results presentation
Methods:
- confusion matrix
- accuracy wrt training epochs
- metrics wrt some model parameter (such as model size)
- some results in tabular format

These results are intended to be presented only wrt most relevant (that is, best performing for each backbone type) models. 

## Final notes
What marked with `optional` is mentioned to be developed only if the other tasks would not be enough to obtain the maximum grade in the project, considering a well-done work.

We are glad if you provide us any suggestion related to the development of this project, in particular related to the number of different backbones to try.