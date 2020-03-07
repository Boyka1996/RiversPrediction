# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：filp_fitting.py
# Computer User          ：Administrator 
# Current Project        ：RiversPrediction
# Development Time       ：2020/3/7  17:53 
# Development Tool       ：PyCharm

import cv2
import numpy as np
import math
import os
import json

TOP_LINE = 341
BOTTOM_LINE = 950
MID_LINE = 511
WIDTH = 1024
HEIGHT = 1024


def sub_image_filp(cv_img):
    width, height = cv_img.shape
    # 二值翻转
    for row in range(width):
        for col in range(height):
            cv_img[row][col] = 255 - cv_img[row][col]
    left_img = cv_img[TOP_LINE:BOTTOM_LINE, 0:MID_LINE]
    right_img = cv_img[TOP_LINE:BOTTOM_LINE, (MID_LINE + 1):(width - 1)]
    """
    参数2 必选参数。用于指定镜像翻转的类型，其中0表示绕×轴正直翻转，即垂直镜像翻转；1表示绕y轴翻转，即水平镜像翻转；-1表示绕×轴、y轴两个轴翻转，即对角镜像翻转。
参数3 可选参数。用于设置输出数组，即镜像翻转后的图像数据，默认为与输入图像数组大小和类型都相同的数组。
    """
    # 先裁剪出来，左面翻转后叠加在右面
    left_img_filp = cv2.flip(left_img, 1)
    sub_img = right_img + left_img_filp
    result_img = cv2.flip(sub_img, 0)
    # kernel = np.ones((10, 10), np.uint8)
    # dilate = cv2.dilate(result_img, kernel, iterations=1)
    # cv2.imwrite('1.jpg', left_img)
    # cv2.imwrite('2.jpg', left_img_filp)
    # cv2.imwrite('3.jpg', right_img)
    # cv2.imwrite('5.jpg', result_img)
    # cv2.imwrite('6.jpg',dilate)
    return result_img


def convert_to_binary_image(cv_img):
    gray = cv2.cvtColor(cv_img, cv2.COLOR_RGB2GRAY)  # 把输入图像灰度化
    # cv2.imwrite("gray_image.jpg", gray)
    # 直接阈值化是对输入的单通道矩阵逐像素进行阈值分割。
    ret, binary_image = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # cv2.imwrite('result.jpg', binary_image)
    return binary_image


def get_coordinate_list(cv_img):
    x_list = []
    y_list = []
    # print(len(img))
    # print(len(img[0]))
    for x_id, x_value in enumerate(cv_img):
        for y_id, y_value in enumerate(cv_img[x_id]):
            # if y_id % 2 == 0:
            #     continue
            if y_value != 0:
                y_list.append(x_id)
                x_list.append(y_id)
    return x_list, y_list


def fit_river(x_list, y_list):
    w = np.polyfit(x_list, y_list, 1)  # 一次多项式拟合，相当于线性拟合
    # b = np.poly1d(w)
    # print(w)
    angle = 90 - (math.degrees(np.arctan(w[0])))
    print(angle)
    return angle


if __name__ == '__main__':
    # img_path = 'E:/PycharmProjects/river_prediction_files/binary_uniform_images/uniform/rivers1794.jpg'
    # merged_img = sub_image_filp(convert_to_binary_image(cv2.imread(img_path)))
    # x_coor_list, y_coor_list = get_coordinate_list(merged_img)
    # ang = fit_river(x_coor_list, y_coor_list)
    img_path = 'E:/PycharmProjects/river_prediction_files/binary_uniform_images/binary/'
    angle_dict = {}
    count = 0
    for img in os.listdir(img_path):
        count += 1
        print(count)
        merged_img = sub_image_filp(convert_to_binary_image(cv2.imread(os.path.join(img_path, img))))
        x_coor_list, y_coor_list = get_coordinate_list(merged_img)
        ang = fit_river(x_coor_list, y_coor_list)
        angle_dict[img] = ang
    with open('binary.json', 'w') as f:
        json.dump(angle_dict, f)
