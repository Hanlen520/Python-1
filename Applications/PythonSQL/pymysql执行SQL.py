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

# 创建游标(相当于是打开了数据库的门)
cursor = conn.cursor()

# 执行数据插入(门打开了，再进行各种数据库的操作)
effect_row = cursor.execute("UPDATE sex SET sex_id = 3 WHERE sex_name='未知'")

# 将上面执行的数据提交到数据库里(不然无法保存新建或者修改的数据)
conn.commit()

# 关闭游标
cursor.close()

# 关闭数据库连接
conn.close()