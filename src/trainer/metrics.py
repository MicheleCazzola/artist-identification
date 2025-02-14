import logging
import torch
import torch.nn.functional as F

from torchmetrics import Metric
from torchmetrics.classification import MulticlassAccuracy, MulticlassConfusionMatrix

class WeightedTopKMCA(MulticlassAccuracy):
    """
    Computes the Weighted Top-K Mean Class Accuracy (MCA) for a given number of classes and top-k value.
    The top-k value is the number of top predictions to consider for the MCA computation.
    Each top-k prediction is weighted, since it has a score depending on its position in the top-k list.
    The MCA is computed as the mean of the weighted top-k predictions for each class.
    
    Attributes:
    -----------
    scores: torch.Tensor
        Scores for each class and top-k prediction
    weights: torch.Tensor
        Weights for each top-k prediction
    samples_per_class: torch.Tensor
        Number of samples for each class
    """
    def __init__(self, num_classes: int, top_k: int):
        super(WeightedTopKMCA, self).__init__(num_classes, top_k)
        self.scores = torch.zeros(num_classes, top_k, dtype=torch.long)
        self.weights = torch.tensor([1 / (k + 1) for k in range(top_k)])
        self.samples_per_class = torch.zeros(num_classes)
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        """
        Updates the scores for each class and top-k prediction.
        
        outputs: torch.Tensor
            Predictions of the model
        labels: torch.Tensor
            Ground truth labels
        """
        
        # Compute the top-k predictions
        preds = torch.topk(outputs, self.top_k, dim=1).indices
        
        # Compute one-hot encoding for the labels (N x C)
        labels_one_hot = F.one_hot(labels.long(), num_classes=self.num_classes).long()
        
        # Compute one-hot encoding for the predictions (N x K x C)
        outputs_one_hot = F.one_hot(preds, num_classes=self.num_classes).long().transpose(1, 2)
        
        # Compute the match matrix (N x C x K)
        match_matrix = (labels_one_hot.unsqueeze(2) & outputs_one_hot).long()
        
        # Update the scores for each class in the match matrix (C x K)
        self.scores += match_matrix.sum(dim=0).to(self.scores.device)
        
        # Update the number of samples for each class (C)
        self.samples_per_class += labels_one_hot.sum(dim=0).to(self.samples_per_class.device)
            
    def reset(self):
        """
        Reset the scores, weights and samples per class.
        """
        self.scores = torch.zeros(self.num_classes, self.top_k).to(self.device)
        self.samples_per_class = torch.zeros(self.num_classes).to(self.device)
        self.weights = self.weights.to(self.device)
    
    def compute(self):
        """
        Compute the Weighted Top-K Mean Class Accuracy (MCA): the mean of the weighted top-k predictions for each class.
        The weighted top-k predictions are computed as the sum of the scores for each class and top-k prediction, divided by the
        number of samples for each class.
        
        """
        return torch.mean(
            (self.scores * self.weights).sum(dim=1).to(self.samples_per_class.device) / self.samples_per_class
        )

class Metrics(Metric):
    """
    Generic class to compute the metrics for a given number of classes and top-k value.
    The metrics computed are:
    - Top-1 Accuracy
    - Top-K Accuracy
    - Mean Class Accuracy (MCA)
    - Weighted Top-K MCA
    - Confusion Matrix (not properly a metric as others, but computed here)
    
    Attributes:
    -----------
    num_classes: int
        Number of classes
    top_k: int
        top-k value for the metrics
    top_1_accuracy: MulticlassAccuracy
        Top-1 accuracy metric, averaged over all the samples
    top_k_accuracy: MulticlassAccuracy
        Top-K accuracy metric, averaged over all the samples
    mca: MulticlassAccuracy
        Mean Class Accuracy (MCA) metric, averaged over all the classes
    weighted_top_k_mca: WeightedTopKMCA
        Weighted Top-K MCA metric
    confusion_matrix: MulticlassConfusionMatrix
        Confusion matrix metric, normalized over the true labels
    """
    def __init__(self, num_classes: int, top_k: int):
        
        if top_k > num_classes:
            logging.error(f"Top-k value {top_k} cannot be greater than number of classes {num_classes}")
            
        super(Metrics, self).__init__()
        
        self.num_classes: int = num_classes
        self.top_k: int = top_k
        self.top_1_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes, average="micro")
        self.top_k_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes, top_k, average="micro")
        self.mca: MulticlassAccuracy = MulticlassAccuracy(num_classes, average="macro")
        self.weighted_top_k_mca: WeightedTopKMCA = WeightedTopKMCA(num_classes, top_k)
        self.confusion_matrix: MulticlassConfusionMatrix = MulticlassConfusionMatrix(num_classes, normalize="true")
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        """Update the metrics with the given outputs and labels"""
        self.top_1_accuracy.update(outputs, labels)
        self.top_k_accuracy.update(outputs, labels)
        self.mca.update(outputs, labels)
        self.weighted_top_k_mca.update(outputs, labels)
        self.confusion_matrix.update(outputs, labels)
        
    def reset(self):
        """Reset the metrics"""
        self.top_1_accuracy.reset()
        self.top_k_accuracy.reset()
        self.mca.reset()
        self.weighted_top_k_mca.reset()
        self.confusion_matrix.reset()
        
    def compute(self):
        """Compute the metrics and return them as a dictionary"""
        top_1_accuracy = self.top_1_accuracy.compute().item()
        top_k_accuracy = self.top_k_accuracy.compute().item()
        mca_result = self.mca.compute().item()
        weighted_top_k_mca = self.weighted_top_k_mca.compute().item()
        top_1_confusion_matrix = self.confusion_matrix.compute().tolist()
        
        return {
            "top-1_accuracy": top_1_accuracy,
            f"top-{self.top_k}_accuracy": top_k_accuracy,
            "mca": mca_result,
            f"weighted_top-{self.top_k}_mca": weighted_top_k_mca,
            "confusion_matrix": top_1_confusion_matrix
        }
    
    
# Local test
if __name__ == "__main__":
    
    wt5_mca = WeightedTopKMCA(5, 3)
    # mca = MulticlassAccuracy(5, average=None)
    # top2_mca = MulticlassAccuracy(5, top_k=2, average=None)
    # top3_mca = MulticlassAccuracy(5, top_k=3, average=None)
    
    outputs1 = torch.tensor([
        [0.1, 0.2, 0.3, 0.15, 0.25],
        [0.05, 0.15, 0.25, 0.35, 0.2],
        [0.2, 0.1, 0.4, 0.14, 0.16],
        [0.3, 0.1, 0.2, 0.25, 0.15],
        [0.25, 0.15, 0.1, 0.3, 0.2],
        [0.2, 0.3, 0.1, 0.25, 0.15]])
    outputs2 = torch.tensor([
        [0.15, 0.25, 0.2, 0.1, 0.3],
        [0.35, 0.05, 0.25, 0.2, 0.15],
        [0.15, 0.2, 0.3, 0.1, 0.25],
        [0.25, 0.1, 0.2, 0.3, 0.15],
        [0.35, 0.1, 0.18, 0.22, 0.15],
        [0.35, 0.12, 0.2, 0.16, 0.17]
    ])
    
    #outputs1 = outputs1[:3, :2]
    
    per_class_predictions = torch.argmax(outputs1, dim=1)
    per_class_second_predictions = torch.argsort(outputs1, dim=1)[:, -2]
    per_class_third_predictions = torch.argsort(outputs1, dim=1)[:, -3]
    
    labels1 = torch.tensor([0, 1, 2, 3, 4, 0])
    labels2 = torch.tensor([1, 2, 3, 4, 3, 0])
    
    #labels1 = labels1[:3]
    
    print(labels1)
    print(labels2)
    print()
    
    print(per_class_predictions)
    print(per_class_second_predictions)
    print(per_class_third_predictions)
    print()
    
    wt5_mca.update(outputs1, labels1)
    print(wt5_mca.compute())
    wt5_mca.update(outputs2, labels2)
    result_good = wt5_mca.compute()
    
    #print(good.scores)
    
    # mca.update(outputs1, labels1)
    # mca_result = mca.compute().mean().item()
    
    # top2_mca.update(outputs1, labels1)
    # top2_result = top2_mca.compute().mean().item()
    
    # top3_mca.update(outputs1, labels1)
    # top3_result = top3_mca.compute().mean().item()
    
    # print(result_good, mca_result, top2_result, top3_result)
    
    print(result_good)