#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/21 22:20
# FileName: D13_02Python中的编码方式.py
# Description: 
# Question:
# --------------------------------------

# python中有两种数据类型
# Unicode
# bytes

# str ---> bytes     编码过程
s1 = "Hello你好"
# utf-8(gbk, utf-16)规则下的bytes类型
b1 = bytes(s1, 'utf-8')
b11 = s1.encode("utf-8")
b111 = bytes(s1, 'gbk')
print("b1: ", b1)       # b'Hello\xe4\xbd\xa0\xe5\xa5\xbd'
print("b11: ", b11)     # b'Hello\xe4\xbd\xa0\xe5\xa5\xbd'
print("b111: ", b111)


# bytes ---> str      解码过程
s2 = str(b11, 'utf-8')
print('s2: ', s2)
s22 = b1.decode('utf-8')
print('s22: ', s22)
s222 = b111.decode('gbk')
print('s222: ', s222)


