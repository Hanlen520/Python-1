#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/14 23:02
# FileName: D9_04函数的作用域.py
# Description: 
# Question:
# --------------------------------------

# 1. 函数的作用域引入
if True:
    a = 10
print("if打印的：", a)

# def foo(b):
#     b = 20
#
# print(foo())
# print(b)
# 报错：变量b没有被定义，因此说明if条件里的变量是没有作用域的，而函数里面的变量是有作用域的


# 2. 函数的作用域范围: BGEL
# 作用域范围的查找顺序为：LEGB（作用域局部 > 外层作用域 > 当前模块中的全局 > python内置作用域）
c = int(2.9)  # built-in

g_count = 0  # global


# def outer():
#     out_count = 1  # enclosing
#
#     def inner():
#         i_count = 3  # local
#         print(i_count)
#
#     print(i_count)   # 找不到
#     inner()


# 3. 局部作用域的变量不能修改全部作用域的变量
counter = 10


def add():
    global counter   # 此处用global声明了counter为全部变量，如果此处不用global全局声明，直接打印下一行会报错，这就相当于是变量没有定义变量直接使用了变量
    print("全部变量counter打印的：", counter)   # 如果此处引用的全部作用域的变量，因此此处的counter打印的是全局变量的值
    counter = 5      # 下面就不能用局部作用域的变量来修改全局作用域的变量了
    print("局部变量counter打印的：", counter)   # 由于上一行重新定义变量，变量又变成了局部变量，因此此处打印的是局部变量的值

add()




