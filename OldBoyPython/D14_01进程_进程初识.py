#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/24 19:16
# FileName: D14_进程初识.py
#   由于GIL的存在，Python的多线程并不是真正的多线程
# Description: 
# Question:
# --------------------------------------

import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

# 创建进程
    def run(self):
        time.sleep(1)
        print("Hello", self.name, time.ctime())


if __name__ == "__main__":
    p_list = []
    for i in range(3):
        p = MyProcess("Test")
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()
