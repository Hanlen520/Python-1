#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# by author: Crisimple
# description: 类方法、实例方法、静态方法

from types import MethodType


# def set_age(self, age):
#     print('self: ', self)
#     return(self)
#     self.age = age
#     print('self.age: ', self.age)
#
#
# set_age(23, 45)   # self:  23

def set_age(self, age):
    # return(self)
    self.age = age


def set_name(self, name):
    self.name = name


class Student(object):
    pass


# ------------给类动态绑定方法------------------
# 给Student类动态绑定一个set_age的方法
Student.bbb = MethodType(set_age, Student)

# Student类创建对象s1和s2
s1 = Student()
s2 = Student()

# 给对象s1和s2动态绑定的方法bbb传入与set_age()方法一样的参数
s1.bbb(10)
s2.bbb(15)

# 打印两个对象绑定动态方法，并且执行该方法后属性的值
print(s1.age, s2.age)   # 15 15


print('---------------------2--------------------')
# # ------------只给类的某个实例对象s1的ccc绑定动态方法-------------
# 只给类的实例对象s1的方法ccc绑定动态方法
s1.ccc = MethodType(set_age, Student)

# # 给实例对象s1的ccc方法传入与set_age方法相同的参数
# s1.ccc(200)
# print(s1.age, s2.age)   # 200 200


# print('---------------------3--------------------')
# # ------------类的属性直接绑定实例方法------------------
# Student.ddd = set_age
# s1.ddd(300)
# s2.ddd(30)
# print(s1.age, s2.age)


print('---------------------4--------------------')
# ------------类的实例对象的ccc直接绑定实例方法------------------
s1.eee = set_age
s1.eee(s2, 400)
print(s1.age)
print(s2.age)


print('---------------------5--------------------')
# ------------类的实例对象的ccc直接绑定实例方法------------------
s1.hhh = MethodType(set_age, s1)
s1.hhh(500)
print(s1.age)