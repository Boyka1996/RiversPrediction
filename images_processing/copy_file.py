# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：copy_file.py
# Computer User          ：Administrator 
# Current Project        ：DataProcess_Python
# Development Time       ：2020/2/25  20:46 
# Development Tool       ：PyCharm
import os
import shutil
# list_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/images/uniform'
# src_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/divide_to_9副本'
# tar_path = 'E:/PycharmProjects/images/uniform'
# list_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/images/left'
# src_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/divide_to_9副本'
# tar_path = 'E:/PycharmProjects/images/left'
list_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/images/right'
src_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/divide_to_9副本'
tar_path = 'E:/PycharmProjects/images/right'
# list_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/images/vertical'
# src_path = 'E:/PycharmProjects/DataProcess_Python/rivers_fitting/divide_to_9副本'
# tar_path = 'E:/PycharmProjects/images/vertical'
if __name__ == '__main__':
    if not os.path.exists(tar_path):
        os.makedirs(tar_path)
    for img in os.listdir(list_path):
        for src_img in os.listdir(src_path):
            if img in src_img:
                shutil.copy(os.path.join(src_path,src_img),os.path.join(tar_path,src_img))

