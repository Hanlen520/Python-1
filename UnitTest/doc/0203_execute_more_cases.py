#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0203_execute_more_cases.py
@Time    :   2019/8/28 22:00
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   这里批量的测试用例指的是 "../testcase/ " 目录下的测试用例们
"""

import unittest
import os


class ExecuteMoreCases(unittest.TestCase):

    def test_execute(self):
        # 当前目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)  # D:\MySpace\Python\WebTesting\util
        cases_dir = os.path.join('../testcase/')
        print(cases_dir)
        suite = unittest.defaultTestLoader.discover(cases_dir, '00203_case1.py')
        unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    unittest.main()

