#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/3/1 21:56
# FileName: pymysql操作SQL的增删改查.py
# Description: 
# Question:
# --------------------------------------

import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='159357', db='STUDY_DATABASE')

# 创建游标
cursor = conn.cursor()

# 字符串拼接SQL，但是不要这样操作会造成SQL注入
# inp = input("请输入您要插入的数据：")
# sql = "INSERT INTO pymysql_singleData(name) values('%s')"
# sql = sql % (inp, )
# r1 = cursor.execute(sql)

# 不能使用字符串拼接的方式，必须使用参数传递的方式
inp = input("请输入您要插入的数据：")
r = cursor.execute("INSERT INTO pymysql_singleData(name) values(%s)", inp)
print(r)


conn.commit()
cursor.close()
conn.close()


