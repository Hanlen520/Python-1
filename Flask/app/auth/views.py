#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/15 15:54
# FileName: views.py
# Description: 
# Question: 
# --------------------------------

from flask import render_template

from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')