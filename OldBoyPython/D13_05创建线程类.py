#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/23 12:07
# FileName: D13_05创建线程类.py
# Description: 
# Question:
# --------------------------------------

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("Running num is: %s" % self.num)
        time.sleep(3)


if __name__ == "__main__":
    t1 = MyThread(1)
    t2 = MyThread(2)

    t1.start()
    t2.start()

