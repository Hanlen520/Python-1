#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0203_case2.py
@Time    :   2019/8/28 22:17
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import unittest


class CaseTwo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试之前执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试之后执行")

    def test_case21(self):
        print('test_case21')

    def test_case22(self):
        print('test_case22')

    @unittest.skip
    def test_case23(self):
        print('test_case23')

    def test_case24(self):
        print('test_case24')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CaseTwo('test_case21'))
    suite.addTest(CaseTwo('test_case22'))
    suite.addTest(CaseTwo('test_case23'))
    suite.addTest(CaseTwo('test_case24'))
    unittest.TextTestRunner().run(suite)
