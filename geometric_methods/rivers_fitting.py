# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：rivers_fitting.py
# Computer User          ：Administrator 
# Current Project        ：DataProcess_Python
# Development Time       ：2020/2/24  14:05 
# Development Tool       ：PyCharm

import cv2
import numpy as np


def convert_to_binary_image(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 把输入图像灰度化
    cv2.imwrite("gray_image.jpg", gray)
    # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    cv2.imwrite('result.jpg', binary_image)
    return binary_image


def get_coordinate_list(img):
    x_list = []
    y_list = []
    temp = []
    for x_id, x_value in enumerate(img):
        for y_id, y_value in enumerate(img[x_id]):
            if y_value == 0:
                temp.append((x_id, y_id))
                x_list.append(x_id)
                y_list.append(y_id)
    print(temp)
    return x_list, y_list


def fit_river(x_list, y_list):
    w = np.polyfit(x_list, y_list, 1)  # 一次多项式拟合，相当于线性拟合
    b = np.poly1d(w)
    return w, b


if __name__ == '__main__':
    img_path = 'images/4.jpg'
    binary_img = convert_to_binary_image(img_path)
    x_coor_list, y_coor_list = get_coordinate_list(binary_img)
    weight, bias = fit_river(x_coor_list, y_coor_list)
