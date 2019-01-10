#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/8 22:18
# FileName: D7_python的字符编码.py
# Description: 
# Question:
# --------------------------------------

# 二进制
# 美国标准
# -----ASCII: 只能存英文和拉丁字符， 一个字符占一个字节(8位)
# 国标
# -----gb2312: 只能存6700多个中文，1980
# -------gbk1.0: 存20000多字符， 1995
# ---------gb18030: 27000中文
# 万国码
# -----Unicode：utf-32   一个字符占4个字节
# -----Unicode：utf-16   一个字符占2个字节
# -----Unicode：utf-8    一个英文用ASCII码来存，一个中文占3个字节

# Python的编码规则
# 编码encode: 将语言转换为Unicode
# 解码decode: 将Unicode转换为某种语言

<<<<<<< HEAD

# Python2：
# Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> string = "特斯拉"
# >>> type(string)
# <type 'str'>
# >>> string
# '\xcc\xd8\xcb\xb9\xc0\xad'
# string.decode("gbk")
# u'\u7279\u65af\u62c9'


# Python3:
# Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> string = "埃隆马斯克"
# >>> string
# '埃隆马斯克'
=======
# Python2：默认编码是ASCII码编码
# string = "特斯拉"


# Python3：默认编码是unicode编码





>>>>>>> fbf128dd0c9d03c187b9b7b20e360351517b60b6









