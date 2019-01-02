#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 06.seniorfeature.py
# author:
# description:

# ---------------------------*************切片*************---------------------------
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)

L = ['A', 'B', 'C', 'D']
for i in L:
    print(i)

r = []
n = 100
for i in range(n):
    r.append(i)
print(r)
# 取前3个元素
print(r[0:3])
print(r[:3])
# 倒着切片
print(r[-3: -1])
# 取后10个数
print(r[-10:])
# 字符串切片
print('ABCDEFG'[: 2])


# ---------------------------*************迭代*************---------------------------
# 如果给定一个list(tuple、dict)，可以通过for循环来遍历这个list或tuple，这种遍历成为迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

# 通过collections模块的Iterable类型判断一个对象是不是可迭代对象：
from collections import Iterable
if isinstance('abc', Iterable) == True:
    print("Yes")
if isinstance(123, Iterable) == True:
    print("Yes")

# 用Python的内置enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


# ---------------------------*************列表生成式*************---------------------------
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print(list(range(1, 11)))

L = []
for i in range(1, 11):
    L.append(i * i)
print(L)
print([x * x for x in range(2, 12)])
print([x * x for x in range(1, 11) if x % 2 == 0])

# 生成二维数组的全排列
print([m + n for m in 'ABC' for n in 'XYZ'])
# 列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])


# ---------------------------*************生成器*************---------------------------
# 生成器出现的缘由：
#       通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
#       而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
#       那后面绝大多数元素占用的空间都白白浪费了。
# 只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
for n in g:
    print(n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


print(next(fib(6)))



# ---------------------------*************迭代器*************---------------------------





