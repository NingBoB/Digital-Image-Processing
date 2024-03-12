# -*- coding: utf-8 -*-
# @Time    : 2023/12/27 13:42
# @Author  : Mean
# @File    : session6.py
# @Description:
import numpy as np
from scipy.fft import fft2, ifft2
from PIL import Image
import matplotlib.pyplot as plt

def quantize(coefficients, quantization_factor):
    return np.round(coefficients / quantization_factor)

def dequantize(quantized_coefficients, quantization_factor):
    return quantized_coefficients * quantization_factor

# 加载灰度图像
image_path = "Lena.tif"
gray_image = Image.open(image_path).convert("L")
image_array = np.array(gray_image)

# 进行DFT
dft_coefficients = fft2(image_array)

# 量化DFT
quantization_factor = 10
quantized_coefficients = quantize(dft_coefficients, quantization_factor)

# 逆运算
dequantized_coefficients = dequantize(quantized_coefficients, quantization_factor)
reconstructed_image = np.abs(ifft2(dequantized_coefficients)).astype(np.uint8)

# 展示
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap='gray')
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(reconstructed_image, cmap='gray')
plt.title("Reconstructed Image")

plt.show()
