#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/14 13:29
# FileName: D9_03函数.py
# Description: 函数的出现就是为了解决代码重复，保持一致性和可扩展性
# Question: 
# --------------------------------
import time


# 1.函数的创建，示例：简单的日志记录
def logger(n):
    time_format = "%Y-%m-%d %H-%M-%S"
    current_time = time.strftime(time_format)

    with open("./OperatorFile/D9_03日志记录.txt", 'a') as f:
        f.write("Now time is: %s , action is: %s \n" % (current_time, n))


def action1(n):
    logger(n)


def action2(n):
    logger(n)


def action3(n):
    logger(n)


# action1(1)
# action2(2)
# action3(3)


# ==============================参数==================================
# 参数的放置顺序，形参、默认参数、不定长参数*args、不定长参数**kwargs
# 2. 函数的参数
# sex就为默认参数
# info(name, age) 位置形参
def info(name, age, sex="male"):
    print("Name: %s" % name)
    print("Age: %d" % age)
    print("Sex: %s" % sex)


# 必须参数
# 位置实参
info("crisimple", 24)


# 关键词参数
info(name="cris", age=25)


# 不定长参数
# 形参*接收多出来的位置参数转化为元组
def info2(*args):
    print(args)
    sum = 0
    for i in args:
        sum += i
    print("总和为：", sum)


info2(1, 2, 3, 4, 5)


# 多出来的关键字参数被**接收转化为字典
def info3(*args, **kwargs):
    for i in args:
        print(i)

    for j in kwargs:
        print("%s: %s" % (j, kwargs[j]))


info3("Simple", 23, "male", Job="IT", Hobby="Music", Sigle=True)


# ==============================关键词return==================================
# 作用：结束函数 、 返回一个对象
# 注意点：函数如果没有return，会默认返回一个None；
#        如果return多个对象，Python会把这多个对象封装成一个元组对象返回
def foo():
    print("-----A------")
    return 1, 2, "string", [1, 2, 3], {"Name:", "Cris"}
    print("=====B======")


print(foo())










