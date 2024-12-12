import matplotlib.pyplot as plt

def plot_metric(values, labels, name):
    
    plt.figure()
    for val, label in zip(values, labels):
        plt.plot(val, label=label)
        plt.ylabel(name)
        plt.title(f"{name} vs. epochs")
    plt.legend()