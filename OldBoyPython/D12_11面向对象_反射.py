#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/20 9:43
# FileName: D12_11面向对象_反射.py
# Description:
#     反射：通过字符串的形式操作(获取、设置、删除、判断是否有)对象中的成员
#          反射在导入模块中也可以使用（类、方法、字段均可以）
# Question: 
# --------------------------------

class Foo:
    static_value = "静态字段"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        return "%s - %s" % (self.name, self.age)

f1 = Foo("name_vale", 12)
print(f1.name)
print(f1.__dict__["name"])
# 去什么里面取什么值
print(getattr(f1, "name"))
func = getattr(f1, 'show_info')
print(func)
print(func())

# 给对象设置值， 给对象设置的值存放在对象的内存中
setattr(f1, "k1", "v1")
print(f1.k1)

# 判断对象中是否有某个值
print(hasattr(f1, "name"))
print(hasattr(f1, "age"))

# 删除对象中的某个
print(delattr(f1, "age"))
print(hasattr(f1, "age"))

# 获取类的静态字段的值
print(getattr(Foo, 'static_value'))


# 反射在实际情况中会用于，例如：
#   用户请求不同的链接返回不同的请求页面
class Website:
    def f1(self):
        return "首页"

    def f2(self):
        return "新闻"

    def f3(self):
        return "关注"

i = input("选择你要观看的网站：")
w = Website()

if hasattr(w, i):
    func = getattr(w, i)
    result = func()
    print(result)
else:
    print("404")




