#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/15 10:52
# FileName: forms.py
# Description: 
# Question: 
# --------------------------------

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField("请少侠报上你的大名：", validators=[DataRequired()])
    submit = SubmitField('提交')
