# -*- coding: utf-8 -*-
# @Time    : 2023/11/21 20:46
# @Author  : Mean
# @File    : session4.py
# @Description: 三种滤波对比
import cv2


def bi_demo(image):  # 高斯双边滤波
    dst = cv2.bilateralFilter(src=image, d=0, sigmaColor=100, sigmaSpace=15)
    cv2.namedWindow('bi_demo', 0)
    cv2.imshow("bi_demo", dst)


def median_blur_demo(image):  # 中值滤波
    dst = cv2.medianBlur(image, 3)
    cv2.namedWindow('median_blur image', 0)
    cv2.imshow("median_blur image", dst)


def blur_demo(image):  # 均值滤波
    dst = cv2.blur(image, (3, 3))
    cv2.namedWindow('blur image', 0)
    cv2.imshow("blur image", dst)


src = cv2.imread('../test/test_pic/gs_noise.jpg', 0)
# bi_demo(src)
blur_demo(src)
median_blur_demo(src)
# cv2.namedWindow('src', 0)
# cv2.imshow('src', src)
cv2.waitKey(0)
