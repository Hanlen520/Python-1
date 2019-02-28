#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/28 16:02
# FileName: 05_pymysql执行存储过程.py
# Description: 
# Question: 
# --------------------------------
import pymysql

# 连接数据库
conn = pymysql.connect(host='172.18.99.180', port=3306, user='root',
                       password='jiangheng', db='STUDY_DATABASE')
# 创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 执行存储过程
cursor.execute('pr1')
# cursor.execute('pr2', args=(1, 2, 3, 4))

# 获取执行完存储的参数
cursor.execute()
result = cursor.fetchall()

conn.commit()
cursor.close()
conn.close()

print(result)