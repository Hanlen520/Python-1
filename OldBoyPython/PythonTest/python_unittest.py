#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 14:44
# FileName: python_unittest.py
# Description: 
# Question: 
# --------------------------------

import unittest

from python_unittest_function import one_equation
from python_unittest_function import two_equation

class TestFkMath(unittest.TestCase):
    # 测试一元一次方程求解
    def test_one_equation(self):
        # 断言该方程求解应该为 -1.8
        self.assertEqual(one_equation(5, -9), -1.8)
        # 断言该方程求解应该为 -2.5
        self.assertTrue(one_equation(4, -10) == -2.5, .00001)
        # 断言该方程求解应该为 27/5
        self.assertTrue(one_equation(4, 27) == 27/4)
        # 断言当 a == 0时，断言引发 ValueError
        with self.assertRaises(ValueError):
            one_equation(0, 9)

    # 测试一元二次方程求解
    def test_two_equation(self):
        r1, r2 = two_equation(1, -3, 2)
        self.assertCountEqual((r1, r2), (1.0, 2.0), '求解错误')
        r1, r2 = two_equation(2, -7, 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解错误')
        # 断言只有一个解的情形
        r = two_equation(1, -4, 4)
        self.assertEqual(r, 2.0, '求解错误')
        # 断言当 a == 0 时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(0, 9, 3)
        # 断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(4, 2, 3)

if __name__ == "__main__":
    unittest.main()