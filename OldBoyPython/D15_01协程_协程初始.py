#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/24 21:50
# FileName: D15_01协程_协程初始.py
# Description:
#   协程，又称微线程。协程是一种用户态的的轻量级线程
#   协程用于自己的寄存器上下文和栈
#   协程的好处：
#       无需线程上下文切换的开销
#       无需原子操作锁定及同步的开销
#       方便切换控制流，简化编程模型
#       高并发 + 高扩展 + 低成本：一个CPU上上万的协程不是问题，所以很适合处理高并发
#   缺点：
#       无法使用多核，但是可以通过进程＋协程进行解决
#
# Gevent-----实现任务之间的切换
#
# Question:
# --------------------------------------

import time
import queue


def customer(name):
    pass


def producer():
    pass


if __name__ == "__main__":
    cu1 = customer("C1")
    cu2 = customer("C2")
    p = producer()
