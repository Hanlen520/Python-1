#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/5 17:32
# FileName: D6_03字符串的操作.py
# Description: 
# Question:
# --------------------------------------

# 创建字符串
string1 = '我是字符串1'
string2 = "我是字符串2"
print(string1)
print(string2)

# 1.重复打印字符串
string3 = "Hello "
print(string3 * 3)

# 2.字符串切片
string4 = "Hello Python!"
print(string4[6:])

# 3.判断字符串是不是在某一个字符串内
string5 = "llo"
print(string5 in string4)

# 4.格式化输出
string6 = "小精灵"
print("我是一只小精灵、%s" % string6)

# 5.字符串拼接
string7 = "abc"
string8 = "123"
string9 = "ABC"
print(string7 + string8)
string10 = "******".join([string7, string8, string9])
print(string10)

# 6.字符串的内置方法
string11 = "this is a string."
print("统计元素个数：", string11.count("i"))
print("字符串开头首字母大写：", string11.capitalize())
print("字符串剧中：", string11.center(50, '*'))
print("字符串剧中：", string11.encode())