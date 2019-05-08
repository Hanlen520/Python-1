#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 20:41
# FileName: test_skip.py
# Description: 
# Question: 
# --------------------------------
import unittest

from hello import *

class TestHello(unittest.TestCase):
    # 测试 say_hello() 函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), 'Hello Python')

    # 测试 add() 函数
    @unittest.skip('临时跳过 test_add')
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-3, 0), -3)

    def test_print(self):
        self.skipTest("临时跳过 test_print")
        print("我是否被跳过执行，我想看看")