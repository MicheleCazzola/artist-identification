import logging
import torch
import torch.nn.functional as F
from torchmetrics.classification import MulticlassAccuracy, MulticlassConfusionMatrix


class WeightedTopKMCA:
    def __init__(self, num_classes: int, top_k: int):
        self.num_classes: int = num_classes
        self.top_k: int = top_k
        self.scores = torch.zeros(num_classes, top_k, dtype=torch.long)
        self.weights = torch.tensor([1 / (k + 1) for k in range(top_k)])
        self.samples_per_class = torch.zeros(num_classes)
        
    def update(self, outputs: torch.Tensor, labels: torch.Tensor):
        outputs = torch.argsort(outputs, dim=1, descending=True)[:, :self.top_k]
        
        # N x C
        labels_one_hot = F.one_hot(labels.long(), num_classes=self.num_classes).long()
        
        # N x C x K
        outputs_one_hot = F.one_hot(outputs, num_classes=self.num_classes).long().transpose(1, 2)
        
        # N x C x K
        match_matrix = (labels_one_hot.unsqueeze(2) & outputs_one_hot).long()
        
        self.scores += match_matrix.sum(dim=0)
        self.samples_per_class += labels_one_hot.sum(dim=0)
            
    def reset(self):
        self.scores = torch.zeros(self.num_classes, self.top_k)
        self.samples_per_class = torch.zeros(self.num_classes)
    
    def compute(self):
        weighted_scores = (self.scores * self.weights).sum(dim=1) / self.samples_per_class
        return weighted_scores.mean()
    
    def to(self, device: torch.device):
        self.scores = self.scores.to(device)
        self.weights = self.weights.to(device)
        self.samples_per_class = self.samples_per_class.to(device)
        return self

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
        self.top_1_accuracy.to(device),
        self.top_k_accuracy.to(device),
        self.mca.to(device),
        self.weighted_top_k_mca.to(device),
        self.confusion_matrix.to(device)
        return self

    @staticmethod
    def from_metrics(num_classes, top_k, *metrics) -> "Metrics":
        new_metrics = Metrics(num_classes, top_k)
        new_metrics.top_1_accuracy = metrics[0]
        new_metrics.top_k_accuracy = metrics[1]
        new_metrics.mca = metrics[2]
        new_metrics.weighted_top_k_mca = metrics[3]
        new_metrics.confusion_matrix = metrics[4]

        return new_metrics
    

if __name__ == "__main__":
    
    good = WeightedTopKMCA(5, 3)
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
    
    good.update(outputs1, labels1)
    print(good.compute())
    good.update(outputs2, labels2)
    result_good = good.compute()
    
    #print(good.scores)
    
    # mca.update(outputs1, labels1)
    # mca_result = mca.compute().mean().item()
    
    # top2_mca.update(outputs1, labels1)
    # top2_result = top2_mca.compute().mean().item()
    
    # top3_mca.update(outputs1, labels1)
    # top3_result = top3_mca.compute().mean().item()
    
    # print(result_good, mca_result, top2_result, top3_result)
    
    print(result_good)