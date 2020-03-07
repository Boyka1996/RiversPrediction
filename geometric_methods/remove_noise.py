# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：remove_noise.py
# Computer User          ：Administrator 
# Current Project        ：RiversPrediction
# Development Time       ：2020/3/7  22:47 
# Development Tool       ：PyCharm

import cv2
import numpy as np

img = cv2.imread('5.jpg')
print(np.shape(img))
kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(img, kernel, iterations=1)
# 显示图片
# ## 效果展示
# cv2.imshow('origin', img)


cv2.imwrite('lishuwang_dilate.jpg', dilate)
# erosion = cv2.erode(img,kernel,iterations = 1)
# cv2.imwrite('lishuwang_erosion.jpg',erosion)

canny1 = cv2.Canny(dilate, 100, 200)
cv2.imwrite('lishuwang_canny.jpg', canny1)

# kernel2 = np.ones((2,1),np.uint8)
# erosion = cv2.erode(canny,kernel2,iterations = 1)
# cv2.imwrite('lishuwang_erosion.jpg',erosion)

_, labels, stats, centroids = cv2.connectedComponentsWithStats(canny1)
print(centroids)
print("stats", stats)
i = 0
for istat in stats:
    if istat[4] < 120:
        # print(i)
        print(istat[0:2])
        if istat[3] > istat[4]:
            r = istat[3]
        else:
            r = istat[4]
        cv2.rectangle(canny1, tuple(istat[0:2]), tuple(istat[0:2] + istat[2:4]), 0, thickness=-1)  # 26
    i = i + 1

cv2.imwrite('lishuwang_canny1.jpg', canny1)