import logging
import torch
from torchmetrics.classification import MulticlassAccuracy, MulticlassConfusionMatrix


class WeightedTopKMCA:
    def __init__(self, num_classes: int, top_k: int):
        self.num_classes: int = num_classes
        self.top_k: int = top_k
        self.mca = [
            MulticlassAccuracy(num_classes, top_k=k, average=None) for k in range(1, top_k+1)
        ]
        self.weights = [
            1 / (k + 1) for k in range(top_k)
        ]
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        for mca in self.mca:
            mca.update(outputs, labels)
    
    def reset(self):
        for mca in self.mca:
            mca.reset()
        
    def compute(self):
        weighted_mca = torch.tensor([mca.compute().mean().item() for mca in self.mca])
        return torch.dot(weighted_mca, torch.tensor(self.weights))

    def to(self, device: torch.device):
        new_mca = WeightedTopKMCA(self.num_classes, self.top_k)
        new_mca.mca = [mca.to(device) for mca in self.mca]
        new_mca.weights = self.weights
        return new_mca
        

class Metrics:
    def __init__(self, num_classes: int, top_k: int):
        
        if top_k > num_classes:
            logging.error(f"Top-k value {top_k} cannot be greater than number of classes {num_classes}")
        
        self.num_classes: int = num_classes
        self.top_k: int = top_k
        self.top_1_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes)
        self.top_k_accuracy: MulticlassAccuracy = MulticlassAccuracy(num_classes, top_k)
        self.mca: MulticlassAccuracy = MulticlassAccuracy(num_classes, average=None)
        self.weighted_top_k_mca: WeightedTopKMCA = WeightedTopKMCA(num_classes, top_k)
        self.confusion_matrix: MulticlassConfusionMatrix = MulticlassConfusionMatrix(num_classes, normalize="true")
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        self.top_1_accuracy.update(outputs, labels)
        self.top_k_accuracy.update(outputs, labels)
        self.mca.update(outputs, labels)
        self.weighted_top_k_mca.update(outputs, labels)
        self.confusion_matrix.update(outputs, labels)
        
    def reset(self):
        self.top_1_accuracy.reset()
        self.top_k_accuracy.reset()
        self.mca.reset()
        self.weighted_top_k_mca.reset()
        self.confusion_matrix.reset()
        
    def compute(self):
        top_1_accuracy = self.top_1_accuracy.compute().item()
        top_k_accuracy = self.top_k_accuracy.compute().item()
        mca_result = self.mca.compute().mean().item()
        weighted_top_k_mca = self.weighted_top_k_mca.compute().item()
        top_1_confusion_matrix = self.confusion_matrix.compute().tolist()
        
        return {
            "top-1_accuracy": top_1_accuracy,
            f"top-{self.top_k}_accuracy": top_k_accuracy,
            "mca": mca_result,
            f"weighted_top-{self.top_k}_mca": weighted_top_k_mca,
            "confusion_matrix": top_1_confusion_matrix
        }
        
    def to(self, device: torch.device):
        return Metrics.from_metrics(
            self.num_classes,
            self.top_k,
            self.top_1_accuracy.to(device),
            self.top_k_accuracy.to(device),
            self.mca.to(device),
            self.weighted_top_k_mca.to(device),
            self.confusion_matrix.to(device)
        )

    @staticmethod
    def from_metrics(num_classes, top_k, *metrics) -> "Metrics":
        new_metrics = Metrics(num_classes, top_k)
        new_metrics.top_1_accuracy = metrics[0]
        new_metrics.top_k_accuracy = metrics[1]
        new_metrics.mca = metrics[2]
        new_metrics.weighted_top_k_mca = metrics[3]
        new_metrics.confusion_matrix = metrics[4]

        return new_metrics