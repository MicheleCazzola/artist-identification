from enum import Enum
import time
from functools import wraps

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
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        wrapper.time = end_time - start_time
        
    return wrapper