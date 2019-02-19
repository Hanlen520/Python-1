#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/18 8:19
# FileName: D12_07面向对象_成员修饰符.py
# Description:
#       公有成员
#       私有成员
# Question:
# --------------------------------------


class Person:

    __father = '大明'
    __sex = 'male'

    # 类的内部
    def __init__(self):
        self.name = '小明'
        # 私有字段，外部无法直接访问
        self.__age = 24

    # 私有字段无法外部直接访问，但是可以通过类的内部方法间接访问
    def show_age(self):
        return self.__age

    @staticmethod
    def show_sex():
        return Person.__sex

    # 类的私有字段外部不可直接访问，可以通过在类的内部使用类来访问
    @staticmethod
    def show_father():
        return Person.__father

    # 私有方法，外部無法直接访问，可以通过内部的
    def __play(self):
        print("play1.........")

    def play2(self):
        p = self.__play()
        return p


# 子类继承父类
class Son(Person):
    def __init__(self):
        self.name = 'son......1213'


# 类的外部
p1 = Person()
print(p1.name)
print(p1.show_age())
print(p1.show_sex())

# 类的私有字段外部不可直接访问，可以通过在类的内部方法来间接的访问
print(Person.show_father())

# 类的私有字段外部不可以直接访问，可以通过在类内部的静态方法来间接的访问
# 所以说只要是内部即可，和普通方法或是静态方法没有必然的关系
print(Person.show_sex())

# 私有的方法通过内部的普通方法间接滴在外部访问
p1.play2()


# 子类继承父类
s1 = Son()
print(s1.name)
# print(s1.__age)   # 虽然是继承但是子类无法直接访问父类的私有字段
# print(s1.show_age())














