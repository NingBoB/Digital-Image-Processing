# -*- coding: utf-8 -*-
# @Time    : 2023/11/6 14:54
# @Author  : Mean
# @File    : test01_showimg.py
# @Description: 读取并显示图片
from skimage import exposure
import cv2 as cv

# 显示opencv版本
print(cv.getVersionString())

# 读取图片
image = cv.imread("test_pic/sifaka.jpg")

# 显示图片
cv.imshow('BaboonRGB', image)
cv.waitKey(0)
