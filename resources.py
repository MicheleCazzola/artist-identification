import json
from statistics import mean
import time
import torch
from src.network import MultiBranchArtistNetwork, BackboneType


@torch.no_grad()
def compute_latency(model, dataset, device):
    latency = []
    for step, x in enumerate(dataset):
        start = time.time()
        x = x.to(device)
        out = model(x)
        end = time.time()
        latency.append(end - start)
        
        if (step + 1) % 40 == 0:
            print(f"Step {step + 1} / {len(dataset)}")
        
    return mean(latency) * 1000     # latency in ms

OUTFILE = "./scripts/resources/resources.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DATASET_SIZE = 10
NUM_CLASSES = 161
BACKBONES = [BackboneType.RESNET18, BackboneType.MOBILENET_V3_SMALL, None]
HANDCRAFTED_FLAGS = [False, True]

MODEL_NAMES = [
    "model_stn_resnet18_no_hcrf",
    "model_stn_resnet18_hcrf",
    "model_stn_mobilenetv3small_no_hcrf",
    "model_stn_mobilenetv3small_hcrf",
    "model_rnd_no_hcrf",
    "model_rnd_hcrf"
]

model_variants = [
    MultiBranchArtistNetwork(num_classes=NUM_CLASSES, stn=backbone, use_handcrafted=handcrafted)
    for backbone in BACKBONES
    for handcrafted in HANDCRAFTED_FLAGS
]

models = dict(zip(MODEL_NAMES, model_variants))

model_stats = {}
for (name, model) in models.items():
    
    print(f"Running model: {name}")
    
    dataset = [torch.randn(1, 3, 512, 512) for _ in range(DATASET_SIZE)]
    num_params = sum(p.numel() for p in model.parameters())
    memory_size = num_params * 4
    latency = compute_latency(model, dataset, DEVICE)
    fps = 1000 / latency
    
    model_stats[name] = {
        "params": f"{num_params / 1024 ** 2:.2f} M",
        "size": f"{memory_size / 1024 ** 2:.2f} MB",
        "latency": f"{latency:.2f} ms",
        "fps": f"{fps:.2f} fps"
    }

with open(OUTFILE, "w") as f:
    json.dump(model_stats, f, indent=4)