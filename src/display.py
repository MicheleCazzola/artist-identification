from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def plot_metric(values, labels, name: str) -> Figure:
    
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
        
    return f