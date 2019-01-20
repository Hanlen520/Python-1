#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/20 14:39
# FileName: D10_04生成器.py
# Description: 
# Question:
# --------------------------------------


# 1. 生成器的创建
# 1.1 ()来创建生成器
generator_a = (x * x for x in range(5))
print(generator_a)        # <generator object <genexpr> at 0x00000240CD15A408>


# 1.2 通过关键词yield
def foo():
    print("OK1")
    yield 1

    print("OK2")
    yield 2

    return None


g = foo()
foo_a = next(g)
foo_b = next(g)
print("foo_a: ", foo_a)
print("foo_b: ", foo_b)


# 2. 生成器取值 0 ~ 5: 左包含右不包含
# 2.1 python3是通过特殊的变量__next__(python2: next())来取值的
print("Zero: ", generator_a.__next__())
print("One: ", generator_a.__next__())
print("Two: ", generator_a.__next__())
print("Three: ", generator_a.__next__())
print("Four: ", generator_a.__next__())
# print("Five: ", generator_a.__next__())       # StopIteration 代表着生成器取值已经超出可生成的范围了
# 2.2 通常是用for循环来取值的
for i in generator_a:
    print("%s: %s" % (i, i))


# 3. 生成器节省内存的原理
# Python中内存的回收机制是：当变量不再引用内存对象时，内存中的对象将会被python的解释器回收
# 例如：
# 第一次：   generator_a.__next__() 指向内存中的 0
# 第二次：   generator_a.__next__() 指向内存中的 1    ----- 0 不再被python中的变量引用了，那么就被回收了
# 第三次：   generator_a.__next__() 指向内存中的 4    ----- 1 不再被python中的变量引用了，那么就被回收了
# ......


# 4. 什么时可迭代对象
#   for 循环后面跟的都是可迭代对象
#   可迭代对象都有__iter__方法
#   常见的几种数据类型中：列表、元组、字典均是可迭代对象


# 5. 生成器改造斐波拉契数列
def fibo(max):
    n, before, after = 0, 0, 1
    while True:
        yield before
        before, after = after, before + after
        n = n + 1


g2 = fibo(5)
print(g2)   # <generator object fibo at 0x000001A7F5BFA4F8>
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))
print(next(g2))


# 6. 生成器中的next()和send()详解
def foo6():
    print("OK6")
    counter = yield 6
    print(counter)

    print("OK7")
    yield 7

    return None


f6 = foo6()
r6 = f6.send(None)      # next(), 第一次send前如果没有next，只能传一个send(None)
print(r6)
f6.send("变变变...")


# 7. 通过yield实现在单线程的情况下实现并发运算的效果---伪并发
#  yield在协程中使用的比较多



