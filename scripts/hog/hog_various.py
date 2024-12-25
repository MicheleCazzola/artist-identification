import json
import time
import numpy as np
from skimage.feature import hog
import torch

def apply_hog(
    img_dim: int,
    orientations: int, 
    pixels_per_cell: int,
    cells_per_block: int,
    transform_sqrt: bool,
    num_iterations: int,
    log_interval: int,
    multichannel: bool = False
) -> torch.Tensor:
    
    FC_LAYER = 2048
    
    image = torch.rand(img_dim, img_dim) if not multichannel else torch.rand(3, img_dim, img_dim).numpy().transpose(1, 2, 0)
    
    start = time.time()
    for i in range(num_iterations):
        features: np.ndarray = hog(
            image, 
            orientations=orientations, 
            pixels_per_cell=(pixels_per_cell, pixels_per_cell), 
            cells_per_block=(cells_per_block, cells_per_block),
            block_norm='L2-Hys',
            transform_sqrt=transform_sqrt,
            feature_vector=False,
            channel_axis=2 if multichannel else None
        )
        
        if (i+1) % log_interval == 0:
            print(f"Iteration {i+1}/{num_iterations}")
            
    elapsed = time.time() - start
    
    overweight = 100 * features.size / FC_LAYER 
    
    return features, overweight, 1000 * elapsed / num_iterations

if __name__ == "__main__":
    
    NUM_ITERATIONS = 1000
    LOG_INTERVAL = 100
    OUTFILE = "./scripts/hog/hog_stats.json"
    
    CONFIGS = [
        {
            "img_dim": 512,
            "orientations": 6,
            "pixels_per_cell": 16,
            "cells_per_block": 2,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 256,
            "orientations": 6,
            "pixels_per_cell": 16,
            "cells_per_block": 2,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 512,
            "orientations": 9,
            "pixels_per_cell": 512 // 3,
            "cells_per_block": 2,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 256,
            "orientations": 9,
            "pixels_per_cell": 256 // 3,
            "cells_per_block": 2,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },{
            "img_dim": 512,
            "orientations": 9,
            "pixels_per_cell": 512 // 3,
            "cells_per_block": 1,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 256,
            "orientations": 9,
            "pixels_per_cell": 256 // 3,
            "cells_per_block": 1,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 224,
            "orientations": 6,
            "pixels_per_cell": 16,
            "cells_per_block": 2,
            "transform_sqrt": False,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 224,
            "orientations": 6,
            "pixels_per_cell": 16,
            "cells_per_block": 2,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 224,
            "orientations": 9,
            "pixels_per_cell": 224 // 3,
            "cells_per_block": 1,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL
        },
        {
            "img_dim": 224,
            "orientations": 9,
            "pixels_per_cell": 224 // 3,
            "cells_per_block": 1,
            "transform_sqrt": True,
            "num_iterations": NUM_ITERATIONS,
            "log_interval": LOG_INTERVAL,
            "multichannel": True
        }
    ]
    
    features_list, overweight_list, elapsed_list = [], [], []
    for config in CONFIGS:
        
        print(f"Configuration: {config}")
        
        features, overweight, elapsed = apply_hog(**config)
        
        expected_size = (config["img_dim"] // config["pixels_per_cell"] - config["cells_per_block"] + 1)**2 * config["orientations"] * config["cells_per_block"]**2
        
        assert features.size == expected_size, f"Feature size mismatch: {features.shape} -> {features.size} != {expected_size}"
        
        features_list.append(features)
        overweight_list.append(overweight)
        elapsed_list.append(elapsed)
        
    for i, config in enumerate(CONFIGS):
        del config["num_iterations"]
        del config["log_interval"]
        
        config["num_features"] = features_list[i].size
        config["overweight"] = overweight_list[i]
        config["elapsed"] = elapsed_list[i]
        
    json.dump(CONFIGS, open(OUTFILE, mode="w", encoding="utf-8"), indent=4)
