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


# 函数的创建，示例：简单的日志记录
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


action1(1)
action2(2)
action3(3)









