# -*- coding: utf-8 -*-
# @Time    : 2023/12/10 17:33
# @Author  : Mean
# @File    : session3.py
# @Description:
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('test1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('test2.png', cv2.IMREAD_GRAYSCALE)

# 平移矩阵
translation_matrix = np.float32([[1, 0, 0], [0, 1, 0]])  # 在x方向平移150个像素，y方向平移80个像素
# 旋转矩阵
rotation_matrix = cv2.getRotationMatrix2D((img1.shape[1] // 2, img1.shape[0] // 2), 10, 1)  # 逆时针旋转45度

# 平移变换
translated_image1 = cv2.warpAffine(img1, translation_matrix, (img1.shape[1], img1.shape[0]))
translated_image2 = cv2.warpAffine(img2, translation_matrix, (img2.shape[1], img2.shape[0]))
# 进行旋转变换
rotated_image1 = cv2.warpAffine(translated_image1, rotation_matrix, (img1.shape[1], img1.shape[0]))
rotated_image2 = cv2.warpAffine(translated_image2, rotation_matrix, (img2.shape[1], img2.shape[0]))

# 二维离散傅立叶变换
dft1 = np.fft.fft2(rotated_image1)
dft2 = np.fft.fft2(rotated_image2)

# 计算幅度谱和相位谱
magnitude1 = np.abs(dft1)
phase1 = np.angle(dft1)
magnitude2 = np.abs(dft2)
phase2 = np.angle(dft2)

# 显示幅度谱和相位谱
plt.subplot(221), plt.imshow(np.log(1 + magnitude1), cmap='gray')
plt.title('Magnitude Spectrum (Img 1)'), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(phase1, cmap='gray')
plt.title('Phase Spectrum (Img 1)'), plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(np.log(1 + magnitude2), cmap='gray')
plt.title('Magnitude Spectrum (Img 2)'), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(phase2, cmap='gray')
plt.title('Phase Spectrum (Img 2)'), plt.xticks([]), plt.yticks([])

plt.show()



