#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 17:40
# FileName: test_hello.py
# Description: 
# Question: 
# --------------------------------

import unittest
from .hello import *

class TestHello(unittest.TestCase):
    # 测试 say_hello() 函数
    def test_say_hello(self):
        self.assertEqual(say_hello(), 'Hello Python')

    # 测试 add() 函数
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-3, 7), 4)
        self.assertEqual(add(0, -3), -3)
