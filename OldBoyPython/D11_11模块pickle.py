#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/13 8:15
# FileName: D11_11模块pickle.py
# Description:
#       json可序列化的对象是字典之类的数据类型
#       如果要将函数序列化，则需使用pickle来将函数对象序列化
# Question:
# --------------------------------------
import pickle


def foo():
    print("OK")

# pickle.dumps将函数对象序列化
# pickleDumps_data = pickle.dumps(foo())
# f_pickleDumps = open('./OperatorFile/pickle_file.txt', 'wb')
# f_pickleDumps.write(pickleDumps_data)
# f_pickleDumps.close()


# pickle.loads将文件中的函数对象反序列化加载
f_pickleLoads = open('./OperatorFile/pickle_file.txt', 'rb')
pickleLoads_data = f_pickleLoads.read()
pickleLoads_data = pickle.loads(pickleLoads_data)
print(pickleLoads_data)
