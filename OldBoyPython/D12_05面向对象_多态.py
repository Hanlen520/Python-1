#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/17 21:01
# FileName: D12_05面向对象_多态.py
# Description:
#       Python天生就是多态的
# Question:
# --------------------------------------


class Test(object):

    def foo(self, args):
        print(args)


# 可以对比着Java面向对象多态来看
# Python由于部用指定属性值的数据类型，所以天生就是多态的
t1 = Test()
t1.foo('string')
t1.foo(123)
t1.foo(123.3333)
t1.foo(-1)




