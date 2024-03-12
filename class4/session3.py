# -*- coding: utf-8 -*-
# @Time    : 2023/12/26 16:55
# @Author  : Mean
# @File    : session3.py
# @Description:

import heapq
import numpy as np
from PIL import Image

class HuffmanNode:
    def __init__(self, value=None, freq=None):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def resize_image(image_path, target_size):
    image = Image.open(image_path)
    resized_image = image.resize(target_size)
    return resized_image

def generate_huffman_tree(freq_dict):
    heap = [HuffmanNode(value=k, freq=v) for k, v in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged_node = HuffmanNode(freq=node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(heap, merged_node)

    return heap[0]

def generate_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node is not None:
        if node.value is not None:
            mapping[node.value] = code
        generate_huffman_codes(node.left, code + "0", mapping)
        generate_huffman_codes(node.right, code + "1", mapping)

    return mapping

def huffman_compress(data, mapping):
    compressed_data = "".join(mapping[char] for char in data)
    return compressed_data

def huffman_decompress(compressed_data, mapping):
    reverse_mapping = {code: char for char, code in mapping.items()}
    current_code = ""
    decompressed_data = ""

    for bit in compressed_data:
        current_code += bit
        if current_code in reverse_mapping:
            decompressed_data += reverse_mapping[current_code]
            current_code = ""

    return decompressed_data

def calculate_compression_rate(original_size, compressed_size):
    return (original_size - compressed_size) / original_size

def compress_and_analyze(image_path, block_size):
    # 图像预处理
    target_size = (64, 64)
    resized_image = resize_image(image_path, target_size)
    grayscale_image = resized_image.convert("L")
    image_array = np.array(grayscale_image)

    # 原始大小
    original_size = image_array.size * 8  # Assuming 8-bit per pixel

    # 将图片分块
    blocks = [image_array[i:i + block_size, j:j + block_size] for i in range(0, image_array.shape[0], block_size) for j in range(0, image_array.shape[1], block_size)]

    # 展开图像
    block_strings = ["".join(map(str, block.flatten())) for block in blocks]

    # 计算频率
    block_frequencies = [{char: block.count(char) for char in set(block)} for block in block_strings]

    # 为每个块生成哈夫曼数和编码
    block_huffman_trees = [generate_huffman_tree(freq_dict) for freq_dict in block_frequencies]
    block_huffman_mappings = [generate_huffman_codes(tree) for tree in block_huffman_trees]

    # 压缩并计算尺寸
    compressed_block_sizes = [len(huffman_compress(block_str, huffman_mapping)) for block_str, huffman_mapping in zip(block_strings, block_huffman_mappings)]

    # 计算总的压缩大小
    total_compressed_size = sum(compressed_block_sizes)

    # 计算压缩率
    compression_rate = calculate_compression_rate(original_size, total_compressed_size)

    return original_size, total_compressed_size, compression_rate

# Test with 8x8 blocks
image_path = "test2.png"
original_size_8x8, compressed_size_8x8, compression_rate_8x8 = compress_and_analyze(image_path, 8)

# Test with 16x16 blocks
original_size_16x16, compressed_size_16x16, compression_rate_16x16 = compress_and_analyze(image_path, 16)

# results
print(f"Original Size (8x8): {original_size_8x8} bits")
print(f"Compressed Size (8x8): {compressed_size_8x8} bits")
print(f"Compression Rate (8x8): {compression_rate_8x8 * 100:.2f}%")

print(f"\nOriginal Size (16x16): {original_size_16x16} bits")
print(f"Compressed Size (16x16): {compressed_size_16x16} bits")
print(f"Compression Rate (16x16): {compression_rate_16x16 * 100:.2f}%")

