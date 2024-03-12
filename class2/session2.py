# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 14:15
# @Author  : Mean
# @File    : session2.py
# @Description: 使用最小二乘法拟合直线

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 实现sobel算子分割
img = cv2.imread('BaboonRGB.tif', cv2.IMREAD_GRAYSCALE)
h, w = img.shape
new_img = np.zeros([h, w])
x_img = np.zeros(img.shape)
y_img = np.zeros(img.shape)
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
# 计算x和y方向上的梯度
for i in range(h - 2):
    for j in range(w - 2):
        x_img[i + 1, j + 1] = abs(np.sum(img[i: i + 3, j: j + 3] * sobel_x))
        y_img[i + 1, j + 1] = abs(np.sum(img[i: i + 3, j: j + 3] * sobel_y))
new_img = np.sqrt(x_img**2+y_img**2)

# 获取边缘点的坐标
edge_points = np.column_stack(np.where(new_img > 0))    # column_stack组合坐标
# 最小二乘拟合直线 polyfit用于拟合，使用的就是最小二乘法
coefficients = np.polyfit(edge_points[:, 0], edge_points[:, 1], 1)
slope, intercept = coefficients

# 绘制
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(new_img, cmap='gray')
x_vals = np.arange(0, new_img.shape[1])
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color='red', label='Fitted Line')
plt.scatter(edge_points[:, 1], edge_points[:, 0], s=5, color='blue', label='Edge Points')
plt.legend()
plt.title('Sobel Edges and Fitted Line')

plt.show()

# cv2.imshow('sobel1', new_img)
# cv2.imshow('sobel2', np.uint8(new_img))
# threshold = 50
# new_img[new_img < threshold] = 0
# new_img[new_img >= threshold] = 255
# cv2.imshow('sobel3', new_img)
#
# cv2.waitKey(0)
