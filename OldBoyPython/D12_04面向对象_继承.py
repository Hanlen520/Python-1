#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/17 15:51
# FileName: D12_04面向对象_继承.py
# Description: 
# Question:
# --------------------------------------


class Father:

    def football(self):
        print("play football")

    def eat_food(self):
        print("father eat rice")

    def bad_habit(self):
        print("father's bad habit")


class Monter:
    def eat_food(self):
        print("mother eat rice")

    def watch_movie(self):
        print("mother watch movie")


class Son(Father):
    def play_games(self):
        print("son can play games")

    # 但是子类不一定全部继承父类的方法，可以通过重写避免继承父类的所有方法
    def bad_habit(self):
        super(Son, self).bad_habit()
        print("son's abd habit")


class Daughter(Monter, Father):
    def buy_cloth(self):
        print("daughter buy cloth")


s1 = Son()
# 1.因为继承了父类（基类），子类（派生类）可以使用父类的方法
s1.eat_food()

# 2.但是子类不一定全部继承父类的方法，可以通过重写避免继承父类的所有方法
# 下面调用的是子类的方法，父类的方法被子类的方法重新后，子类的实例对象就不会调用父类对象的方法了
s1.bad_habit()

# 3.如果想在重写父类方法时，调用子类方法时也调用父类的方法
# super(Son, self).bad_habit()  在子类重写的方法中加上super(子类, self).父类的方法

# 4.多重继承
# 上面的Daughter类继承了两个基类Father、Mother
d1 = Daughter()
# 如果继承两个类，子类调用父类时会先找左边的类的方法，有了的话就不再调用右边类的方法了，如果没有再去找右边类的
d1.eat_food()   # mother eat rice;






