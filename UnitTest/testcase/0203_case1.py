#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0203_case1.py
@Time    :   2019/8/28 22:05
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import unittest


class CaseOne(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('测试前执行')

    @classmethod
    def tearDownClass(cls) -> None:
        print('测试后执行')

    def test_case11(self):
        print("test_case11")

    @unittest.skip
    def test_case12(self):
        print("test_case12")

    def test_case13(self):
        print("test_case13")


if __name__ == "__main__":
    # unittest.main()
    # 创建测试容器
    suite = unittest.TestSuite()
    # 添加测试用例到测试容器中
    suite.addTest(CaseOne('test_case11'))
    suite.addTest(CaseOne('test_case12'))
    suite.addTest(CaseOne('test_case13'))
    # 执行容器里的测试用例
    unittest.TextTestRunner().run(suite)
