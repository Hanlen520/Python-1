#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/7 20:49
# FileName: 04Serialization.py
# Description: 
# Question: 
# --------------------------------

import json
import requests

print('json_methods: ', json.__all__)


dict1 = {
    'name': 'A',
    'age': 25,
    'job': 'IT'
}
def dict_to_json():
    print('dict1_origin_type: ', type(dict1))
    print('dict1_origin: ', dict1)

    json1 = json.dumps(dict1)
    print('json1_type: ', type(json1))
    print('json1: ', json1)
dict_to_json()


dict2 = {
    'name': 'xk',
    'age': 25,
    'sex': 'male'
}
def json_to_dict():
    print('dict2_origin_type: ', type(dict2))
    print('dict2: ', dict2)

    # 将 dict2 序列化处理
    json2 = json.dumps(dict2)
    print('json2_type: ', type(json2))
    print('json2: ', json2)

    # 对 json2 进行反序列化处理
    dict21 = json.loads(json2)
    print('dict21_type: ', type(dict21))
    print('dict21: ', dict21)
# json_to_dict()


# 用 requests 查看返回的 json 数据
def requests_get_jsondata():
    r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=北京')
    print('r_text_type: ', type(r.text))
    print('r_text: ', r.text)

    # 对数据进行反序列化操作(json_to_dict)
    r_json = json.dumps(r.text)
    print('r_json_type: ', type(r_json))
    print('r_json: ', r_json)
# requests_get_jsondata()
