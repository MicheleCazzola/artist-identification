import json
from statistics import mean
from matplotlib import pyplot as plt
import torch
from src.model.network import MultiBranchArtistNetwork
from src.utils.utils import BackboneType, execution_time
from src.config.config import HOGConfig

@execution_time
def call_model(x):
    return model(x)


@torch.no_grad()
def compute_latency(model: torch.nn.Module, dataset, device, log_frequency):
    latency = []
    model.eval()
    for step, x in enumerate(dataset):
        x = x.to(device)
        out = call_model(x)
        latency.append(call_model.time)
        
        if (step + 1) % log_frequency == 0:
            print(f"Step {step + 1} / {len(dataset)}")
        
    return mean(latency) * 1000     # latency in ms

OUTFILE = "./scripts/resources/resources_prova.json"
OUTFILE_PLOT = "./scripts/resources/accuracy_vs_latency_prova.png"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DATASET_SIZE = 1000
NUM_CLASSES = 161
BACKBONES = list(BackboneType) + [None]
HANDCRAFTED_FLAGS = [False, True]

model_names = [
    name
    for backbone in BACKBONES
    for name in ([f"{backbone.value}_no_hcrf", f"{backbone.value}_hcrf"] if backbone is not None else ["rnd_no_hcrf", "rnd_hcrf"])
]

model_variants = [
    MultiBranchArtistNetwork(
        num_classes=NUM_CLASSES,
        stn=backbone,
        use_handcrafted=handcrafted,
        hog_params=HOGConfig()
    ).to(DEVICE)
    for backbone in BACKBONES
    for handcrafted in HANDCRAFTED_FLAGS
]

top1_acc_imagenet = {
    BackboneType.RESNET18: 69.76,
    BackboneType.MOBILENET_V3_SMALL: 67.7,
    BackboneType.EFFICIENTNET_B0: 76.3,
    BackboneType.REGNET_X_400MF: 77.6,
    BackboneType.SHUFFLENET_V2_X0_5: 60.3,
    BackboneType.MNASNET0_5: 68.9,
    None: 0.1
}

models = dict(zip(model_names, model_variants))
# _ = [print(name, model) for name, (_, model) in zip(MODEL_NAMES, model_variants)]
# models = dict(zip(MODEL_NAMES, [m[0] for m in model_variants]))

dataset = [torch.randn(1, 3, 512, 512) for _ in range(DATASET_SIZE)]

model_stats = {}
for (name, model) in models.items():
    
    print(f"Running model: {name}")
    
    num_params = sum(p.numel() for p in model.parameters())
    memory_size = num_params * 4
    latency = compute_latency(model, dataset, DEVICE, DATASET_SIZE // 10)
    fps = 1000 / latency
    
    model_stats[name] = {
        "params": f"{num_params / 1024 ** 2:.2f} M",
        "size": f"{memory_size / 1024 ** 2:.2f} MB",
        "latency": f"{latency:.2f} ms",
        "fps": f"{fps:.2f} fps",
        "accuracy": top1_acc_imagenet[model.roi_extractor.stn]
    }

with open(OUTFILE, "w") as f:
    json.dump(model_stats, f, indent=4)
    
fig = plt.figure(figsize=(16,8))
plt.subplots_adjust(left=0.05, right=0.75)  # Adjust the subplot to remove left margin and make space for legend

names, acc, lat = zip(*[(name, stats["accuracy"], float(stats["latency"].split()[0])) for (name, stats) in model_stats.items()])
colors = plt.cm.tab20.colors  # Use a colormap with enough distinct colors
color_map = {name: colors[i % len(colors)] for i, name in enumerate(names)}

for name, latency, accuracy in zip(names, lat, acc):
    plt.scatter(latency, accuracy, color=color_map[name], label=name)

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))

plt.legend(by_label.values(), by_label.keys(), loc='center left', bbox_to_anchor=(1, 0.5))

plt.grid()
plt.xlabel("Latency (ms)")
plt.ylabel("Top-1 Accuracy on ImageNet (%)")
plt.title("Top-1 Accuracy vs Latency")


plt.savefig(OUTFILE_PLOT)