#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 12ioprogramming.py
# author:
# description:

# IO编程：同步IO（本章的内容） / 异步IO（回调模式、轮询模式）
# ----------------------------*********文件读写*********------------------------------------
# 读写文件就是请求操作系统打开一个文件对象（通常叫做文件描述符）
# 读文件
f = open('./ioFile/test.txt', 'r')
print(f.name)
print(f.buffer)
print(f.read())
f.close()
# print(f.read())


# 捕获异常操作
def read_txt():
    try:
        f = open('./ioFile/test.txt', 'r')
        print(f.read())
    finally:
        if f:
            f.close()


# 使用with
with open('./ioFile/test.txt', 'r') as f:
    print(f.read())


# 如果不确定文件的大小，可以规定每次读取数据的大小
def read_size():
    try:
        f = open('./ioFile/test.txt', 'r')
        print(f.read(1))
        print(f.read(1))
    finally:
        if f:
            f.close()


print("============read_size()==========")
read_size()


# 如果是读取配置文件
def read_lines():
    try:
        f = open('./ioFile/test.txt', 'r')
        for line in f.readlines():
            print(line.strip())
    finally:
        if f:
            f.close()


print("==============read_lines=========================")
read_lines()


# file-like Object
# 像open()函数返回的这种有个read()方法对象，统称为file-like Object
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
def read_binary():
    try:
        frb = open('./ioFile/erjinzhi.jpg', 'rb')
        print(frb.read())
    finally:
        if f:
            frb.close()


read_binary()


# 字符编码
def read_encoding():
    try:
        fre = open('./ioFile/test.txt', 'r', encoding='gbk', errors='ignore')
        print(fre.read())
    finally:
        if fre:
            fre.close()


read_encoding()


# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，
# 传入标识符'w'或者'wb'表示写文本文件或写二进制文件
def write_file():
    try:
        fw = open('./ioFile/writeToFile.txt', 'a')
        fw.write('Hello Python\t')
        fw.flush()
        fw.close()
        fr = open('./ioFile/writeToFile.txt', 'r')
        print(fr.read())
        fr.close()
    finally:
        if fr:
            fr.close()


print("==========write_file===============")
write_file()


# ---------------------*********StringIO和BytesIO**********------------------------
# StringIO
# 有时候读写不一定是在文件中读写，也可以在内存中读写，StringIO就是在内存中读写str
from io import StringIO


# 向内存中写中写入数据
def stringIO():
    try:
        fsi = StringIO()
        fsi.write('Hello')
        print(fsi.write('Hello'))
        fsi.write(' ')
        print(fsi.write(' '))
        fsi.write('StringIO')
        print(fsi.write('StringIO'))
        print(fsi.getvalue())
    finally:
        if f:
            f.close()


stringIO()


# 从内存中读取数据
from io import StringIO


def out_memory():
    try:
        fom = StringIO('Hello\n cure\n memory data')
        while True:
            s = fom.readline()
            if s == '':
                # print("read data is empty")
                break
            print(s.strip())
    finally:
        print("--------------end---------------")


out_memory()


# BytesIO
# StringIO操作的是str，要操作二进制数据，就需要使用BytesIO
# 与StringIO一样，BytesIO也可以实现在内存中读写bytes
from io import BytesIO


def writeb_memory():
    try:
        fwm = BytesIO()
        fwm.write('中文'.encode('utf-8'))
        print(fwm.write('中文'.encode('utf-8')))
        print(fwm.getvalue())
    finally:
        print("--------------end writeb_memory------------")


writeb_memory()


# BytesIO从内存中读取二进制数
from io import BytesIO


def readb_memory():
    try:
        frm = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87\xe4\xb8\xad\xe6\x96\x87')
        # frm.read()
        print(frm.read())
    finally:
        print("--------------end readb_memory------------")


readb_memory()


print("\n")
print('------------start operator and director-----------------')
# ----------------------******操作文件和目录**********-------------------------
# Python内置了os模块也可以直接调用操作系统提供的接口函数
# 获取操作系统的类型
import os


print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统


# 获取操作系统详细的信息
import os


# print(os.uname)
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


# 环境变量
import os


print(os.environ)


# 在某个目录下创建新的目录
# 先把新的目录路径描述出来
os.path.join('./ioFile/', 'mkfile')
print(os.path.join('./ioFile/', 'mkfile'))
# 然后创建这个目录
# os.mkdir('./ioFile/mkfile')
# 最后再删除这个目录
# os.rmdir('./ioFile/mkfile')


# 拆分目录----只对字符串进行操作，合并拆分的路径并不要求真实存在
ops = os.path.splitext('./ioFile/mkfile/test.txt')
print(ops)


# 对文件重命名
# os.rename('./ioFile/mkfile/test.md', './ioFile/mkfile/test.txt')


# 模块shutli模块【是对os模块的补充】提供了copyfile()的函数，
dirFilter = [x for x in os.listdir('.') if os.path.isdir(x)]
print(dirFilter)


# 列出所有符合条件的
fileFilter = [y for y in os.listdir('.') if os.path.splitext(y)[1] == '.py']
print(fileFilter)


print("\n")
print('------------start xu lie hua-----------------')
# ----------------------******序列化**********-------------------------
# 序列化
# 程序运行中，所有的变量都是在内存中的
# 把变量从内存中变成可存储或传输的过程称之为序列化(pickling)---序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
import pickle


d = dict(name='Bob', age=20, score=90)
dp = pickle.dumps(d)
print("序列化的结果为：%s" % dp)


# 把序列化的结果写入文件中
# os.path.join('./ioFile/', 'dp2File.txt')
f = open('./ioFile/dp2File.txt', 'wb')
pickle.dump(dp, f)
f.close()


# JSON
#       JSON类型              Python类型
#         {}                    dict
#         []                    list
#       "string"                 str
#       1234567                 int/float
#       true/false              True/False
#         null                  None
#
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，更好的方法就是序列化为JSON
# Python对象变成一个JSON
import json


dj = dict(name='test', age=20, score=98)
d2j = json.dumps(dj)
print("dict变为json后的结果为：%s" % d2j)


# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象
import json


class Student(object):
    def __int__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 99)
print(json.dumps(s, default=lambda obj: obj.__dict__))
#

















