# -*- coding: utf-8 -*-
# @Time    : 2023/12/10 16:41
# @Author  : Mean
# @File    : session2.py
# @Description:
import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('test1.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('test2.png', cv2.IMREAD_GRAYSCALE)

# 二维离散傅里叶变换
dft1 = np.fft.fft2(img1)
dft2 = np.fft.fft2(img2)

# 计算幅度谱和相位谱
magnitude_spectrum1 = np.log(1 + np.abs(dft1))
phase_spectrum1 = np.angle(dft1)
magnitude_spectrum2 = np.log(1 + np.abs(dft2))
phase_spectrum2 = np.angle(dft2)

# 显示结果
plt.subplot(221), plt.imshow(img1, cmap='gray')
plt.title('Img1'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum1, cmap='gray')
plt.title('Magnitude Spectrum 1'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img2, cmap='gray')
plt.title('Img2'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(magnitude_spectrum2, cmap='gray')
plt.title('Magnitude Spectrum 2'), plt.xticks([]), plt.yticks([])
plt.show()
