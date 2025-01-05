from enum import Enum
import json
import time
from functools import wraps
import torch

class BackboneType(str, Enum):
    RESNET18 = "resnet18"
    MOBILENET_V3_SMALL = "mobilenet_v3_small"
    EFFICIENTNET_B0 = "efficientnet_b0"
    REGNET_X_400MF = "regnet_x_400mf"
    SHUFFLENET_V2_X0_5 = "shufflenet_v2_x0_5"
    MNASNET0_5 = "mnasnet0_5"
    

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