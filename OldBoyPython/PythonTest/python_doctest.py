#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 11:51
# FileName: python_doctest.py
# Description: 所谓文档测试，指的是通过 python 的 doctest 模块运行 python 源文件的说明文档中的测试用例，从而生成测试报告；文档测试工具可以提取说明文档中的测试用例，其中 ">>>" 之后的内容表示测试用例，接下来的一行则表示该测试用例的输入结果
# 文档测试工具会判断测试用例的运行结果与输出结果是否一致，如果不一致就会显示错误信息。
# Question: 
# --------------------------------
import doctest

def square(x):
    '''
        一个可以计算平方的函数

    >>> square(2)
    4
    >>> square(3)
    9
    >>> square(-2)
    4
    >>> square(0)
    1
    '''

    return x * 2   # 此处故意写错的


class User:
    '''
    定义一个代表用户的类，该类包含两个属性：
    name - 用户的名字
    age - 用户的年龄

    >>> u = User('abc', 9)
    >>> u.name
    abc
    >>> u.age
    9
    >>> u.say('这是我说的话')
    'abc say: 这是我说的话'
    '''
    def __init__(self, name, age):
        self.name = 'ABC'  # 此处故意写错的
        self.age = age

    def say(self, content):
        return self.name + ' say: ' + content


if __name__ == "__main__":
    doctest.testmod()
