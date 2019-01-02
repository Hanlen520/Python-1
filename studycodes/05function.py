#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 05function.py
# author:
# description:

# ---------------------------*************调用函数*************---------------------------
# 调用函数
print(abs(-1))
print(max(-1, 0, -5, 9))

# 数据类型转换
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋值给一个变量，相当于给这个函数起了一个“别名”
print(int(12.34))
print(float('12.34'))
print(bool(1))
print(bool(0))

a = abs
print(a(-1))


# ---------------------------*************定义函数*************---------------------------
# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号；然后，在缩进中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-1))

# ---------------------------*************函数的参数*************---------------------------
# 位置参数


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(3, 3))


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 多参数时，默认参数可以降低复杂度，如下：
def enroll(name, age, city="beijing", job="developer"):
    print('name', name)
    print('age', age)
    print('city', city)
    print('job', job)


# 定义默认参数的时候：默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())


def add_end(L=None):
    if L is None:
        L = []
    L .append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())

# 分析：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，
# 它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了


# 可变参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    total = 0
    for n in numbers:
        total = total + n * n
    return total


print(calc(1, 2))


# 关键字参数
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


print(person('gyf', 22, city='Beijing'))
extra = {'city': 'Beijing', 'job': 'Tester'}
print(person('gyf', 23, city=extra['city'], job=extra['job']))
print(person('gyf', 22, **extra))


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，至于到底传入了那些，就需要在函数内部通过kw检查
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分割符*, *后面的参数被视为命名关键字参数
def person01(name, age, *, city, job):
    print(name, age, city, job)


def person02(name, age, *, city='shanghai', job):
    print(name, age, city, job)


print(person01('Jack', 24, city="Beijing", job='Engineer'))
print(person02('Bob', 23, job="Tester"))


# 参数组合
# 在python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数这5种参数组合使用
# 但参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


print(1, 2)


# ---------------------------*************递归函数*************---------------------------
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，此函数就是递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)


print(fact(1))
print(fact(5))


# 使用递归函数要注意防止栈(stack)溢出
# 解决递归调用栈溢出的方法是通过尾递归优化
# 尾递归：函数返回时，调用自身本身，并且return语句不能包含表达式。这样编译器使递归本身无论调用多少次都只占用一个栈帧，不会出现栈溢出
def fact1(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return 1
    return fact_iter(num - 1, num * product)

