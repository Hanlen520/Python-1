#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/17 21:50
# FileName: D12_06面向对象类的知识.py
# Description:
#    应用场景：
#         如果对象中需要保存一些值，执行某些功能的时候，需要使用对象中的值 =====》 普通方法
#         不需要任何对象中的值 ===》静态方法
#
# Question:
# --------------------------------------


class Test(object):

    # 类属性（类字段：保存在类里面的，执行时可以通过对象访问也可以通过类访问）
    country = "CN"

    # 构造方法
    def __init__(self, name):
        # 属性（普通字段：保存在对象里面的，执行时只能通过对象访问）
        self.name = name

    # 普通方法：保存在类中，执行中一般用对象来调用，但是也可以用类来调用但一般不用
    # self---对象
    def area(self):
        print("我是普通方法")

    # 静态方法
    @staticmethod
    def static_method():
        print("123")

    # 类方法: cls--当前类
    @classmethod
    def class_method(cls):
        # cls是类名
        print(cls)
        print("class_method")


t1 = Test
print(t1.country)
print(Test.static_method())