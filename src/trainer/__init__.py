import torch
from .train import TrainingResult  # Adjust the import path as necessary

torch.serialization.add_safe_globals([TrainingResult])

if torch.backends.cudnn.is_available():
    torch.backends.cudnn.benchmark = False
    torch.backends.cudnn.deterministic = True