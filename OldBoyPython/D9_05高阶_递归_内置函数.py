#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/16 14:36
# FileName: D9_05高阶函数和递归函数.py
# Description: 
# Question: 
# --------------------------------
from functools import reduce


# ==================高阶函数===============
# 子函数
def func(n):
    return n * n


# 下面定义的这个函数称之为高阶函数
def high_fuc(a, b, func):
    return func(a) + func(b)


print(high_fuc(1, 2, func))


# ====================递归函数=======================
# 递归函数: 其本质就是一个高阶函数
# 用递归函数实现阶乘， 递归的特点：
#   1. 递归的效率在多数情况下非常低
#   2. 能用递归完成的，用循环都可以完成
#   3. 递归就是自己调自己
#   4. 递归必须有一个结束条件
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)

# 5 * fac(4)
# 5 * 4 * fac(3)
# 5 * 4 * 3 * fac(2)
# 5 * 4 * 3 * 2 * fac(1)
# 5 * 4 * 3 * 2 * 1
print(fac(5))


# 用递归实现斐波拉契数列
# 0 1 1 2 3 5 8 13 21 34 55
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(8))


# ==================内置函数=========================
# 3.1. all() 判断是否元素中是否有空元素
print(all([1, 2, "string", '']))
print(all("string"))

# 3.2 set是可变击合，frozenset为不可变集合
set_a = set("abcdefg")
set_b = frozenset("ABCDEFG")
print("set_a: ", set_a)
print("set_b: ", set_b)
set_a.update("x")
print("set_a: ", set_a)
# set_b.update("b")


# filter 过滤器比较省内存，利用了迭代器的原理
def fun1(n):
    return n % 2 == 1

filter_list = filter(fun1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("filter_list: ", filter_list)
print("filter_list: ", list(filter_list))


# map 对对象进行遍历处理
def fun2(n):
    return "V_" + n

map_list = map(fun2, ["Y", "X", "Z"])
print("map_list: ", map_list)
print("map_list: ", list(map_list))


# reduce 返回是一个值
def fun3(x, y):
    return x * y

reduce_list = reduce(fun3, range(1, 6))
print("reduce_list: ", reduce_list)


# lambda 匿名函数
# 实现阶乘
print("lambda_list: ", reduce(lambda x, y: x*y, range(1, 6)))







