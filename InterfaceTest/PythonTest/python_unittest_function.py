#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 14:25
# FileName: python_unittest_function.py
# Description: 
# Question: 
# --------------------------------

def one_equation(a, b):
    '''
    求方程 a * x + b = 0 的解
    参数 a ----- 方程中变量的系数
    参数 b ----- 方程中的常量
    返回方程的解
    :param a:
    :param b:
    :return:
    '''
    if a == 0:
        raise ValueError('参数错误')
    else:
        return b / a

def two_equation(a, b, c):
    '''
    求方程 a * x * x + b * x + c = 0的解
    参数 a ----- 方程中变量二次幂的系数
    参数 b ----- 方程中变量的系数
    参数 c ----- 方程中的常量
    :param a:
    :param b:
    :param c:
    :return:
    '''
    if a == 0:
        raise ValueError('参数错误')
    elif b * b - 4 * a * c < 0:
        raise ValueError('方程再有理数范围无解')
    elif b * b - 4 * a * c == 0:
        return -b / (2 * a)
    else:
        r1 = (-b + (b * b - 4 * a * c) ** 0.5) / 2 / a
        r2 = (-b - (b * b - 4 * a * c) ** 0.5) / 2 / a
        return r1, r2