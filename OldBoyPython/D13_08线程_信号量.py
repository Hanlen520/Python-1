#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/23 15:04
# FileName: D13_08线程_信号量.py
# Description:
#   信号量：semaphore 是用于控制线程并发数的
# Question:
# --------------------------------------

import threading
import time


class MyThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(5)
            semaphore.release()


if __name__ == "__main__":
    semaphore = threading.BoundedSemaphore(5)
    thrs = []
    for i in range(100):
        thrs.append(MyThread())
    for t in thrs:
        t.start()


