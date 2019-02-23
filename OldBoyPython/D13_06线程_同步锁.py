#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/23 13:57
# FileName: D13_06线程_同步锁.py
# Description: 
# Question:
# --------------------------------------

import threading
import time

r = threading.Lock()


def reduce_num():
    global num

    # final num is:  99
    # 加锁
    r.acquire()
    temp = num
    time.sleep(0.0001)
    # print("ok......")
    num = temp - 1
    r.release()


num = 100

thread_list = []
for i in range(100):
    t = threading.Thread(target=reduce_num)
    t.start()
    thread_list.append(t)

# 等待所有线程处理完成
for i in thread_list:
    t.join()


print("final num is: ", num)







