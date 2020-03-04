#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 下午1:58
# @Author  : Boyka
# @Email   : upcvagen@163.com
# @File    : get_img_shape.py
# @Software: PyCharm
import cv2
import os

if __name__ == '__main__':
    path = 'sub_img/train/uniform'
    for img in os.listdir(path):
        print(img)
        cv_img = cv2.imread(os.path.join(path, img))
        print(cv_img.shape)
