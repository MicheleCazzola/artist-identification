from enum import Enum

class BackboneType(str, Enum):
    RESNET18 = "resnet18"
    MOBILENET_V3_SMALL = "mobilenet_v3_small"
    EFFICIENTNET_B0 = "efficientnet_b0"
    REGNET_X_400MF = "regnet_x_400mf"
    SHUFFLENET_V2_X0_5 = "shufflenet_v2_x0_5"
    MNASNET0_5 = "mnasnet0_5"