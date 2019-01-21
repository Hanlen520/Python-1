#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/20 16:38
# FileName: D10_05迭代器.py
# Description: 
# Question:
# --------------------------------------

# 生成器都是迭代器，迭代器不一定是生成器
from collections.abc import Iterable


# 1. 什么时可迭代对象
#   for 循环后面跟的都是可迭代对象
#   可迭代对象都有__iter__方法
#   常见的几种数据类型中：列表、元组、字典、字符串均是可迭代对象
list_a = [1, 2, 3, 4]
print(list_a.__iter__())
a = iter(list_a)
print(a)


# 2. 什么是迭代器
#   一、有iter()方法
#   二、有next()方法
print(next(a))
print(next(a))


# 3. for进行生成器或迭代器循环时，进行了三件事：
# （1）调用可迭代对象的iter方法返回一个可迭代对象
# （2）不断调用迭代器的next方法
# （3）处理StopIteration
# for i in list_a:
#     iter(i)     # TypeError: 'int' object is not iterable


# 4. 判断是否是迭代器
print(isinstance(a, Iterable))
