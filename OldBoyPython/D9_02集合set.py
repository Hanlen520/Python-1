#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/12 23:14
# FileName: D9_02集合set.py
# Description: set：把不同的元素集合在一起形成的集合
# Question:
# --------------------------------------

# 1.创建集合
set_a = set("Hello Word")
set_b = set(["HEllo", "hello", "Word"])
print(set_a)    # 由此可以看出集合的元素是唯一不可重复的，因此可以用来做去重
print(set_b)


# 2.判断元素是否存在于集合内in / not in
print("a" in set_a)
print("e" in set_a)
print("e" not in set_a)


# 3.更新集合
# 添加元素: 以整体增加
set_a.add("uu")
print("set_a: ", set_a)

# 更新元素: 以小结合增加到大集合中
set_a.update("ops")
print("set_a: ", set_a)

# 删除元素 -- 随机删除的，因为集合中的元素的排列是无序的
set_a.pop()
print("set_a: ", set_a)


# 4.集合关系测试：相等、包含、交集
print(set("HHEELLOO") == set("HELLO"))
set_e = set("12345")
set_f = set("45678")
print("set_e: ", set_e)
print("set_f: ", set_f)

# 父集（超集）
print(set("hell") < set("hello"))

# 取交集
print("交集：", set_e.intersection(set_f))
print("交集：", set_e & set_f)

# 取并集
print("并集：", set_e.union(set_f))
print("并集：", set_e | set_f)

# 取差集
print("差集：", set_e.difference(set_f))
print("差集：", set_e - set_f)
print("差集：", set_f.difference(set_e))
print("差集：", set_f - set_e)

# 对称差集（反向交集）
print("对称差集：", set_e.symmetric_difference(set_f))
print("对称差集：", set_e ^ set_f)

