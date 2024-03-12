# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 15:44
# @Author  : Mean
# @File    : session2.py
# @Description:
import cv2
import numpy as np

image = cv2.imread('./test2.png', cv2.IMREAD_GRAYSCALE)
image_resize = cv2.resize(image, (64, 64))

out = []
# 00 01 10 20 11 02 03 12 21 30
for i in range(127):
    for j in range(i + 1):
        if i % 2 != 0 and j < 64 and i - j < 64:
            out.append(image_resize[j][i - j])
        elif i % 2 == 0 and j < 64 and i - j < 64:
            out.append(image_resize[i - j][j])

count = 1
image_res = []
data = []
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
print()
ys_rate = len(out)/len(image_res)
print('压缩比为' + str(ys_rate) + '%')
