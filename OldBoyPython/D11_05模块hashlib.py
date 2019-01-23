#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/23 14:49
# FileName: D11_05模块hashlib.py
# Description: 其实就是计算加密的模块
# Question: 
# --------------------------------

import hashlib

# 1. md5() 算法
m = hashlib.md5()
print(m)    # 返回的是一个md5 HASH对象: <md5 HASH object @ 0x000002A35FECD0A8>
# 进行字符串1的加密
m.update("Hello World".encode("utf-8"))
# 对加密后的数据1进行查看，返回摘要，作为十六进制数据字符串值
# hash.digest() 返回摘要，作为二进制数据字符串值
print(m.hexdigest())  # b10a8db164e0754105b7a99be72e3fe5


# 对字符串2进行加密
m.update("小测试".encode("utf-8"))
# 对加密后的数据2进行查看
print(m.hexdigest())    # 65d874c1db56095c60312ce2c4ecf249

# ** 如何判断字符串1和字符串2在update加密的时候有关系？
# 通过以下的方法进行加密后的值进行比较判断，发现对字符串2进行加密是在字符串1加密的基础上进行的
m2 = hashlib.md5()
m2.update("Hello World小测试".encode("utf-8"))
print(m2.hexdigest())  # 65d874c1db56095c60312ce2c4ecf249


# 2. hash ----更高级的算法
#       常用的加密用sha256
h1 = hashlib.sha256()
h1.update("Hello World".encode("utf-8"))
print(h1.hexdigest())
# hashlib加密是一种不可逆的过程

