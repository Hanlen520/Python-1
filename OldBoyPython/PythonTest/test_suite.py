#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/5 17:46
# FileName: test_suite.py
# Description: 
# Question: 
# --------------------------------

import unittest

from PythonTest.python_unittest import TestFkMath
from PythonTest.test_hello import TestHello

test_cases = (TestHello, TestFkMath)

def whole_suite():
    # 创建测试加载器
    loader = unittest.TestLoader()

    # 创建测试包
    suite = unittest.TestSuite()

    # 遍历所有测试类
    for test_class in test_cases:
        # 从测试类中加载测试用例
        tests = loader.loadTestsFromTestCase(test_class)
        # 将测试用例添加到测试包中
        suite.addTests(tests)
    return suite


if __name__ == "__main__":
    with open('test_report.txt', 'a') as f:
        # 创建测试运行器（TestRunner），并将测试报告输出到文件中
        runner = unittest.TextTestRunner(verbosity=2, stream=f)
        runner.run(whole_suite())