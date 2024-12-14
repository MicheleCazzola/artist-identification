import json
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from src.config import Config
from src.train import EvaluationResult, TrainingResult

def save_plot_result(values: list, labels: list, name: str, save_path: str) -> Figure:
    
    f = plt.figure(name)
    for val, label in zip(values, labels):
        plt.plot(val, label=label)
        plt.title(f"{name} vs. epochs")
    
    plt.xticks(ticks=range(len(values)+1), labels=range(1, len(values)+2))
    plt.xlabel("Epochs")
    plt.ylabel(name)
    plt.grid()
    plt.legend()
    plt.xlim(0, len(values)+0.2)
    
    if name.lower().startswith("acc"):
        plt.ylim(0,1.1)
        
    f.savefig(f"{save_path}/{name.lower()}.png")
    

def save_config_results(config: Config, train_result: TrainingResult, test_result: EvaluationResult, save_path: str):
    
    result = config.__dict__.copy()
    result.update(train_result.__dict__)
    result.update(test_result.__dict__)
    
    with open(f"{save_path}/config.json", "w") as f:
        json.dump(result, f, indent=4)