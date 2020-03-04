# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：devide_images.py
# Computer User          ：Administrator 
# Current Project        ：DataProcess_Python
# Development Time       ：2020/2/25  16:33 
# Development Tool       ：PyCharm
import os
import cv2

if __name__ == '__main__':
    img_path = 'images/All_images'
    save_path_3 = 'divide_to_3'
    save_path_9 = 'divide_to_9'
    if not os.path.exists(save_path_3):
        os.makedirs(save_path_3)
    if not os.path.exists(save_path_9):
        os.makedirs(save_path_9)
    for img in os.listdir(img_path):
        cv_img = cv2.imread(os.path.join(img_path, img))
        width, height, channel = cv_img.shape
        print(width)
        sub_imgs = [None, None, None]
        sub_imgs[0] = cv_img[0:int(height / 3), 0:width]
        sub_imgs[1] = cv_img[int(height / 3):2 * int(height / 3), 0:width]
        sub_imgs[2] = cv_img[2 * int(height / 3):height, 0:width]
        for img_id, sub_img in enumerate(sub_imgs):
            cv2.imwrite(os.path.join(save_path_3, str(img_id) + '_' + img), sub_img)
            little_images = [None, None, None]
            little_images[0] = sub_img[0:int(height / 3), 0:int(width / 3)]
            little_images[1] = sub_img[0:int(height / 3), int(width / 3):2 * int(width / 3)]
            little_images[2] = sub_img[0:int(height / 3), 2 * int(width / 3):width]
            for little_img_id, little_image in enumerate(little_images):
                cv2.imwrite(os.path.join(save_path_9, str(img_id) + '_' + str(little_img_id) + '_' + img), little_image)
