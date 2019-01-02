#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 22connectDatabase.py
# author:
# description:
#   1. mysql.connector.errors.ProgrammingError: 1698 (28000): Access denied for user 'root'@'localhost'
#       解决方案：停止mysql服务----------- sudo service mysql stop
#                以安全模式启动MySQL------ sudo mysqld_safe --skip-grant-tables &
#   2. mysql.connector.errors.OperationalError: MySQL Connection not available.
#       解决方案：如果你打开了一个cursor，但是没有把里面的结果集都read一遍就把它close掉了，以后就悲剧了
#                注释掉提交事务后面的conn.close()

# 程序运行的时候，数据都是在内存中的。
# 当程序终止的时候，通常都需要将数据保存到磁盘上，无论是保存到本地磁盘，还是通过网络保存到服务器上，最终都会将数据写入磁盘文件。
# MySQL是Web世界中使用最广泛的数据库服务器。
# SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用
# MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
import mysql.connector

# 创建连接对象并创建游标
conn = mysql.connector.connect(user='root', password='YES', database='test')
cursor = conn.cursor()

# 创建user表
# cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')

# 插入一行记录，注意MySQL的占位符是%s
# cursor.execute('INSERT INTO user(id, name) VALUES(%s, %s)', ['4', 'jiangheng4'])
print(cursor.rowcount)

# 提交事务
conn.commit()
# conn.close()

# 运行查询
cursor = conn.cursor()
cursor.execute('SELECT * FROM user WHERE id = %s', ('1', ))
values = cursor.fetchall()
print(values)
conn.close()


