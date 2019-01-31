#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/31 18:11
# FileName: D11_09模块BASEDIR.py
# Description: 
# Question: 
# --------------------------------

import os
import sys

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path.append(BASE_DIR))