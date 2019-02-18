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
# Question:
# --------------------------------------


class Test:

    # 类属性（类字段：保存在类里面的，执行时可以通过对象访问也可以通过类访问）
    country = "CN"

    # 构造方法
    def __init__(self):
        # 属性（普通字段：保存在对象里面的，执行时只能通过对象访问）
        self.name = 'a'

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

    # 不伦不类的属性 ===》t1.per
    # 此处主要是对属性的访问
    @property
    def per(self):
        # print("per")
        return 1

    # 此处主要是对属性的赋值设置操作
    @per.setter
    def per(self, val):
        print(val)

    #
    @per.deleter
    def per(self):
        return "是否真正删除了"


t1 = Test()
# 对象访问静态属性
print(t1.country)
# 类访问静态属性
print(Test.country)
# 类直接访问静态方法
print(Test.static_method())
# 对象访问构造方法里面的普通字段
# print(t1.name)

# 不伦不类的属性的访问
p = t1.per
print(p)
# 不伦不类的属性它也是属性，如果相对属性赋值，则需
t1.per = "通过per.setter给不伦不类的属性设的值"
del t1.per




