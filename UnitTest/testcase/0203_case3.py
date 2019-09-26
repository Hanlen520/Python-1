#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0203_case3.py
@Time    :   2019/8/28 22:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import unittest


class CaseThree(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("测试之前执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("测试之后执行")

    def test_case31(self):
        print('test_case21')

    def test_case32(self):
        print('test_case22')

    def test_case33(self):
        print('test_case23')

    def test_case34(self):
        print('test_case24')


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CaseThree('test_case31'))
    suite.addTest(CaseThree('test_case32'))
    suite.addTest(CaseThree('test_case33'))
    suite.addTest(CaseThree('test_case34'))
    unittest.TextTestRunner().run(suite)
