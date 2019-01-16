#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/16 20:48
# FileName: D10_01装饰器详解.py
# Description: 
# Question: 
# --------------------------------


# 装饰器的前戏 --- 闭包
# 闭包的定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）
#   简单来说就是：闭包 = 内部函数 + 定义函数时的环境
def outer():
    x = 10

    def inner():    # inner就是内部函数
        print(x)    # x 就是对外部作用域的变量的引用

    return inner()  # 内部函数inner就被认为是一个闭包


print(outer())




# 装饰器(函数)






