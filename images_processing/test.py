# -*- coding: utf-8 -*-
# School                 ：UPC
# Author                 ：Boyka
# E-mail                 ：upcvagen@163.com
# File Name              ：test.py
# Computer User          ：Administrator 
# Current Project        ：DataProcess_Python
# Development Time       ：2020/2/24  19:51 
# Development Tool       ：PyCharm

import numpy as np

a = np.array([0, 1])
print(a)
b = np.array([0, 1])
w = np.polyfit(a, b, 1)
bias = np.poly1d(w)
print(type(w))
print(len(w))
print(w)
print(bias)
