#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0102_doctest.py
@Time    :   2019/8/17 15:48
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import doctest


class User:
    """
    定义一个代表用户的类，该类包含两个属性：
    name - 用户的名字
    age - 用户的年龄

    >>> u = User('abc', 9)
    >>> u.name
    'ABC'
    >>> u.age
    9
    >>> u.say()
    'abc 说，我今年 10 岁了。'
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return "%s 说，我今年 %s 岁了。" % (self.name, self.age)


if __name__ == "__main__":
    # testmod() 函数会自动提取该模块的说明文档中的测试用例，并执行这些测试用例，最终生成测试报告。
    # 如果存在没有通过的测试用例，程序就会显示有多少个测试用例没有通过；如果所有测试用例都通过测试，则不生成任何输出结果。
    doctest.testmod()
