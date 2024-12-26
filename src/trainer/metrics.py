import logging
import torch
from torchmetrics.classification import MulticlassAccuracy, MulticlassConfusionMatrix


class Metrics:
    def __init__(self, num_classes: int, top_k: int):
        
        if top_k > num_classes:
            logging.error(f"Top-k value {top_k} cannot be greater than number of classes {num_classes}")
        
        self.num_classes: int = num_classes
        self.top_k: int = top_k
        self.top_1_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes)
        self.top_k_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes, top_k)
        self.mca: MulticlassAccuracy = MulticlassAccuracy(num_classes, average=None)
        self.confusion_matrix: MulticlassConfusionMatrix = MulticlassConfusionMatrix(num_classes, normalize="true")
        
        # TODO: Add Kaggle score (optional)
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        self.top_1_accuracy.update(outputs, labels)
        self.top_k_accuracy.update(outputs, labels)
        self.mca.update(outputs, labels)
        self.confusion_matrix.update(outputs, labels)
        
    def reset(self):
        self.top_1_accuracy.reset()
        self.top_k_accuracy.reset()
        self.mca.reset()
        self.confusion_matrix.reset()
        
    def compute(self):
        top_1_accuracy = self.top_1_accuracy.compute().item()
        top_k_accuracy = self.top_k_accuracy.compute().item()
        mca_result = self.mca.compute().mean().item()
        top_1_confusion_matrix = self.confusion_matrix.compute().tolist()
        
        return {
            "top-1_accuracy": top_1_accuracy,
            f"top-{self.top_k}_accuracy": top_k_accuracy,
            "mca": mca_result,
            "confusion_matrix": top_1_confusion_matrix
        }
        
    def to(self, device: torch.device):
        return Metrics.from_metrics(
            self.num_classes,
            self.top_k,
            self.top_1_accuracy.to(device),
            self.top_k_accuracy.to(device),
            self.mca.to(device),
            self.confusion_matrix.to(device)
        )

    @staticmethod
    def from_metrics(num_classes, top_k, *metrics) -> "Metrics":
        new_metrics = Metrics(num_classes, top_k)
        new_metrics.top_1_accuracy = metrics[0]
        new_metrics.top_k_accuracy = metrics[1]
        new_metrics.mca = metrics[2]
        new_metrics.confusion_matrix = metrics[3]

        return new_metrics