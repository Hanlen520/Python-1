#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 17virtualenv.py
# author:
# description:


# 如果A应用使用Python3.6，B应用使用Python2.7
# 每个应用各自拥有自己"独立的运行"环境，virtualenv就是用来为每个应用创建“隔离”Python运行环境的


# 第一步，创建目录：
# mkdir myProject
# cd myProject/


# 创建一个独立的运行环境，命名为venv：
# 命令virtualenv创建独立的Python运行环境，参数--no-site-packages第三方包都不会复制过来
# virtualenv --no-site-packages venv

