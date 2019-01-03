#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2018/12/28 20:50
# FileName: D5_03for循环中使用break或continue.py
# Description: continue结束本次循环，继续下一次循环
# Question: 
# --------------------------------

# 在for循环中使用break模拟用户登录

# 模拟数据库中的用户名和密码
# __user = "crisimple"
# __passwd = "test123"
#
# # 标记位法控制某些语句的输出
# passed_authentication = False
#
# counter = 0
# while counter < 3:
# # for counter in range(3):
#     username = input("Please input your username: ")
#     password = input("Please input your password: ")
#     if username == __user and password == __passwd:
#         print("Welcome %s login..." % __user)
#         passed_authentication = True
#         break   # 程序中断，跳出本次整个当前循环
#     else:
#         print("Invalid username or password.")
#     counter += 1
#
#     if counter == 3:
#         keep_going_choice = input("Do you want to continue?[y|n]")
#         if keep_going_choice == "y":
#             counter = 0
# # for...else
# else:
#     print("打死你个龟孙，不要妄图破解我的用户名和密码...")

# 用标志位的方式判断
# if not passed_authentication:
#     print("打死你个龟孙，不要妄图破解我的用户名和密码...")


# continue
exit_flag = False
for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("layer2: ", j)
        if j == 6:
            exit_flag = True
            break
    if exit_flag:
        break