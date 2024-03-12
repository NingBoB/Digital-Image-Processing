# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 13:42
# @Author  : Mean
# @File    : session1.py
# @Description:
import cv2
import numpy as np

image = cv2.imread('./test2.png', cv2.IMREAD_GRAYSCALE)
image_resize = cv2.resize(image, (64, 64))
out = []
# 00 01 11 10 20 21 22 12 02
# 获取行程
for i in range(64):
    for j in range(2 * (i + 1) - 1):
        if i % 2 == 0:
            if j <= i:
                out.append(image[i][j])
            elif j > i:
                out.append(image[i - (j - i)][i])
        else:
            if j <= i:
                out.append(image[j][i])
            elif j > i:
                out.append(image[i][i - (j - i)])
count = 1
image_res = []
data = []
# 判断当前是否和后一项相同，相同则count增加
for i in range(len(out) - 1):
    if count == 1:
        image_res.append(out[i])
    if out[i] == out[i + 1]:
        count += 1
        if i == len(out) - 2:
            image_res.append(out[i])
            data.append(count)
    else:
        data.append(count)
        count = 1
# 处理最后一个
if out[len(out) - 2] != out[-1]:
    data.append(1)
    image_res.append(out[-1])

# 压缩比
ys_rate = len(out)/len(image_res)
print('压缩比为' + str(ys_rate))


