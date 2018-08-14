# -*- coding:utf-8 -*-
import numpy as np
detection_file='/home/liuyp/liu/mot/deep_sort/resources/detections/MOT16_POI_test/MOT16-07.npy'
sda=np.load(detection_file)
print(sda[:, 0].max())