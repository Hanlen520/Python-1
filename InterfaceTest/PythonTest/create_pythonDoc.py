#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 10:31
# FileName: create_pythonDoc.py
# Description: 
# Question: 
# --------------------------------

My_NAME = 'PYDOC学习'

def say_hi(name):
    '''
        定义一个打招呼的函数
        返回对指定用户进行打招呼
    '''
    print('执行函数')
    return 'HELLO' + 'name'

def print_rect(height, width):
    '''
        定义一个打印矩形的函数
        height - 代表矩形的高
        width - 代表矩形的宽
    '''
    print(('*' * width + '\n') * height)


class User:
    '''
        定义一个代表用户的类
        该类包括name, age两个变量
    '''
    def __init__(self, name, age):
        '''
            name初始化该用户的name
            age初始化该用户的age
        '''
        self.name = name
        self.age = age

    def introduce_myself(self):
        '''
            定义了用户进行自我介绍的方法
        '''
        print('我叫 %s， 我今年 %d 岁' % (self.name, self.age))


