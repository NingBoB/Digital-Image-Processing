# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 12:35
# @Author  : Mean
# @File    : session4.py
# @Description:
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# 将图片按位分为8个平面
def split_into_bitplanes(image_array, num_planes=8):
    bitplanes = [(image_array & (1 << i)) >> i for i in range(num_planes)]
    return np.array(bitplanes)

# 行程编码
def run_length_encode(bitplane):
    encoded_data = []
    current_run = [bitplane[0], 1]

    for bit in bitplane[1:]:
        if bit == current_run[0]:
            current_run[1] += 1
        else:
            encoded_data.append(tuple(current_run))
            current_run = [bit, 1]

    encoded_data.append(tuple(current_run))
    return encoded_data

def calculate_compression_rate(original_size, compressed_size):
    return (original_size - compressed_size) / original_size

# 加载灰度图片
image_path = "Lena.tif"
gray_image = Image.open(image_path).convert("L")
image_array = np.array(gray_image)

bitplanes = split_into_bitplanes(image_array, num_planes=8)

# 获取最高位平面，并编码
highest_bitplane = bitplanes[7].flatten()
encoded_data = run_length_encode(highest_bitplane)

# 创建子图展示每个位平面
plt.figure(figsize=(12, 6))
for i in range(8):
    plt.subplot(2, 4, i + 1)
    plt.imshow(bitplanes[i], cmap='gray')
    plt.title(f"Bit Plane {i}")

plt.tight_layout()
plt.show()

# 计算原始尺寸
original_size = image_array.size * 8

# 计算压缩后尺寸
compressed_size = len(encoded_data) * (1 + 8)

# 计算压缩率
compression_rate = calculate_compression_rate(original_size, compressed_size)

print(f"Original Size: {original_size} bits")
print(f"Compressed Size: {compressed_size} bits")
print(f"Compression Rate: {compression_rate * 100:.2f}%")
