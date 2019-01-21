#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/21 9:49
# FileName: D11_01模块time.py
# Description: 
# Question: 
# --------------------------------

import time
import datetime

# 1.利用help函数查看time函数的使用方法
print(help(time))


# time.time()打印自1970年1月1日00:00:00起走过的秒数
# 2.timestamp时间戳
print(time.time())

# time.sleep(3)
# DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
# 3.082753
#   print(time.clock())
# print(time.clock())
# 3.CPU计算时间
print(time.perf_counter())
print(time.process_time())

# 4. time.gmtime()
# UTC结构化时间，所谓的世界标准时间
# time.struct_time(tm_year=2019, tm_mon=1, tm_mday=21, tm_hour=7, tm_min=51, tm_sec=58, tm_wday=0, tm_yday=21, tm_isdst=0)
print("gmtime:", time.gmtime())

# 5. localtime本地时间
# 当前即取的东八区的时间
print(time.localtime())

# 6. strftime()
# 格式化时间 print(help(time.strftime))
local_time = time.localtime()
print("strftime: ", time.strftime("%Y-%m-%d %H:%M:%S", local_time))

# 7. strptime()
# 将本地时间形式转换成结构化的时间格式
local_time2 = time.localtime()
print("strptime: ", time.strptime("2019-01-21 16:12:54", "%Y-%m-%d %H:%M:%S"))
# 8.取结构化时间中某块的时间
a8 = time.strptime("2019-01-21 16:12:54", "%Y-%m-%d %H:%M:%S")
print("年：", a8.tm_year)
print("星期几：", a8.tm_wday)

# 9.ctime()
# 取当前的时间
print("ctime: ", time.ctime())
print(time.ctime(2889777487))  # 将时间戳格式化

# 10.mktime()
# 将结构化时间转换为时间戳
print("mktime: ", time.mktime(time.localtime()))

# 11. datetime
print(datetime.datetime.now())








