# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 13:28
# @Author  : Mean
# @File    : session5.py
# @Description:
import numpy as np
from scipy.fft import fft2, ifft2
from PIL import Image
import matplotlib.pyplot as plt


def quantize_and_encode(coefficients, quantization_factor):
    quantized_coefficients = np.round(coefficients / quantization_factor).astype(int)

    flattened_coefficients = quantized_coefficients.flatten()

    encoded_data = []
    current_run = [flattened_coefficients[0], 1]

    for coefficient in flattened_coefficients[1:]:
        if coefficient == current_run[0]:
            current_run[1] += 1
        else:
            encoded_data.append(tuple(current_run))
            current_run = [coefficient, 1]

    encoded_data.append(tuple(current_run))

    return encoded_data


def calculate_compression_rate(original_size, compressed_size):
    return (original_size - compressed_size) / original_size


# 加载灰度图像
image_path = "BaboonRGB.tif"
gray_image = Image.open(image_path).convert("L")
image_array = np.array(gray_image)

# 进行傅里叶变换
dft_coefficients = fft2(image_array)

# 量化并且进行行程编码
quantization_factor = 10
encoded_data = quantize_and_encode(dft_coefficients.real, quantization_factor)

# 原始尺寸
original_size = image_array.size * 8  # 8 bits per pixel for a grayscale image

# 压缩尺寸
compressed_size = len(encoded_data) * (1 + 8)  # Assuming 1 bit for value and 8 bits for length

# 压缩率计算
compression_rate = calculate_compression_rate(original_size, compressed_size)

# 结果
print(f"Original Size: {original_size} bits")
print(f"Compressed Size: {compressed_size} bits")
print(f"Compression Rate: {compression_rate * 100:.2f}%")
