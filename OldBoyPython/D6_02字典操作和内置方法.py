#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/4 20:56
# FileName: D6_02字典操作和内置方法.py
# Description: 
# Question: 
# --------------------------------

# 字典采用键值对(key - value)的形式存储数据
# python对key进行哈希函数进行运算，根据运算的结果决定value的存储地址
# 字典的存储是无序存储的，且key必须是可哈希的，可哈希的表示key必须是不可变类型，如：数字、字符串、元组

# 字典的创建
# 传统创建字典的方式
dict_a = {
    "name": 'crisimple',
    "age": 24,
    "hobby": 'music',
    "job": 'programming',
    "single": True,
}
# 工厂函数创建字典的方式
dict_b = dict((("name", "Tester"), ))
print(dict_b)
dict_c = dict([("age", 24), ])
print(dict_c)

# 字典的增删改查
# 增
dict_a["salary"] = 1000000
print("增加键值对以后的dict_a", dict_a)

# 删除
dict_e = {"name": "B", "age": 24, "hobby": 'jita', "job": 'IT'}
print("清空字典，得到空字典：", dict_e.clear())
dict_f = {"name": "B", "age": 24, "hobby": 'jita', "job": 'IT'}
f = dict_f.pop("job")
print("pop删除指定值返回：", f)
print("pop指定键删除字典的值：", dict_f)
print("popitem随机删除字典的值：", dict_f.popitem())
del dict_f
print("del删除整个字典dict_f：", dict_f)

# 改
dict_b = {"name": "B", "age": 24, "hobby": 'jita', "job": 'IT'}
print("通过键来赋值更改字典前：", dict_b)
dict_b["name"] = 'C'
print("通过键来赋值更改字典后：", dict_b)
b1 = dict_b.setdefault("age", 25)
print("如果本来存在键，setdefault返回值：", b1)
b2 = dict_b.setdefault("single", True)
print("本来不存在键，setdefault返回值：", b2)


# 查
print("通过字典的键来查：", dict_a["name"])
print("通过keys查看所有的键：", dict_a.keys())
print("通过values查看所有的值：", dict_a.values())
print("通过items查看所有的键值对：", dict_a.items())

