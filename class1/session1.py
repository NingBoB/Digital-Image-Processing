# -*- coding: utf-8 -*-
# @Time    : 2023/11/6 14:27
# @Author  : Mean
# @File    : session1.py
# @Description: 图像的对比度变换
import numpy as np
import cv2 as cv


def gamma(image, f):
    image = image / 255.0
    after = np.array(np.power(image, 1 / f) * 255, dtype=np.uint8)
    # after = np.power(image, 1/f)
    return after


# 读取图片
BaboonRGB = cv.imread("BaboonRGB.tif")
Pheasant = cv.imread("pheasant.jpg")
cv.imshow("BaboonRGB", BaboonRGB)
cv.imshow("Pheasant", Pheasant)

# 图片1
# gamma大于1---变亮
out = gamma(BaboonRGB, 2)
cv.imshow("BaboonRGB gamma=2", out)

# gamma小于1---变暗
out = gamma(BaboonRGB, 0.5)
cv.imshow("BaboonRGB gamma=0.5", out)

# 图片2
out = gamma(Pheasant, 2)
cv.imshow("Pheasant gamma=2", out)
out = gamma(Pheasant, 0.5)
cv.imshow("Pheasant gamma=0.5", out)

cv.waitKey(0)
