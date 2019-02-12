#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/12 19:00
# FileName: D12_10模块json.py
# Description: 
# Question: 
# --------------------------------

dict_data = {
    'name': "json"
}

f = open('./OperatorFile/json文件', 'w', encoding="utf-8")

# f.write(dict_data)
# TypeError: write() argument must be str, not dict
# 说明字典dict_data是不可序列化的

