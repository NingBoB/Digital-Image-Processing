# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 12:36
# @Author  : Mean
# @File    : cv2line.py
# @Description: cv2绘制直线
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, [(0, 0), (200, 200)], [(511, 511), (0, 400)], (0, 0, 255), 2)

cv2.imshow("example", img)
cv2.waitKey(0)
