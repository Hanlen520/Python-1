#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/14 18:50
# FileName: __init__.py
# Description: 
# Question: 
# --------------------------------

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors