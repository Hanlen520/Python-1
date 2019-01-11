#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/11 20:38
# FileName: D8_02文件操作具体方法.py
# Description: read tell seek flush
# Question: 
# --------------------------------
import sys
import time

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

f.close()


# flush将缓存中的数据写入到硬盘上去
# 在终端上打印简易的进度条演示
# for i in range(30):
#     sys.stdout.write("*")
#     sys.stdout.flush()
#     print("X", end='', flush=True)
#     time.sleep(0.1)


# truncate截断写入的数据，截取内容为起始位置到要截取的长度
ft = open("./OperatorFile/truncate.txt", 'w', encoding="utf8")
ft.write("Hello Word")
print(ft.tell())
print(ft.truncate(6))
ft.close()


# 读写 写读 追加读
# r+ 读写模式：读文件的同时可以将数据写进文件里
fr_ = open("./OperatorFile/小诗小吟.txt", 'r+', encoding="utf-8")
print(fr_.readlines())
fr_.write("杨绛")
print("=======================")
# print(fr_.readlines())
fr_.close()

# w+ 写读模式：先将文件内容清空，然后再往文件里面写入数据并读取，因此读取到的也只是写人的数据
fw_ = open("./OperatorFile/没有文件创建文件.txt", 'w+', encoding="utf-8")
fw_.write("我是刚写进的字符串")
fw_.flush()
print(fw_.readlines())
fw_.close()

# a+ 追加读模式：光标在文末，添加数据的同时并读取数据
# fa_ = open("./OperatorFile/没有文件创建文件.txt", 'a+', encoding="utf-8")
# fa_.append("我是刚添加的字符串")
# fa_.flush()
# print(fa_.readlines())
# fa_.close()
