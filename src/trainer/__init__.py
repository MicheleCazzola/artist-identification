import torch
from .train import TrainingResult  # Adjust the import path as necessary

torch.serialization.add_safe_globals([TrainingResult])