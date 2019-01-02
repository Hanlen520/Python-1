#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: Python起步.py
# author: jiangheng
# description:
# questions:


# ------------------2.1 程序输出，print 语句及“Hello World!”
# **************************print支持重定向*******************************
logfile = open('./TestFile/myLog.txt', 'a+')
myString = 'Fatal error, invalid input!'

# print >> sys.stderr, "Fatal error, invalid input!"
# 将错误信息'Fatal error, invalid input!'重定向到文件logfile.txt中去
# 试了print >> logfile, myString，报错：
# .....................TypeError: unsupported operand type(s) for >>: 'builtin_function_or_method' and '_io.TextIOWrapper'. Did you mean "print(<message>, file=<output_stream>)"?
print(myString, file=logfile)
# 关闭文件操作
logfile.close()


# -----------------2.2 程序输入和 raw_input()内建函数
# *****************简单的登录交互小程序*****************
def foo():
    user = input("Enter your name: ")
    age = int(input("Enter your age: "))
    sex = input("Enter your sex: ")

    print("Hello, %s, I am %d age old, I am %s" % (user, age, sex))


# ----------------2.3 注释
# ******************生成运行时访问的注释，也可以用来自动生成文档
def foo():
    "This is a doc String"
    return True


# ----------------2.6 数据类型
# ******************int、long、boolean、complex、float、decimal
import decimal

number = 1.1
print(number)
print(decimal.Decimal(number))


# ----------------2.7 字符串
myStrings = "I am a good boy. "
anotherString = 'I am so nervous!!!'
print("索引运算符[]得到子字符串：", myStrings[2])
print("索引运算符[]得到子字符串：", myStrings[-1])
print("切片运算符[:]得到子字符串：", myStrings[2: 6])
print("加号+用于字符串连接运算：", myStrings + anotherString)
print("*号用于字符串重复：", myStrings * 2)


# ----------------2.8 列表和数组
myList = ['A', '1', 'B', 'C', "myString", '...']
print("切片运算符[:]得到子字符串：", myList[0: 2])
print("切片运算符[:]得到子字符串：", myList[2:])
print("切片运算符[:]得到子字符串：", myList[:3])
myList[1] = 'D'
print("切片运算符[:]得到子字符串：", myList[1])
print("切片运算符[:]得到子字符串：", myList)

myTuple = ('Aa', 'Bb', "Cc", "Ee")
print("打印Tuple：", myTuple)
print("元组不能修改，但是还可以切：", myTuple[1:2])


# ----------------2.9 字典
myDict = {'host': 'earth'}
print("基础字典：", myDict)
myDict['port'] = 80
print("增加键值对后的结果：", myDict)
for key in myDict:
    print(key + ":", myDict[key])


# ----------------2.12 while循环
counter = 0
while counter < 3:
    print("------loop %d" % counter)
    counter += 1


# --------------2.13 for 循环和 range()内建函数
for item in ['A', 'B', 'C', 'D', 'E', 'F']:
    print(item, end=', ')

print()

myDict2 = ['A', 'B', 'C', 'D', 'E', 'F']
print(len(myDict2))
for i in range(len(myDict2)):
    if i != len(myDict2) - 1:
      print(i, myDict2[i], end=', ')
    else:
      print(i, myDict2[i], end='')

print()

for eachNum in range(4):
    print(eachNum + 1, end=' ')


print()


foo = 'abc'
for i, ch in enumerate(foo):
    print(ch, '(%d)' % i)


# --------------2.14 列表解析
squared = [x ** 2 for x in range(4)]
print("平方后的结果为：", squared)

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
print("平方后not不能被2整除的，即偶数：", sqdEvens)
print()

# --------------2.15 文件和内建函数 open() 、file()
filename = './TestFile/myLog.txt'


def openfile(filename1):
    handle = open(filename1, 'r')
    for eachLine in handle:
        print(eachLine, end=' ')
    handle.close()


openfile(filename)


# --------------2.16 错误和异常


def openfile_senior(filename1):
    try:
        handle = open(filename1, 'r')
        for eachLine in handle:
            print(eachLine + "senior", end=' ')
        handle.close()
    except IOError as ie:
        print("打开文件报错了，请注意查看", ie)


filename_path = './TestFile/myLog.txt'
openfile_senior(filename_path)


# -----------------2.17 函数
def addMe2Me(x):
    print("addMe2Me的执行结果为：", x + x)


myList1 = ['a', '-1', '0', 'B']
addMe2Me(myList1)


# 默认参数，如果填写就按填写参数去做条件判断，如果不填写就执行默认参数的条件的判断
def test_foo(debug=True):
    if debug:
        print("in debug model...")
        print("done...")
    else:
        print("end...")


test_foo(False)


# --------------------------------------------------------
print("-----------------2.18 类")
# -----------------2.18 类


class FooClass(object):
    version = 0.1


    def __init__(self, nm = 'jiangheng'):
        '''constructor'''
        self.name = nm
        print("Created a class instance for", nm)


    def show_name(self):
        print("Your name is: ", self.name)
        print("My name is: ", self.__class__.name)


    def show_showver(self):
        '''display class(static) attribute'''
        print(self.version)


    # @staticmethod
    def addMe2Me(self, x):
        return x + x


foo01 = FooClass()
print(foo01)
print(foo01.show_showver)
print(foo01.addMe2Me(0.5))


# --------------------------------------------------------
print("-----------------2.19 模块")
# -----------------2.19 模块
import sys

# 不同于 print 语句， write(), 不会自动在字符串后面添加换行符号。
sys.stdout.write("Hello module \n")
print(sys.platform)
print(sys.version, '\n')


# --------------------------------------------------------
print("-----------------2.20 实用的函数")
# -----------------2.20 实用的函数
# 对Python初学者又用的内建函数
# dir([obj])--------------显示对象的属性，如果没有提供参数，则显示全局变量的名字
# help([obj])-------------以整齐美观的方式显示对象的文档字符串，如果没有提供任何参数则会进入交互式帮助
# int([obj])--------------将一个对象转换为整数
# len([obj])--------------返回对象的长度
# open(fn, mode)----------以mode(r/w)方式打开一个文件名为fn的文件
# range([[start, ]stop[, step]])----返回一个整数列表。起始值为 start, 结束值为 stop - 1; start 默认值为 0， step默认值为1。
# raw_input(str)----------等待用户输入一个字符串， 可以提供一个可选的参数 str 用作提示信息。
# str(obj)----------------将一个对象转换为字符串
# type(obj)---------------返回对象的类型（返回值本身是一个type对象）



