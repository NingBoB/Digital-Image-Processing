# -*- coding: utf-8 -*-
# @Time    : 2023/11/27 14:02
# @Author  : Mean
# @File    : sobel_cv2_polyfit.py
# @Description:
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像并转为灰度
image = cv2.imread('./test_pic/macaw.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用Sobel算子进行边缘检测
edges_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
edges_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
edges = np.sqrt(edges_x**2 + edges_y**2)
cv2.imshow('sobel1',edges)

# 阈值处理得到二值图像
threshold = 50
edges[edges < threshold] = 0
edges[edges >= threshold] = 255
cv2.imshow('sobel2',edges)
cv2.waitKey(0)

# 获取边缘点的坐标
edge_points = np.column_stack(np.where(edges > 0))

# 使用最小二乘法拟合直线
coefficients = np.polyfit(edge_points[:, 0], edge_points[:, 1], 1)
slope, intercept = coefficients

# 绘制结果
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
x_vals = np.arange(0, edges.shape[1])
y_vals = slope * x_vals + intercept
plt.plot(x_vals, y_vals, color='red', label='Fitted Line')
plt.scatter(edge_points[:, 1], edge_points[:, 0], s=5, color='blue', label='Edge Points')
plt.legend()
plt.title('Sobel Edges and Fitted Line')

plt.show()