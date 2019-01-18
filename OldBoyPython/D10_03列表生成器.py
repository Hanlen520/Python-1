#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/18 9:50
# FileName: D10_03列表生成器.py
# Description: 
# Question: 
# --------------------------------

# ==================列表生成式===============
# 下面的这个执行机理为：for x in range(0, 10)生成的每一个元素，传给到x * x里面进行计算
list_0 = []
for x in range(0, 10):
    list_0.append(x)
print(list_0)
list_a = [x * x for x in range(0, 10)]
print("list_a: ", list_a)
















