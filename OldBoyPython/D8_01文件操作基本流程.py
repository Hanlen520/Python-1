#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/10 20:18
# FileName: D8_01文件操作基本流程.py
# Description: 
# Question: 
# --------------------------------

# r创建文件读操作对象
# fr = open("./OperatorFile/小诗小吟.txt", 'r', encoding="utf-8")
# 读取数据操作
# data = fr.read()
# print(data)
# print("fr: ", fr.fileno())
# 关闭文件操作
# fr.close()


# w创建文件写操作对象
# 如果文件存在则会清空文件，重新开始写的操作
# 如果文件不存在则会创建文件，开始写的操作
# 但是这种写操作会连在一块
# fw = open("./OperatorFile/没有文件创建文件.txt", 'w', encoding="utf-8")
# fw.write("我们是祖国的花朵")
# fw.write("你一定会爱上我")
# print("fw: ", fw.fileno())
# 关闭文件操作
# fw.close()


# a创建append文件操作对象
# import time
# fa = open("./OperatorFile/append文件.txt", 'a', encoding="utf-8")
# fa.write("\n Hello Python \n")
# fa.write("Hello Shell \n")
# fa.write("Hello JavaScript\n")
# print("fa: ", fa.fileno())
# time.sleep(10)
# fa.close()


# readline按行读取
# readline只能一行一行的读取文件数据
# readlines读取文件中的全部行，但是readlines存在一个缺陷，文件太大的时候一读取会全部读到内存里面去
fra = open("./OperatorFile/小诗小吟.txt", 'r', encoding="utf-8")
# print(fra.readline())
# print(fra.readline())
# counter = 0
# for line in fra.readlines():
#     counter += 1
    # ========方法一===========
    # if counter == 4:
    #     print(line.strip(), "---看淡皆浮云")
    # else:
    #     print(line.strip())
    # =====方法二：对上面进行改造=========
    # if counter == 4:
    #    line = ''.join([line.strip(), "---上帝视角看皆为浮云"])
    #    line = line.strip() + "---上帝视角看皆为浮云"
    # print(line.strip())

# 方法三: 因为readlines读取文件后，会把每一行数据存在一个列表中
# print(fra.readlines())
# for k in fra.readlines():
#     print(k)
    # if k[3] == 3:
    #     fra.readlines()[k] = ''.join([fra.readlines()[3], '---来自降维视角的蔑视'])

    # print(fra.readlines())
# if fra.readlines(). == 3:
#     fra.readlines()[3] = ''.join([fra.readlines()[3], '---来自降维视角的蔑视'])

# 方法四：迭代器
# for循环使用fra对象内的迭代器，用一行生成一行
number = 0
for i in fra:
    number += 1
    if number == 6:
        i = ''.join([i.strip(), "---来自降维视角的蔑视"])
    print(i.strip())
fra.close()







