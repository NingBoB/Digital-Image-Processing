# -*- coding: utf-8 -*-
# @Time    : 2023/11/19 23:58
# @Author  : Mean
# @File    : session2.py
# @Description: 图像的平滑滤波
import cv2
import numpy as np
from matplotlib import pyplot as plt


# 计算中心距离
def get_C(sigmad, n):
    C = np.zeros((n, n))
    x = np.array([n // 2, n // 2])
    for i in range(n):
        for j in range(n):
            ksi = np.array([i, j])
            C[i, j] = np.exp(-0.5 * (np.linalg.norm(ksi - x) / sigmad) ** 2)
    C /= C.sum()
    return C

# 计算灰度距离
def get_S(f, sigmar, n):
    S = np.zeros((n, n))
    f = np.float64(f)
    S = np.exp(-0.5 * ((f - f[n // 2, n // 2]) / sigmar) ** 2)
    S /= S.sum()
    return S


# 导入图片
img = cv2.imread('../test/test_pic/salt-and-pepper_noise.png', 0)

sigmar = 50
sigmad = 3
n = 11

h, w = img.shape
img2 = np.zeros_like(img)

C = get_C(sigmad, n)

for i in range(h - n):
    for j in range(w - n):
        f = img[i:i + n, j:j + n]
        S = get_S(f, sigmar, n)
        K = C * S
        K /= K.sum()
        img2[i, j] = (f * K).sum()
plt.imshow(img)
plt.show()
plt.imshow(img2)
plt.show()
