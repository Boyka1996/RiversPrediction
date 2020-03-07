#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 下午11:55
# @Author  : Boyka
# @Email   : upcvagen@163.com
# @File    : threshold_optimization.py
# @Software: PyCharm

import json
import matplotlib.pyplot as plt


def get_errors_num(binary_angle_list, uniform_angle_list, threshold):
    binary = 0
    uniform = 0
    for binary_angle in binary_angle_list:
        if binary_angle > threshold:
            binary += 1
    for uniform_angle in uniform_angle_list:
        if uniform_angle < threshold:
            uniform += 1
    return binary, uniform


if __name__ == '__main__':
    binary_list = json.load(open('binary.json', 'r')).values()
    uniform_list = json.load(open('uniform.json', 'r')).values()
    print(len(uniform_list))
    binary_loss = []
    uniform_loss = []
    total_loss = []
    min_loss = 1000
    min_loss_angle = 0
    for i in range(91):
        binary_num, uniform_num = get_errors_num(binary_list, uniform_list, i)
        binary_loss.append(binary_num)
        uniform_loss.append(uniform_num)
        total_loss.append(binary_num + uniform_num)
        if (binary_num + uniform_num) < min_loss:
            min_loss = (binary_num + uniform_num)
            min_loss_angle = i
    print(min_loss, min_loss_angle)
    fig = plt.figure(num=1, figsize=(15, 8), dpi=80)  # 开启一个窗口，同时设置大小，分辨率
    ax1 = fig.add_subplot(1, 1, 1)  # 通过fig添加子图，参数：行数，列数，第几个。
    ax1.set_title('Error number')  # 设置图体，plt.title
    ax1.set_xlabel('angle')  # 设置x轴名称,plt.xlabel
    ax1.set_ylabel('num')  # 设置y轴名称,plt.ylabel
    angle_list = [angle for angle in range(91)]
    plot1 = ax1.plot(angle_list, binary_loss, color='g', label='binary_num')  # 点图：marker图标
    plot2 = ax1.plot(angle_list, uniform_loss, color='b',
                     label='uniform_num')  # 线图：linestyle='--',linestyle线性，alpha透明度，color颜色，label图例文本
    plot3 = ax1.plot(angle_list, total_loss, marker='o', color='r', label='total_loss')  # 点图：marker图标
    # plt.plot(angle_list,total_loss)
    plt.legend()
    plt.savefig('loss.jpg')
    plt.show()
