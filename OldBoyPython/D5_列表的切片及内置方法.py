#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: jiangheng
# CreateTime: 2019/1/2 21:07
# FileName: D5_列表的切片及内置方法.py
# Description: 
# Question: 
# --------------------------------

list_a = ["A", "B", "C", "D", "E"]
print("原始的列表list_a: ", list_a)

# 列表的增删改查
# 增
list_a.append("F")
list_a.append("F")
list_a.append("F")
print("append以后的列表list_a：", list_a)
list_a.insert(3, "O.O")
print("insert以后的列表list_a：", list_a)
list_b = ["a", "b", "c", "d"]
print("将list_b中元素放入到list_a中后的结果为：", list_a.extend(list_b))

# 删
print(list_a.pop(2))        # pop是可以知道你要删除的是那个数据
print("pop以后的列表list_a：", list_a)
list_a.remove(list_a[3])
print("remove以后的列表list_a：", list_a)
del list_a[4]
print("del以后的列表list_a：", list_a)

# 改
list_a[0] = "modify"
print("改以后的列表list_a：", list_a)

# 查(切片、索引)
print(list_a[0::2])
print(list_a)
print("取出'o.o'的索引为：", list_a.index("O.O"))
print("计算列表中某个元素的个数：", list_a.count("F"))

# reverse（翻转）
list_c = [2, 5, 1, 4, 6, 3, 0, 9, 8, 1, 7]
list_c.reverse()
print(list_c)

# sort（排序）
list_c.sort()
print(list_c)