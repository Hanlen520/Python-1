#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/13 14:42
# FileName: D11_12模块shelve.py
# Description:
#           shelve模块和pickle模块类似，但是比pickle模块使用简单
# Question: 
# --------------------------------
import shelve


f = shelve.open('./OperatorFile/shelve_file.txt')
# 直接可以通过句柄f写入到文件
# f['info'] = {
#     'name': 'shelve',
#     'method': '可以直接将字典写入'
# }

# 直接可以通过句柄读取数据
data = f.get('info')
data1 = f.get('info').get('name')
data2 = f.get('info').get('method')
print(data)