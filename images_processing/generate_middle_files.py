# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：generate_middle_files.py
# Computer User          ：Administrator 
# Current Project        ：RiversPrediction
# Development Time       ：2020/3/7  13:02 
# Development Tool       ：PyCharm

import os
import cv2

if __name__ == '__main__':
    img_path = 'E:/PycharmProjects/river_prediction_files/binary_uniform_images/uniform'
    save_path = 'E:/PycharmProjects/river_prediction_files/binary_uniform_images/sub_images/uniform'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for img in os.listdir(img_path):
        cv_img = cv2.imread(os.path.join(img_path, img))
        width, height, channel = cv_img.shape
        sub_image = cv_img[255:767, 0:width]
        cv2.imwrite(os.path.join(save_path, img.replace('rivers', 'uniform_')), sub_image)
