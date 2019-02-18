#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/15 8:06
# FileName: D12_03面向对象_封装.py
# Description: 
# Question:
# --------------------------------------
class Person(object):
    # 构造方法：类名() --- 会自动执行构造方法
    def __init__(self, name, age, sex):
        print("自动执行构造方法")
        self.name = name
        self.age = age
        self.sex = sex

    # 类方法
    def eat(self):
        print(self, self.name)

# 实例化对象
#   p1 = Person() 做了两件事
#       创建对象
#       通过对象执行类中的一个特殊方法
p1 = Person()
print(p1)
print(p1.eat('apple'))      # 由此退出self指的就是实例化对象本身
print("=============================")
p2 = Person()
print(p2)
print(p2.eat('orange'))

