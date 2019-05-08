#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 20:09
# FileName: test_fixture.py
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
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(-3, 0), -3)

    @classmethod
    def setUpClass(cls) -> None:
        print('\n=====执行 setUp 模拟初始固件 =====')

    @classmethod
    def tearDownClass(cls) -> None:
        print('\n=====执行 setUp 模拟模拟固件 =====')