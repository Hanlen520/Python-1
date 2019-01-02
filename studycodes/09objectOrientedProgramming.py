#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 09objectOrientedProgramming
# author:
# description:

# ---------------------****************导读********************-----------------------------
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数
# 为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度
# 在Python中，所有数据类型都可以视为对象，自定的对象数据类型就是面向对象中的类(class)的概念
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 99}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


print_score(std1)


# -------->
class Student(object):
     # 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
     # __init__方法的第一个参数永远是self，表示创建的实例本身，
     # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
     # 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
     # 但self不需要传，Python解释器自己会把实例变量传进去：
     def __init__(self, name, score):
         self.name = name
         self.score = score


     # 数据封装
     def print_score(self):
         print('%s: %s' % (self.name, self.score))

     def get_grade(self):
         if self.score >= 90:
             return 'A'
         elif self.score >= 60:
             return 'B'
         else:
             return 'C'


bart = Student('bart', 99)
lisa = Student('lisa', 98)
bart.print_score()
lisa.print_score()
print(lisa.get_grade())
# 面向对象的设计思想是抽象出Class，根据Class创建Instance。


# ---------------------****************访问限制********************-----------------------------
# 如果要让内部属性不被外部访问，可以把属性名称前加上两个下划线__
# 实力的变量名如果以__开头，就变成了私有变量(private)，只有内部可以访问，外部不能凡哥维纳
class Studen(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= self.score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score.')

# 在Python中，变量名类似__xxx__的，是特殊变量，是可以直接访问的，不是private变量，所以不能用__name__、score__这样的变量名


#
# bart = Student('Bart', 98)
# print(bart.__name)


# ---------------------********************继承和多态********************-----------------------------
# OPP设计中，当我们定义一个class时，可以从某个现有的class继承，新的class称为子类(Subclass)，而被继承的class称为基类、父类或超类
class Animal(object):
    def run(self):
        print("Animal is run...")


# 编写Dog类和Cat类，可以直接从Animal类继承：
class Dog(Animal):
    pass


class Cat(Animal):
    pass


# 继承的好处：
#   最大的好处就是获得了父类的全部功能
dog = Dog()
dog.run()

cat = Cat()
cat.run()


# 对子类增加一些方法
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat....')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


dog = Dog()
dog.run()
# 即子类和父类存在相同的方法时，子类的方法会覆盖父类的方法，这样就获得了继承的另一个好处：多态
# 前提：判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))


# 理解多态
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Duck(Animal):
    def run(self):
        print('Duck is running laughter.....')


run_twice(Duck())
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
# 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，
# 就会自动调用实际类型的run()方法，这就是多态的意
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


# 静态语言 vs 动态语言
# 静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法
# Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了


# ---------------------********************继承和多态********************-----------------------------
# 获取对象信息
# type()
print(type(1213))
print(type('123'))
print(type(None))
print(type(abs))
print(type(dog))


# isinstance()
# 对于class的继承关系来说,使用type()很不方便, 我们要判断class的类型, 可以使用isinstance()函数
class Husky(Dog):
    def run(self):
        print('Husky is running...')


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Dog))
print(isinstance(d, Dog) and isinstance(d, Animal))


# dir()
# 如果要获得一个对象的所有属性和方法,可以使用dir()函数
# 它返回一个包含字符串的list
print(dir('ARC'))


# ---------------------********************实例属性和类属性********************-----------------------------
# 由于Python是动态语言, 根据类创建的实例可以任意绑定属性
class Tree(object):

    name = 'LittleTree'

    # def __int__(self, name):
    #     self.name = name


print(Tree.name)
t = Tree()
print(t.name)
































