#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/15 15:50
# FileName: __init__.py
# Description: 
# Question: 
# --------------------------------

from flask import Blueprint

# 用户认证系统的路由在 auth 蓝本中定义
auth = Blueprint('auth', __name__)

from . import views
