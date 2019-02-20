#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/20 13:34
# FileName: D12_12面向对象_单例模式.py
# Description: 
# Question: 
# --------------------------------
class Foo:
    static_value = "静态字段"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return "%s - %s" % (self.name, self.age)

# f1叫对象，f1也叫做Foo类的实例（实例化的过程）
f1 = Foo("Tester1", 23)
f2 = Foo("Tester2", 24)
f3 = Foo("Tester3", 25)

# 单例模式：就是不用每次创建一个新的对象，循环使用一个创建对象
# v = None
#
# while True:
#     if v:
#         v.show_info()
#     else:
#         v = Foo("Tester_v", 23)
#         v.show_info()

# 改造单例模式的写法
class FooV:
    __v = None

    # 类方法，cls就指的是当前类
    @classmethod
    def get_instance(cls):
        if cls.__v:
            return cls.__v
        else:
            cls.__v = FooV()
            return cls.__v

# 以下三个创建的对象是一模一样的，就是单例模式
fv1 = FooV.get_instance()
print(fv1)
fv2 = FooV.get_instance()
print(fv2)
fv3 = FooV.get_instance()
print(fv3)

# 单例模式的应用
#   应用于数据库连接，数据库连接特别的耗时耗资源
#       不同的请求都是需要请求数据库的，因此只需要一个单例模式对象就行了（一个数据库连接池就行了）


