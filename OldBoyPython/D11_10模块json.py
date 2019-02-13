#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/12 19:00
# FileName: D11_10模块json.py
# Description: 
# Question: 
# --------------------------------

import json

dict1_data = {
    'name': "json"
}

f = open('./OperatorFile/json文件', 'w', encoding="utf-8")

# f.write(dict1_data)
# TypeError: write() argument must be str, not dict
# 说明字典dict_data是不可序列化的


# 为了能将字典可序列化可以使用json的方法dumps方法进行字典转序列化
json_dict = {
    "name": "json_dict",
    "method": "dumps"
}

# json.dumps将字典序列化
f_dumps = open("./OperatorFile/json_dumps.txt", 'w', encoding="utf-8")
# 以下紧跟的两行代码可以用以下json.dump来简略
json_data = json.dump(json_dict, f_dumps)
# json_data = json.dumps(json_dict)
# # f_dumps.write(json_data)
# f_dumps.close()

# json.loads将json反序列化
f_loads = open("./OperatorFile/json_dumps.txt", 'r', encoding="utf-8")
# 以下紧跟的两行代码可以用以下json.load来简略
json_loads = json.load(f_loads)
# json_loads = f_loads.read()
# json_loads = json.loads(json_loads)
print(json_loads["method"])
f_loads.close()




