#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/21 16:39
# FileName: D11_02模块random.py
# Description: 
# Question: 
# --------------------------------

import random

# 1. random()
# 不传参数，获取0~1之间的随机数
print("random: ", random.random())

# 2. randint()
# 传参数，获取参数之间的随机数，左右两边均包含
print("randint: ", random.randint(1, 9))

# 3. choice()
# 传参数，随机获取字符串(序列)中的字符
print("choice: ", random.choice("HELLO"))
print("choice: ", random.choice(["12", 2, [1, 3], [3, 4]]))

# 4.shuffle()
#
# print(help(random.shuffle))
# print(random.shuffle())

# 5. sample()
# 根据传进的参数，在给定的序列中随机选择参数个的序列
print("shuffle: ", random.sample((["12", 2, [1, 3], [3, 4]]), 3))

# 6. 生成验证码
def random_code():
    code = ''
    for i in range(4):
        add = random.choice([random.randrange(10), chr(random.randrange(65, 91))])
        # if i == random.randint(0, 3):
        #     add = random.randrange(10)
        # else:
        #     add = chr(random.randrange(65, 91))

        code += str(add)
    print(code)

random_code()