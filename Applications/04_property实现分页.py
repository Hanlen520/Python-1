#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/18 7:49
# FileName: 04_property实现分页.py
# Description: 
# Question:
# --------------------------------------


class Pergination:
    def __init__(self, current_page):
        try:
            p = int(current_page)
        except Exception as e:
            p = 1
        self.page = p

    @property
    def start(self):
        val = (self.page - 1) * 10
        return val

    @property
    def end(self):
        val = self.page * 10
        return val


list = []
for i in range(1000):
    list.append(i)

# print(list)
while True:
    p = input("请输入你想要的页码：")
    obj = Pergination(p)
    # 0: 0~9
    # 1: 10~20
    # 2: 20~30
    # start = (p - 1) * 10
    # end = p * 10
    # 此处用到了list的切片功能
    print(list[obj.start: obj.end])
