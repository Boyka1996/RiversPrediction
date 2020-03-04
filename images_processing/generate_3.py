# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：generate_3.py
# Computer User          ：Administrator 
# Current Project        ：DataProcess_Python
# Development Time       ：2020/2/26  9:38 
# Development Tool       ：PyCharm


import os
import cv2
import numpy as np

if __name__ == '__main__':
    img_path = 'images/vertical'
    save_path = 'images/sub_img/train/vertical'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for img in os.listdir(img_path):
        cv_img = cv2.imread(os.path.join(img_path, img))
        width, height, channel = cv_img.shape
        top_image = cv_img[0:int(height / 3), 0:width]
        top_image = np.rot90(np.rot90(top_image))
        bottom_image = cv_img[(2 * int(height / 3)+1):height, 0:width]
        cv2.imwrite(os.path.join(save_path, 'top_' + img.replace('.png', '.jpg')), top_image)
        cv2.imwrite(os.path.join(save_path, 'bottom_' + img.replace('.png', '.jpg')), bottom_image)
