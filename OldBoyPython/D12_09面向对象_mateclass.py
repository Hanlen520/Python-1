#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/19 7:51
# FileName: D12_09面向对象_mateclass.py
# Description:
#       python中一切皆对象
#       类创建对象时执行步骤如下代码流程
# Question:
# --------------------------------------


class MyType(type):
    def __init__(self, *args, **kwargs):
        print('...123...')

    def __call__(self, *args, **kwargs):
        print("...456...")


class Foo(object, metaclass=MyType):
    def __init__(self):
        self.name = 'tester'

    def __new__(cls, *args, **kwargs):
        print("...789...")

    def func(self):
        print('Foo...func')


# ===============================
def func():
    print('1213')


Foo2 = type('Foo', (object,), {'func': func})

# f 是 Foo类的对象
# Foo类是type的对象----> 类都是type的对象
f = Foo()






