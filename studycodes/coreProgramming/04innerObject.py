#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: .py
# author: jiangheng
# description:
# questions:



# 两个变量表象---指向了相同的整数对象
# 我们会希望 a 与 b 能和 c 与 d 一样，因为我们本意就是为了创建两个整数对象
a1 = 1
print("查看a4变量的内存索引地址：", id(a1))
b1 = 1
print("查看b1变量的内存索引地址：", id(b1))

a2 = 1.01
print("查看a2变量的内存索引地址：", id(a2))
b2 = 1.01
print("查看b2变量的内存索引地址：", id(b2))


# --------- 4.6.3 str()和 repr() (及 `` 运算符)
# print 语句结合 str() 函数实际上是调用了对象的 __str__ 方法来输出结果。
# 而 print 结合 repr() 实际上是调用对象的 __repr__ 方法输出结果
print(str('123'))
print(str(123))
print('123'.__str__())
print(repr('123'))
print(repr(123))
print('123'.__repr__())
print(eval('type(type)'))


# -------- 4.6.4 type() 和 isinstance()
print(type(''))
s = 'String'
print(type(s))
print(type(100))
print(type(0+0j))
print(type(0.0))
print(type([]))
print(type(()))
print(type({}))
print(type(type))


class Foo:
    pass


foo = Foo()


class Bar(object):
    pass


bar = Bar()
print(type(Foo))
print(type(foo))
print(type(Bar))
print(type(bar))

