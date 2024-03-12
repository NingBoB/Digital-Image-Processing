# -*- coding: utf-8 -*-
# @Time    : 2023/11/15 15:58
# @Author  : Mean
# @File    : gamma.py
# @Description: 实现gamma变换
import cv2
import numpy as np

img = cv2.imread("../class1/pheasant.jpg")
cv2.imshow("organ", img)

# 默认gamma值为1.0，默认不变化
def adjust_gamma(image, gamma=1.0):
    invgamma = 1/gamma
    brighter_image = np.power((image/255), invgamma)        # imshow内部的参数类型可以分为两种,
    # 1）当输入矩阵是uint8类型的时候，此时imshow显示图像的时候，会认为输入矩阵的值范围在0-255之间。（2）如果imshow的参数是double类型的时候，那么imshow会认为输入矩阵值的范围在0-1。
    # 所以若结果为大于 1 的浮点数就会被看做 1 ，等同与 255
    # brighter_image = np.array(np.power((image/255), invgamma)*255, dtype=np.uint8)
    return brighter_image

# gamma大于1，变亮
img_gamma1 = adjust_gamma(img, gamma=3.0)
cv2.imshow("gamma=3.0", img_gamma1)

# gamma小于1，变暗
img_gamma2 = adjust_gamma(img, gamma=0.5)
cv2.imshow("gamma=0.5", img_gamma2)

cv2.waitKey(0)
