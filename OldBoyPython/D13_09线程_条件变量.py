#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/23 16:45
# FileName: D13_09线程_条件变量.py
# Description:
#       有一类线程需要满足条件之后才能够继续执行
#       python提供了threading.Condition对象用于条件变量的支持
#       它提供了RLock() Lock() wait()  notify()  notifyAll()方法
# Question:
# --------------------------------------

import threading


