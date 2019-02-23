#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/23 17:00
# FileName: D13_10线程_Event.py
# Description:
#       from threading import Event
#       Event.isSet()  # 返回event的状态值
#       Event.wait()  # 如果 event.isSet()==False将阻塞线程；
#       Event.set()  # 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
#       Event.clear()  # 恢复
# Question:
# --------------------------------------


# 模拟红绿灯控制车辆通行
from threading import Event, currentThread, Thread
import time

e = Event()


def traffic_lights():
    # 红绿灯
    time.sleep(5)
    e.set()


def car():
    print("\033[42m %s 等绿灯\033[0m" % currentThread().getName())
    e.wait()
    print("\033[44m %s 等绿灯\033[0m" % currentThread().getName())


if __name__ == "__main__":

    # 有10辆车
    for i in range(10):
        t_car = Thread(target=car)
        t_car.start()

    traffic_thread = Thread(target=traffic_lights)
    traffic_thread.start()






