#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0202_testsuite.py
@Time    :   2019/8/18 17:43
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
import unittest


def say():
    return "Hello Python"


def func_add(a, b):
    return a + b


def func_error(a):
    return a


def func_skip():
    return "skip这个方法"


class TestSay(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("TestSay开始测试固件...")

    def test_say(self):
        self.assertEqual(say(), "Hello")

    @classmethod
    def tearDownClass(cls) -> None:
        print("TestSay结束测试固件...")


class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("TestAdd开始测试固件...")

    def test_func_add(self):
        self.assertEqual(func_add(1, 2), 3)
        self.assertEqual(func_add(1, -2), -1)
        self.assertEqual(func_add(-1.5, -2), -3.5)

    def test_error(self):
        self.assertEqual(func_error(2), -2)

    @unittest.skip('这条测试用例跳过不执行')
    def test_skip(self):
        self.assertEqual(func_skip(), 'skip这个方法')

    @classmethod
    def tearDownClass(cls) -> None:
        print("TestAdd结束测试固件...")


# 测试用例管理
testCases = (TestSay, TestAdd)


def whole_suite():
    # 创建测试加载器
    loader = unittest.TestLoader()

    # 创建测试包
    suite = unittest.TestSuite()

    # 遍历所有测试类
    for testCase in testCases:
        # 从测试类中加载测试用例
        tests = loader.loadTestsFromTestCase(testCase)
        # 将测试用例加到测试包中
        suite.addTests(tests)

    return suite


if __name__ == "__main__":
    with open('0202_testsuite_report.txt', 'a') as f:
        # 创建测试运行器（TestRunner）
        # verbosity=2 生成更详细的测试报告
        runner = unittest.TextTestRunner(verbosity=2, stream=f)
        runner.run(whole_suite())
