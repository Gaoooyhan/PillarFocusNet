# Copyright (c) OpenMMLab. All rights reserved.
from .pillar_encoder import DynamicPillarFeatureNet, PillarFeatureNet
from .voxel_encoder import (DynamicSimpleVFE, DynamicVFE, HardSimpleVFE,
                            HardVFE, SegVFE)
#from .pillar_encoder_new import DynamicPillarFeatureNet_NEW, PillarFeatureNet_NEW
from .pillar_encoder_new2 import DynamicPillarFeatureNet_NEW2, PillarFeatureNet_NEW2
from .pillar_encoder_new3 import DynamicPillarFeatureNet_NEW3, PillarFeatureNet_NEW3
from .pillar_encoder_new4 import DynamicPillarFeatureNet_NEW4, PillarFeatureNet_NEW4
from .pillar_encoder_new5 import DynamicPillarFeatureNet_NEW5, PillarFeatureNet_NEW5

__all__ = [
     'HardVFE', 'DynamicVFE','PillarFeatureNet', 'DynamicPillarFeatureNet',
    'HardSimpleVFE', 'DynamicSimpleVFE', 'SegVFE',  'PillarFeatureNet_NEW2', 'DynamicPillarFeatureNet_NEW2',
    'DynamicPillarFeatureNet_NEW3', 'PillarFeatureNet_NEW3',  'PillarFeatureNet_NEW4', 'DynamicPillarFeatureNet_NEW4',
    'PillarFeatureNet_NEW5', 'DynamicPillarFeatureNet_NEW5'
]
#'PillarFeatureNet', 'DynamicPillarFeatureNet',