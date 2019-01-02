#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 07functionalProgramming.py
# author:
# description:

# ---------------------------**************高级函数************---------------------------
# 函数是python内建支持的一种封装，把大段代码拆成函数通过一层一层的函数调用，把复杂任务分解为简单的任务
# 这种分解成为面向过程的程序设计，函数就是面向过程的程序设计基本单元
# 函数式编程的特点：允许把函数本身作为参数传入另一个函数，还允许返回一个函数！


# map/reduce
# map()函数接受两个参数，一个是函数，一个是Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# map内部实际上用的是生成器
def double(x):
    return x * x


r = map(double, [1, 2, 3, 4, 5, 6])
print(list(r))
print(list(map(double, [1, 2, 3, 4, 5, 6])))
print(list(map(str, [1, 2, 3, 4, 5, 6])))


# reduce，把一个函数作用在一个序列[x1, x2, x3, ...]，这个函数必须接受两个参数，reduce会把结果继续和序列的下一个元素做累积
from functools import reduce


def my_add(x, y):
    return x + y


print(reduce(my_add, [1, 2, 3, 4, 5]))

# 把序列[9, 8, 7, 6, 5, 4, 3, 2, 1]变换成整数987654321


def my_integer(x, y):
    return x * 10 + y


print(reduce(my_integer, [9, 8, 7, 6, 5, 4, 3, 2, 1]))


def my_charnum(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


print("======================================================")
print(list(map(my_charnum, '0000000')))
print(reduce(my_integer, map(my_charnum, '123456')))

# 将字符串str转换为整数int
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


print(str2int('1234'))

# filter
# Python内建的filter()函数用于过滤序列
# filter()接受一个函数和一个序列
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))


def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


# filter求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# sorted
print(sorted([36, 5, -12, 9, -21]))
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
print(sorted([36, 5, -12, 9, -21], key=abs))
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# ---------------------------**************返回函数************---------------------------
# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# 实现可变参数求和：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 不需要返回求和结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum


print("====================lazy_sum========================")
print(lazy_sum(1, 2, 3, 4, 5))
f = lazy_sum(1, 2, 3, 4, 5)
print(f())
# 上面的例子，在函数lazy_sum()中定义了函数sum()，内部函数sum()可以引用外部函数lazy_sum()的参数和局部变量，当lazy_sum()
#  函数返回sum()时，相关参数和变量都保存在返回函数中，这种成为--闭包（这种程序结构拥有极大的威力）

# 注意：当调用lazy_sum()时，每次调用都会返回一个新的函数吗，即使传入相同的参数
# f1()和f2()的调用结果互不影响
f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print(f1 == f2)


# 闭包
# 返回函数在其定义内部引用了坚决不变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# 返回函数不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用循环变量--------创建一个新的函数，用该函数的参数绑定循环变量当前的值
# 无论该循环变量后续如何更改，已绑定到函数的值不变
def my_count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))    # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# ---------------------------**************匿名函数************---------------------------
# 在传入函数是，不需要显式地定义函数，直接传入匿名函数更方便
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))

# 优点：
# 1. 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
# 2. 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(5))


# 3. 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda x: x * x + y * y


# 判断是否是奇数的原函数：
def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, range(1, 20)))
print(L)


# 使用匿名函数改造原函数
f = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(f)


# ---------------------------**************装饰器************---------------------------
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以通过变量也能调用该函数
def now():
    print('2018-07-21')


f = now
print(f())

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)


# 如果要增强now()函数的功能，比如在函数调用前后自动打印日志，但又不希望修改now()函数的定义
# 这种在代码运行期间动态增加功能的方式，称之为----装饰器
# 本质上，decorator就是一个返回函数的高阶函数。所以要定义一个能打印日志的decorator
def my_log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper


# @my_log()
# def now():
#     print('201807211405')


# ---------------------------**************偏函数************---------------------------
# python的functools模块提供了很多功能，其中一个就是偏函数(Partial function)
# 在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
print(int('123'))
print(int('123', base=8))
print(int('123', base=16))


# 定义进制转换函数，方便转换
def int8(x, base=8):
    return int(x, base)


print(int8('123'))

# ===========>>
# 简单总结functools.partial的作用就是，把一个函数的某些参数给固定住(也就是设定默认值), 返回一个新的函数，这样调用新函数更简单
import functools
int80 = functools.partial(int, base=8)
print(int80('123'))


# 实际上，创建偏函数时可以接受函数对象、*args、**kwargs这3个参数
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单