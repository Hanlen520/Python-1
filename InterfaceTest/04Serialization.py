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

def json_to_dict():
    pass