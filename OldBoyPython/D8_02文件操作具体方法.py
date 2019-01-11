#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/11 20:38
# FileName: D8_02文件操作具体方法.py
# Description: read tell seek
# Question: 
# --------------------------------
f = open("./OperatorFile/小诗小吟.txt", 'r', encoding="utf-8")
print("tell打印光标所在位置：", f.tell())


# 注意了：如果文件内容是英文时，tell识别的时候一个英文字符占一个字节位置；
#        如果文件内容是中文时，tell识别的时候一个汉字字符占三个字节的位置
print("read(2)读取两个字符：", f.read(2))
print("read(3)读取两个字符：", f.read(3))
print("tell打印光标所在位置：", f.tell())


# 调整光标所在的位置，seek作用可以用于文件传输时候的断点续传
print("seek调整光标所在的位置：", f.seek(0))
print("tell打印光标所在位置：", f.tell())
print("read(4)读取两个字符：", f.read(4))
print("tell打印光标所在位置：", f.tell())

# flush将缓存中的数据写入到硬盘上去
# 在终端上打印简易的进度条演示
import sys
import time

for i in range(30):
    sys.stdout.write("*")
    sys.stdout.flush()
    print("X", end='', flush=True)
    time.sleep(0.1)

f.close()