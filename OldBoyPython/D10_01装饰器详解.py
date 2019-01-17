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
import time

# 装饰器的前戏 --- 闭包
# 闭包的定义：如果在一个内部函数里，对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包（closure）
#   简单来说就是：闭包 = 内部函数 + 定义函数时的环境
def outer():
    x = 10

    def inner():    # inner就是内部函数
        print(x)    # x 就是对外部作用域的变量的引用

    return inner()  # 内部函数inner就被认为是一个闭包


print(outer())




# 装饰器 -- 其实就是一种特殊的函数
#   它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象


# 装饰器的引入：
# 为了计算say_hello()函数的执行时间
def show_time(f):   # 此处的参数f就相当于是内部函数cal_time的外部作用域
    def cal_time():
        start_time = time.time()
        time.sleep(1)
        f()     # 这里的f()函数就相当于是
        end_time = time.time()
        print("函数执行耗时：", (end_time - start_time))
    return cal_time

# say_hello = show_time(say_hello)
# 给功能函数增加参数
@show_time     # 装饰器就相当于是上面的一行的意思，进行赋值操作
def say_hello(*args, **kwargs):
    sum_num = 0
    for i in args:
        sum_num += i
    return sum_num
    print("I'm say function")


print(say_hello())


# 给装饰器加参数
def logger(flag):
    def show_time(f):
        def inner(*args, **kwargs):
            sum_num = 0
            for i in args:
                sum_num += i
            return sum_num
        return inner
    return show_time


print("=============logger============")
@logger("True")
def say_hello(*args, **kwargs):
    sum_num = 0
    for i in args:
        sum_num += i
    return sum_num
    print("I'm say function")


print(say_hello())











