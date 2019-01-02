#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 03Chapter-PythonBase.py
# author: jiangheng
# description:
# questions:

# ----------------3.2 变量赋值
# 链式赋值
x = 1
y = x = x + 1
print(x, y)

# 增量赋值
x += 1
x -= 2
# x &= 2
x ^= 1
print(x)

# 多重赋值
a = b = c = 2
print(a, b, c)

# 多元赋值
e, f, g = 1, 2, 'String'
# 无需中间变量，可以实现两个变量交换彼此的值
# 更好解释了引用
h, i = 10, 19
print(h, i)
h, i = i, h
print(h, i)
