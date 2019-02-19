#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/18 22:54
# FileName: D12_08面向对象_特殊成员.py
# Description: 
# Question:
# --------------------------------------


class Foo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__")

    def __call__(self, *args, **kwargs):
        print("__call__")

    def __int__(self):
        return 1212

    def __str__(self):
        return "%s - %s"%(self.name, self.age)

    def __getitem__(self, item):
        return item + 10

    def __setitem__(self, key, value):
        print(key, value)

    def __delitem__(self, key):
        print(key)


f1 = Foo('Tester', 18)
f1()
f2 = Foo("Developer", 24)
f2()
# 等价于下面
# Foo('Tester', 18)()

print(f1, type(f1))
# int,对象------自动执行对象的__init__方法，并将返回值赋值给int对象
r_int = int(f1)
print(r_int)
r_str = str(f1)
print(r_str)

# self ≡ f1, f2作为参数传入到f1中去
# r_f1f2 = f1 + f2
# print(r_f1f2)

# 对象访问值
li = Foo("Lister", 23)
r_list = li[8]
print(r_list)
# 对象设置值
li["setter"] = 100
# 对象删除值
del li["delitem"]




