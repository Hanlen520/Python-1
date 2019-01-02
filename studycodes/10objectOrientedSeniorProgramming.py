#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 09objectOrientedProgramming
# author:
# description:

# -------------------------************导读************------------------------
# 面向对象的3个基础概念：数据封装、继承、多态
# 多重继承、定制类、元类


# -------------------------************使用__slots__************------------------------
class Student(object):
    pass


s = Student()
s.name = 'test name'    # 动态给实例绑定属性
print(s.name)


def set_age(self, age):     # 给实例绑定一个方法
    self.age = age


from types import MethodType
s.set_age = MethodType(set_age, s)      # 给实例绑定一个方法
s.set_age(25)   # 调用实例方法
print(s.age)

# 给一个实例绑定的方法，对另一个实例是不起作用的
s2 = Student()
# print(s2.set_age(25))


# 给class绑定方法后，所有实例均可调用
def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)


# 如要限制实例的属性，Python允许在定义class时，定义一个特殊的变量__slots__，来限制class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')


# s = Student()
# s.weight = '123'
# print(s.weight)
# 由于'weight'没有被放到__slots__中，所以不能绑定weight属性，试图绑定weight将得到AttributeError的错误。
# 特别注意：__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
    pass


g = GraduateStudent()
s.score = '98'
print(s.score)


# -------------------------************使用@property************------------------------
# g = GraduateStudent()
# s.score = '98'
# print(s.score)
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改
# 为了限制score的范围，可以通过一个set_score()来设置成绩，用get_score()来获取成绩
# class Student(object):
#     @property
#     def get_score(self):
#         return self.score
#
#     @score.setter
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be integer')
#         if value < 0 or value > 100:
#             raise ValueError('score must be in 0 ~ 100')
#
#         self._score = value
#
#
# s = Student()
# s.score = 80
# print(s.score)


# -------------------------************多重继承************------------------------
# 通过继承，子类就可以扩展父类的功能
class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


# 要给Dog加上Runnable的功能，给Bat加上Flyable的功能
class Runnable(object):
    def run(self):
        print("Running...")


class Flyable(object):
    def fly(self):
        print("Flying...")


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能
# Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，
# 这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来
# TCPServer
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
#
#
# # UPServer
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
#
#
# # 协程模型
# class MyTCPServer(TCPServer, CoroutineMinIn):
#     pass


# -------------------------************定制类************------------------------
# __str__
# __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
# class Book(object):
#     def __int__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return "Book object (name: %s)" % self.name
#
#     # 偷懒
#     __repr__ = __str__
#
#
# print(Book('Bob'))


# __iter__
# 类用for...in...循环，必须使用__iter__方法，返回一个迭代对象
class Fib(object):
    def __int__(self, a, b):
        self.a, self.b = 0, 1   # 初始化两个值

    def __iter__(self):
        return self     # 实例本身就是迭代对象，故返回自己

    def __next__(self, a, b):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10000:
            raise StopIteration
        return self.a


# for n in Fib():
#     print(n)

# __getitem__


# -------------------------************使用枚举类************------------------------
# 定义常量时，一个办法是用大写变量通过整数来定义
# 枚举类Enum定义一个class类型，每个常量都是class的一个唯一实例
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '==>', member, ',', member.value)


# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique


@unique     # @unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)


# -------------------------************使用元类************------------------------
# type()
# 动态语言的函数和类的定义是在运行时动态创建的
class Hello(object):
    def sayHi(self, name='Python'):
        print("Hello, %s" % name)


h = Hello()
print(type(Hello))
print(type(h))


# type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name="python"):
    print("hi, %s" % name)


# 创建Hello class
Hi = type("Hi", (object,), dict(hi=fn))

# 要创建一个class对象，type()函数依次传入3个参数：
#   1. class的名称；
#   2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#   3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello


# metaclass
# 除了使用type()动态创建类，还可以使用metaclass（元类）来控制类的创建行为
# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例（你可以把类看成是metaclass创建出来的“实例”）
class ListMetaclass(type):    # metaclass是类的模板，所以必须从`type`类型派生：
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass

# __new__()方法接收到的参数依次是：
#   当前准备创建的类的对象；
#   类的名字；
#   类继承的父类集合；
#   类的方法集合。
