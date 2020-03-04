#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 上午11:13
# @Author  : Boyka
# @Email   : upcvagen@163.com
# @File    : config.py.py
# @Software: PyCharm


#数据集的类别
NUM_CLASSES = 4

#训练时batch的大小ge
BATCH_SIZE = 32

#训练轮数
NUM_EPOCHS= 150

#预训练模型的存放位置
#pytorch更新以后现在是自己下载了，如果下不下来可以在其他地方下下来以后放到torch的cache下
#下载地址：https://download.pytorch.org/models/resnet50-19c8e357.pth
PRETRAINED_MODEL = './resnet101-5d3b4d8f.pth'

##训练完成，权重文件的保存路径,默认保存在trained_models下
TRAINED_MODEL = 'r-50-32-150_rivers.pth'

#这里我后面改一下
#数据集的存放位置
TRAIN_DATASET_DIR = './river_images/train'
VALID_DATASET_DIR = './river_images/val'