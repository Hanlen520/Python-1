#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/23 17:37
# FileName: D13_11线程_Queue.py
# Description:
#   队列的出现是为了解决列表线程不安全的问题
#   队列: FIFO(先进先出)
# Question:
# --------------------------------------

import queue

# 队列: FIFO(先进先出)
q1 = queue.Queue(5)
q1.put("1")
q1.put("2")
q1.put("3")
print(q1.get())
print(q1.get())
print(q1.get())


# 队列: FILO(先进后出)
q2 = queue.LifoQueue()
q2.put("First")
q2.put("Second")
q2.put("Third")
print(q2.get())
print(q2.get())
print(q2.get())

# 队列: 设置优先级队列, 数字越小优先级越高
q3 = queue.PriorityQueue()
q3.put(20, "b")
q3.put(10, "a")
q3.put(30, "c")
print(q3.get())
print(q3.get())
print(q3.get())








