from enum import Enum
import json
import time
from functools import wraps
import torch
import random
import numpy as np

class BackboneType(str, Enum):
    RESNET18 = "resnet18"
    MOBILENET_V3_SMALL = "mobilenet_v3_small"
    EFFICIENTNET_B0 = "efficientnet_b0"
    REGNET_X_400MF = "regnet_x_400mf"
    SHUFFLENET_V2_X0_5 = "shufflenet_v2_x0_5"
    MNASNET0_5 = "mnasnet0_5"
    

class Env(str, Enum):
    CUDA = "cuda"
    CPU = "cpu"
    

def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if torch.cuda.is_available():
            start_event = torch.cuda.Event(enable_timing=True)
            end_event = torch.cuda.Event(enable_timing=True)
            
            start_event.record()
            result = func(*args, **kwargs)
            end_event.record()
            
            torch.cuda.synchronize()
            
            # Time in ms
            wrapper.time = start_event.elapsed_time(end_event) / 1000
        else:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            wrapper.time = end_time - start_time
            
        return result
        
    return wrapper

def load_stats(filename: str) -> tuple:
    
    stats = json.load(open(filename, "r"))
    
    return stats["mean"], stats["std"]

def init_seed(seed: int) -> tuple[callable, torch.Generator]:
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    
    torch.use_deterministic_algorithms(True, warn_only=True)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    def seed_worker(_):
        worker_seed = torch.initial_seed() % 2**32
        np.random.seed(worker_seed)
        random.seed(worker_seed)

    g = torch.Generator()
    g.manual_seed(seed)
    
    return seed_worker, g