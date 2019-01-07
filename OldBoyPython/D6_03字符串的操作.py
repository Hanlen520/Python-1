#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/5 17:32
# FileName: D6_03字符串的操作.py
# Description: 
# Question:
# --------------------------------------

# 创建字符串
string1 = '我是字符串1'
string2 = "我是字符串2"
print(string1)
print(string2)

# 1.重复打印字符串
string3 = "Hello "
print(string3 * 3)

# 2.字符串切片
string4 = "Hello Python!"
print(string4[6:])

# 3.判断字符串是不是在某一个字符串内
string5 = "llo"
print(string5 in string4)

# 4.格式化输出
string6 = "小精灵"
print("我是一只小精灵、%s" % string6)

# 5.字符串拼接
string7 = "abc"
string8 = "123"
string9 = "ABC"
print(string7 + string8)
string10 = "******".join([string7, string8, string9])
print(string10)

# 6.字符串的内置方法
string11 = "th\tis is a string222."
print("统计元素个数：", string11.count("i"))
print("字符串开头首字母大写：", string11.capitalize())
print("字符串剧中：", string11.center(50, '*'))
print("字符串剧中：", string11.encode())
print("以什么结束：", string11.endswith("ing."))
print("以什么开始：", string11.startswith("th"))
print("通过\t来确定字符串之间的分隔：", string11.expandtabs(tabsize=20))
print("通过find查找到第一个元素并将索引值返回：", string11.find('r'))
string12 = "{name} is {age}"
print("format格式化输出：", string12.format(name="crisimple", age=24))
print("format_map格式化输出：", string12.format_map({"name": 'crisimple', "age": 24}))
print("通过index查找索引：", string11.index('a'))
print("isalnum是字母或数字的判断：", 'abc123'.isalnum())
print("十进制的数的判断：", '121'.isdecimal())
print("isdigit判断是不是数字：", '2333'.isdigit())
print("isnumeric判断是不是数字：", "22332s".isnumeric())
print("isidentifier非法变量判断：", '121www'.isidentifier())
print("全是小写判断islower：", 'Abc'.islower())
print("全是小写判断isupper：", 'ABC'.isupper())
print("空格的判断：", ' '.isspace())
print("标题的判断：", "My Title Is Nice".istitle())
print("大写变小写：", "My Title Is Nice".lower())
print("小写变大写：", "My Title Is Nice".upper())
print("小写变大写，大写变小写：", "My Title Is Nice".swapcase())
print("向左添加*：", "My Title".ljust(50, "*"))
print("向右添加*：", "My Title".rjust(50, "&"))
print("去掉字符串左右的空格:", " My Title ".strip())
print("替换：", "My title title".replace("title", "love", 1))
print("字符串分割", "My title title".split(" "))
print("字符串分割从右边开始", "My title title".rsplit(" ", 1))
print("变成title格式：", "My title title".title())

