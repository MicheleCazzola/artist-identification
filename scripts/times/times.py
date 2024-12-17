from statistics import mean
import time
import torch
from src.multi_branch_nn_simpler import DeepMultibranchNetwork

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model_stn_r18_hcrf = DeepMultibranchNetwork(num_classes=161, use_stn=True, use_handcrafted=True)
model_rnd_hcrf = DeepMultibranchNetwork(num_classes=161, use_stn=False, use_handcrafted=True)
model_stn_r18_no_hcrf = DeepMultibranchNetwork(num_classes=161, use_stn=True, use_handcrafted=False)
model_rnd_no_hcrf = DeepMultibranchNetwork(num_classes=161, use_stn=False, use_handcrafted=False)

models = {
    "model_stn_r18_hcrf": model_stn_r18_hcrf.to(device),
    "model_rnd_hcrf": model_rnd_hcrf.to(device),
    "model_stn_r18_no_hcrf": model_stn_r18_no_hcrf.to(device),
    "model_rnd_no_hcrf": model_rnd_no_hcrf.to(device)
}

@torch.no_grad()
def compute_latency(model, dataset):
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


model_latencies = {}
for (name, model) in models.items():
    
    print(f"Running model: {name}")
    
    dataset = [torch.randn(1, 3, 512, 512) for _ in range(120)]
    model_latencies[name] = compute_latency(model, dataset)

print(model_latencies)