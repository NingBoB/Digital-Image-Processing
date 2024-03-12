# -*- coding: utf-8 -*-
# @Time    : 2023/12/10 10:13
# @Author  : Mean
# @File    : session1.py
# @Description:
# 离散余弦变换，并获取其幅频谱
import cv2
import numpy as np
import matplotlib.pyplot as plt


# 理想低通滤波器
def ideal_lowpass_filter(shape, cutoff_frequency):
    rows, cols = shape
    center_row, center_col = rows // 2, cols // 2
    filter_mask = np.zeros((rows, cols), np.float32)
    distance_mask = np.zeros((rows, cols), np.float32)
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - center_row) ** 2 + (j - center_col) ** 2)
            distance_mask[i][j] = distance
            if distance <= cutoff_frequency:
                filter_mask[i, j] = 1.0
    return filter_mask


# 设定门限频率
s = 330

image = cv2.imread('Lena.tif', cv2.IMREAD_GRAYSCALE)
# image = image[0:128, 0:128]
# DCT与iDCT
img_dct = cv2.dct(np.float32(image))
mask = ideal_lowpass_filter(img_dct.shape, s)
img_dct_after_filter = img_dct * mask


img_dct_log = 20 * np.log(abs(img_dct))
# 逆离散余弦变换，变换图像回至空间域
img_back = cv2.idct(img_dct_after_filter)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(1, 3, 2)
plt.imshow(img_dct_after_filter, cmap='gray')
plt.title('Dct Image')
plt.subplot(1, 3, 3)
plt.imshow(img_back, cmap='gray')
plt.title('iDct Image')
plt.show()
