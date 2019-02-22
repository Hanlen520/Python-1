#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/22 9:53
# FileName: D13_03线程进程.py
# Description:
#   线程：线程是操作系统能够执行调度的最小单位，它被包含在进程之中，是进程中的实际运作单位。
#         python创建线程使用threading模块
#
#
#   进程：
# Question: 
# --------------------------------

import time
import threading

start_time = time.time()

def foo(n):
    print("foo %s" % n)
    time.sleep(1)
    print("...end foo...")

def bar(n):
    print("bar %s" % n)
    time.sleep(2)
    print("...end bar...")

# 按顺序执行
# foo()
# bar()

# 创建线程并行执行
t1 = threading.Thread(target=foo, args=(1, ))
t2 = threading.Thread(target=bar, args=(2, ))
t1.start()
t2.start()
# 保证两个线程执行完再执行下面的事件计算
t1.join()
t2.join()
print("\n....................................")

end_time = time.time()
print("耗时:", end_time - start_time)