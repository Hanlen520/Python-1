#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/23 20:33
# FileName: D11_06模块logging.py
# Description: 
# Question: 
# --------------------------------

import logging

# 1.灵活配置日志级别
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s",
    datefmt="%a,%d %b %Y %H:%M:%S",
    filename="D:\\MySpace\\Python\\OldBoyPython\\Logging\\test.log",
    filemode='a'
)

# 2.以下是按级别从高到低排序
logging.critical("critical")
logging.error("error")
logging.warning("warning")
# 以下两个不打印
logging.info("info")
logging.debug("debug")

# 3. 参数
# %(levelno)s
# 打印日志级别的数值
#
#
# %(levelname)s
# 打印日志级别名称
#
#
# %(pathname)s
# 打印当前执行程序的路径
#
#
# %(filename)s
# 打印当前执行程序名称
#
#
# %(funcName)s
# 打印日志的当前函数
#
#
# %(lineno)d
# 打印日志的当前行号
#
#
# %(asctime)s
# 打印日志的时间
#
#
# %(thread)d
# 打印线程id
#
#
# %(threadName)s
# 打印线程名称
#
#
# %(process)d
# 打印进程ID
#
#
# %(message)s
# 打印日志信息

# *******4.既将日志信息打印进文件中也要在控制台中显示*********
# (1) 获取一个logger对象
logger = logging.getLogger()
# (2) 创建一个handle，用于写入文件日志
fh = logging.FileHandler("D:\\MySpace\\Python\\OldBoyPython\\Logging\\fh.log")
# (3) 再创建一个handle，用于打印输出到控制台
sh = logging.StreamHandler()
# (4) 创建一个格式对象formatter
formatter = logging.Formatter("%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s")

fh.setFormatter(formatter)
sh.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(sh)

logger.setLevel(logging.DEBUG)

logger.critical("critical")
logger.error("error")
logger.warning("warning")
logger.debug("debug")
logger.info("info")


