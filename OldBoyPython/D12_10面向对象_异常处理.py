#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/19 8:14
# FileName: D12_10面向对象_异常处理.py
# Description: 
# Question:
# --------------------------------------


def foo1():
    return False


def foo2():
    try:
        # 代码块（逻辑）
        value = input("请输入自然数")
        value = int(value)
        # 主动触发异常...一般用于函数嵌套的应用场景中
        result = foo1()
        if not result:
            raise Exception("主动触发异常...")
    except Exception as e:
        # e时Exception对象，对象封装了错误信息
        # 如果上述代码块出错，自动执行当前代码块
        print(e)
        value = 1
    else:
        print("......")
    finally:
        print("肯定会执行的部分...")
    print(value)


# 自定义异常
class MyException(Exception):
    def __int__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


me1 = MyException("执行我的自定义异常")


def act_exception():
    try:
        raise MyException("我是自定义异常，我被触发了")
    except Exception as e:
        print(e)


act_exception()


# 断言: assert + 条件-------用于用户强制执行，不服从就报错，一般不捕获
print(123)
assert 1 == 2
print(456)