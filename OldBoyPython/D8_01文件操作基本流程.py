#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/10 20:18
# FileName: D8_01文件操作基本流程.py
# Description: 
# Question: 
# --------------------------------

# 创建文件读操作对象
fr = open("./OperatorFile/小诗小吟.txt", 'r', encoding="utf-8")
# 读取数据操作
data = fr.read()
print(data)
print("fr: ", fr.fileno())
# 关闭文件操作
fr.close()

# 创建文件写操作对象
# 如果文件存在则会清空文件，重新开始写的操作
# 如果文件不存在则会创建文件，开始写的操作
# 但是这种写操作会连在一块
fw = open("./OperatorFile/没有文件创建文件.txt", 'w', encoding="utf-8")
fw.write("我们是祖国的花朵")
fw.write("你一定会爱上我")
print("fw: ", fw.fileno())
# 关闭文件操作
fw.close()

import time
# 创建append文件操作对象
fa = open("./OperatorFile/append文件.txt", 'a', encoding="utf-8")
fa.write("\n Hello Python \n")
fa.write("Hello Shell \n")
fa.write("Hello JavaScript\n")
print("fa: ", fa.fileno())

# time.sleep(50)
fa.close()







