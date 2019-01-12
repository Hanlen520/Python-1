#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/12 17:54
# FileName: D9_01深浅拷贝.py
# Description: 
# Question:
# --------------------------------------
import copy

# 深浅拷贝的引入
list_a = ["A", "B", "C"]
# 通过赋值的方式复制一个列表
list_b = list_a
print("list_a: ", list_a)
print("list_b: ", list_b)
# 更改list_b的值
list_b[0] = "a"
print("list_a: ", list_a)
print("list_b: ", list_b)
print("*".join(["---", "分割线1"]).center(30))

# ---
list_c = ["菜鸟", "大笨蛋", "废物"]
list_d = list_c.copy()
print("list_c: ", list_c)
print("list_d: ", list_d)
# 更改list_d的值
list_d[0] = "高手"
print("list_c: ", list_c)
print("list_d: ", list_d)
print("*".join(["---", "分割线2"]).center(30))

# --- 浅拷贝只会copy列表的第一层
list_e = [[1, 2], 3, 4]
list_f = list_e.copy()
print("list_e: ", list_e)
print("list_f: ", list_f)
# 更改list_f的值
list_f[0][0] = 2
print("list_e: ", list_e)
print("list_f: ", list_f)
print("*".join(["---", "分割线3"]).center(30))
# 浅拷贝的应用
husband = ["husband", 1001, [10000, 5000]]
wife = husband.copy()
# wife = copy.copy(husband)  与上一行等同就是浅拷贝
wife[0] = "wife"
wife[1] = 1002
wife[2][0] -= 3000
print("husband: ", husband)
print("wife: ", wife)
print("*".join(["---", "分割线4"]).center(30))


# --- 深拷贝: 全部拷贝
husbands = ["husbands", 1001, [10000, 5000]]
lover = copy.deepcopy(husbands)
lover[0] = "lover"
lover[1] = 1003
lover[2][0] -= 5000
print("husbands: ", husbands)
print("lover: ", lover)
