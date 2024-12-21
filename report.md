# Report dei test svolti

## Normale, con 5 epoche
Obbiettivo: valutare prestazioni di diverse reti

### EFFICIETNET + HOG
- Batch size = 8
- Ram = 10.5 GB
- Time = 52 minutes

### REGNET_X_400MF + HOG
- Batch size = 16
- Ram = 10.2 GB
- Time = 42 minutes

### MOBILENET_V3_SMALL + HOG
- Batch size = 16
- Ram = 8.7 GB
- Time = 35 minutes

### MOBILENET_V3_SMALL + HOG
- Batch size = 24
- Ram = 12.8 GB
- Time = 33 minutes

### SHUFFLENET_V2_X0_5 + HOG
- Batch size = 16
- Ram = 7.8 GB
- Time = 35 minutes

### SHUFFLENET_V2_X0_5 + HOG
- Batch size = 24
- Ram = 11.5 GB
- Time = 32 minutes

### RESNET_18 + HOG
- Batch size = 16 
- Ram = 10 GB
- Time = 42 minutes


### RESNET_18
- Batch size = 16
- Ram = 10 GB
- Time = 27 minutes

### MNASNET0_5 + HOG
- Batch size = 16
- Ram = 10 GB
- Time = 38 minutes

### RANDOM + HOG
- Batch size = 32
- Ram = 12 GB
- Time ~ 30 minutes

## OVERFITTING
Obbiettivo: assicurarsi che la rete riesca ad overfittare su un piccolo sample


### RESNET_18 + HOG
- pretrained = True
- reduce_factor = 0.04
- batch size = 16
- num epochs = 55
- lr = 1e-3
- scheduler_step_size: int = 30
- scheduler_gamma: float = 0.2
- train_accuracy: bool = True
- backbone_type: BackboneType = None
- Time = 60 minutes
- Loss = 0.3
- Accuracy = 98.8%

### RANDOM + HOG
- pretrained = False
- reduce_factor = 0.04
- batch size = 32
- num epochs = 80
- lr = 1e-3
- scheduler_step_size: int = 10
- scheduler_gamma: float = 0.5
- train_accuracy: bool = True
- backbone_type: BackboneType = None
- Time = 60 minutes
- Loss = 0.78
- Accuracy = 92.7%

### RANDOM 
- pretrained = False
- reduce_factor = 0.08
- batch size = 32
- num epochs = 50
- log_frequency = 50
- lr = 5e-3
- scheduler_step_size: int = 40
- scheduler_gamma: float = 0.2
- train_accuracy: bool = True
- backbone_type: BackboneType = None
- use_handcrafted: bool = False
- Time = 1h 3 minutes
- Loss = 0.19
- Accuracy = 98.9%

### SHUFFLENET_V2_X0_5 + HOG -> verifica
- pretrained = True
- reduce_factor = 0.04
- batch size = 24
- num epochs = 60
- lr = 1e-2
- scheduler_step_size: int = 10
- scheduler_gamma: float = 0.5
- train_accuracy: bool = 96.4%
- backbone_type: BackboneType = None
- Time = 57 minutes
- Loss = 0.67
- Accuracy = 96.4%

## VALIDATION LOSS
Trovare un learning rate alto che faccia andare giù la loss subito

### RANDOM + HOG 
- config_20241220-220603.json
- pretrained = False
- reduce_factor: float = None -> 1
- batch size = 32
- num epochs = 3
- log_frequency = 50
- lr = 5e-2 -> per far scendere la loss 
- weight_decay -> 1e-6 -> per regolarizzare un minimo per evitare che validation loss si stacchi subito da training loss
- scheduler_step_size: int = 20 -> per non usarlo
- train_accuracy: bool = False -> perchè non stiamo overfittando ma validation loss
- backbone_type: BackboneType = None
- use_handcrafted: bool = True

### RANDOM + HOG 
- config_20241220-230830.json
- pretrained = False
- reduce_factor: float = None -> 1
- batch size = 32
- num epochs = 3
- log_frequency = 25
- lr = 1e-3 -> per far scendere la loss 
- weight_decay -> 1e-6 -> per regolarizzare un minimo per evitare che validation loss si stacchi subito da training loss
- scheduler_step_size: int = 20 -> per non usarlo
- train_accuracy: bool = False -> perchè non stiamo overfittando ma validation loss
- backbone_type: BackboneType = None
- use_handcrafted: bool = True
- Validation loss: 5.1 --> 4.27
- Validation accuracy: 0.129

### RANDOM 
- config_20241220-233758.json
- pretrained = False
- reduce_factor: float = None -> 1
- batch size = 32
- num epochs = 3
- log_frequency = 25
- lr = 1e-3 -> per far scendere la loss 
- weight_decay -> 1e-6 -> per regolarizzare un minimo per evitare che validation loss si stacchi subito da training loss
- scheduler_step_size: int = 20 -> per non usarlo
- train_accuracy: bool = False -> perchè non stiamo overfittando ma validation loss
- backbone_type: BackboneType = None
- use_handcrafted: bool = False
- Validation loss: 5.1 --> 4.27
- Validation accuracy: 0.129

