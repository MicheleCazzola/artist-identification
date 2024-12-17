import json
from statistics import mean
import time
import torch
from src.network import MultiBranchArtistNetwork, BackboneType


@torch.no_grad()
def compute_latency(model: torch.nn.Module, dataset, device):
    latency = []
    model.eval()
    for step, x in enumerate(dataset):
        x = x.to(device)
        start = time.time()
        out = model(x)
        end = time.time()
        latency.append(end - start)
        
        if (step + 1) % 20 == 0:
            print(f"Step {step + 1} / {len(dataset)}")
        
    return mean(latency) * 1000     # latency in ms

OUTFILE = "./scripts/resources/resources.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
DATASET_SIZE = 10
NUM_CLASSES = 161
BACKBONES = list(BackboneType) + [None]
HANDCRAFTED_FLAGS = [False, True]

model_names = [
    name
    for backbone in BACKBONES
    for name in ([f"{backbone.value}_no_hcrf", f"{backbone.value}_hcrf"] if backbone is not None else ["model_rnd_no_hcrf", "model_rnd_hcrf"])
]

model_variants = [
    MultiBranchArtistNetwork(num_classes=NUM_CLASSES, stn=backbone, use_handcrafted=handcrafted).to(DEVICE)
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
    None: None
}

models = dict(zip(model_names, model_variants))
# _ = [print(name, model) for name, (_, model) in zip(MODEL_NAMES, model_variants)]
# models = dict(zip(MODEL_NAMES, [m[0] for m in model_variants]))

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
        "fps": f"{fps:.2f} fps",
        "accuracy": top1_acc_imagenet.get(model.roi_extractor.stn, "None")
    }

with open(OUTFILE, "w") as f:
    json.dump(model_stats, f, indent=4)