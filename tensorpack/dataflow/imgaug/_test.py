# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
# -*- coding: utf-8 -*-
# File: _test.py


import sys
import cv2

from . import AugmentorList
from .crop import *
from .deform import *
from .imgproc import *
from .noise import SaltPepperNoise
from .noname import *

anchors = [(0.2, 0.2), (0.7, 0.2), (0.8, 0.8), (0.5, 0.5), (0.2, 0.5)]
augmentors = AugmentorList([
    Contrast((0.8, 1.2)),
    Flip(horiz=True),
    GaussianDeform(anchors, (360, 480), 0.2, randrange=20),
    # RandomCropRandomShape(0.3),
    SaltPepperNoise()
])

img = cv2.imread(sys.argv[1])
newimg, prms = augmentors._augment_return_params(img)
cv2.imshow(" ", newimg.astype('uint8'))
cv2.waitKey()

newimg = augmentors._augment(img, prms)
cv2.imshow(" ", newimg.astype('uint8'))
cv2.waitKey()
