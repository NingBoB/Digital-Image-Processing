# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 15:11
# @Author  : Mean
# @File    : session3.py
# @Description: Hough线检测
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
image = cv2.imread('../test/test_pic/cizhuan.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 转为灰度图像
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
# 使用Canny边缘检测
edges = cv2.Canny(gray, 50, 200, apertureSize=3)
# cv2.imshow('canny', edges)
# cv2.waitKey(0)

# 使用霍夫直线变换
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=10, maxLineGap=50)

# 绘制边缘和检测到的直线
line_image = np.zeros_like(image_rgb)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# 将直线图叠加到原始图像
result = cv2.addWeighted(image_rgb, 0.8, line_image, 1, 0)

# 绘制结果
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)  # 将图片排成一行两列，该图在1
plt.imshow(image_rgb)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(result)
plt.title('Hough Transform for Long Edges')

plt.show()

