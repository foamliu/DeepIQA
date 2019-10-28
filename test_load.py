import time

import torch

from mobilenet_v2 import MobileNetV2

filename = 'image_classification_distilled.pt'

print('loading {}...'.format(filename))
start = time.time()
model = MobileNetV2()
model.load_state_dict(torch.load(filename))
print('elapsed {} sec'.format(time.time() - start))
