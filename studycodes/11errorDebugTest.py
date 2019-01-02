#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 11errorDebugTest.py
# author:
# description:


# ------------------------**********错误处理*********-----------------------------
# 可以使用错误码，对特定的错误赋值返回特定的数字标识
# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     try:
#         bar('5')
#     except Exception as e:
#         print('Error', e)
#     finally:
#         print('finally...')
#
#
# try:
#     # print("try......")
#     # r = 10 / int('a')
#     # print("result: ", r)
#     foo('5')
# except ValueError as v:
#     print('ValueError: ', v)
# except ZeroDivisionError as e:
#     print("except:", e)
# finally:
#     print("finally...")
# print("END")


# 断言
def cutSpeak(s):
    n = int(s)
    # assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    assert n != 0, 'n is ZERO!'
    return 10 / n


def main():
    cutSpeak('0')


# logging
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


# pdb


# pdb.set_trace()


# ------------------------**********单元测试*********-----------------------------
# 为了编写单元测试，我们需要引入Python自带的unittest模块
# 以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
# 一旦编写好单元测试，我们就可以运行单元测试。
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value




import unittest


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


# ------------------------**********文档测试*********-----------------------------





