#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/22 13:39
# FileName: D13_04Python的GIL.py
# Description:
#       如果任务是IO密集型的话，可以用多线程
#       如果任务是计算密集型的，建议用C
#   守护线程：
#       当主线程运行完了守护的那个还没有干掉，主线程等非守护线程全都结束它才结束
# Question: 
# --------------------------------

from multiprocessing import Process
from threading import Thread
import time, os


def talk1():
    time.sleep(2)
    print("开始talk1的线程")
    for i in range(2):
        print("talk1.....11111")
    print("结束talk1的线程")


def talk2():
    time.sleep(3)
    print("开始talk2的线程")
    for i in range(3):
        print("talk2.....22222")
    print("结束talk2的线程")


if __name__ == "__main__":
    t1 = Thread(target=talk1)
    t2 = Thread(target=talk2)

    # 守护线程
    # t1.daemon = True

    # 执行各个子线程
    t1.start()
    t2.start()

    print("主线程：", os.getpid())














