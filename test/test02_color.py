# -*- coding: utf-8 -*-
# @Time    : 2023/11/6 15:04
# @Author  : Mean
# @File    : test02_color.py
# @Description: 三通道提取
import cv2 as cv

# 读取图片
image = cv.imread("../class1/pheasant.jpg")

Red = cv.split(image)[0]

# RGB3个通道的提取   提取R、G、B分量，opencv读取顺序是BGR
cv.imshow("Blue", image[:, :, 0])
cv.imshow("Green", image[:, :, 1])
cv.imshow("Red", image[:, :, 2])
cv.waitKey(0)
