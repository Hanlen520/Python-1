#!/bin/usr/env python2
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: jiangheng
# CreateTime: 2018/12/28 10:17
# FileName: D5_01字符串格式化输出.py
# Description: 格式话输出用户信息
# Question:
# --------------------------------

name = input("Please input your name: ")
age = int(input("Please input your age: "))
job = input("Please input your job: ")
salary = input("Please input your salary: ")

if salary.isdigit():
    salary = int(salary)
else:
    exit("salary must be int.")

print(name, age, job, salary)

message = '''
----------info of %s------------
Name: %s
Age: %d
Job: %s
Salary: %f
Will work: %d years
---------------end--------------
''' % (name, name, age, job, salary, (65-age))
print(message)

