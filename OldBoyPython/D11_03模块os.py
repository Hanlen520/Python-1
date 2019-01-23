#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/22 9:46
# FileName: D11_02模块os.py
# Description:
#               r'C:\Users'的r代表的意思是原生字符串，不进行任何的转义操作
# Question:
# --------------------------------

import os


# 1. getcwd()
# 获取当前目录
print("当前目录路径为：", os.getcwd())

# 2.chdir()
# 改变当前目录
os.chdir(r'C:\Users')
print("chdir()改变目录后当前目录路径为：", os.getcwd())

# 3.curdir
# 回到当前目录
print("curdir回到当前目录: ", os.curdir)

# 4.pardir
# 获取当前目录的父目录字符串名
print("pardir获取当前目录的父目录字符串名: ", os.pardir)

# 5.makedirs()
# 创建多级目录
# os.chdir(r'D:\MySpace\Python\OldBoyPython')
print("当前目录的路径是：", os.getcwd())
# os.makedirs("Dirs\\dir1\\dir2")
# os.makedirs("Dirs\\非空文件不能删除")
print("当前目录的路径是：", os.getcwd())

# 6.removedirs()
# 删除目录(但是只能删除空文件)
# os.removedirs("Dirs\\dir1\\dir2")
print("当前目录的路径是：", os.getcwd())

# 7.mkdir()
# 生成一层目录
# os.mkdir("Dirs\\dirO")

# 8.rmdir()
# 删除一层目录
# os.rmdir("Dirs\\dirO")

# 9.listdir()
# 打印当前目录下的所有文件及文件夹
# list_dirs = os.listdir(r"D:\MySpace\Python\OldBoyPython\Dirs")
# print("list_dirs: ", list_dirs)
# print("更改目录路径：", os.chdir(r"D:\MySpace\Python\OldBoyPython\Dirs"))
# print("当前目录路径：", os.getcwd())
# print("list_dirs: ", list_dirs)

# 10.remove()
# 只能删除文件，不能删除文件夹
# os.remove(r"remove可以删除文件.txt")
# print("list_dirs: ", list_dirs)

# 11.rename()
# os.rename('改名字', '改名字后的文件夹')
# print("list_dirs: ", list_dirs)

# 12.stat()
# 获取文件操作系统层次的信息
# file_info = os.stat(r"D:\MySpace\Python\OldBoyPython\Dirs\stat文件.txt")
# print(file_info)
# print("文件大小st_size:", file_info.st_size)


# 13.sep
# 为了避免不同操作系统之间的文件路径分隔符不一致的问题
s = os.sep
print(s)

# 14.linesep
# 跨平台的换行符: WIN：\r\n； LINUX：\n
print(os.linesep)

# 15.pathsep
# 跨平台的路径分割符:
print(os.pathsep)

# 16.system
# 执行不同平台的操作命令
print(os.system("dir"))

# 17.environ
# 环境变量
print(os.environ)

# 18. path.abspath
# 打印绝对路径
print(os.path.abspath("./abc"))

# 19.path.split
# 区分路径和文件
# print(os.path.split(r"D:\MySpace\Python\OldBoyPython\Dirs\abc.txt"))

# 20.path.dirname
# 获取路径
# print(os.path.dirname(r"D:\MySpace\Python\OldBoyPython\Dirs\abc.txt"))

# 21.path.basename
# 获取文件名
print(os.path.basename(r"C:\MySpace\Python\OldBoyPython\Dirs\abc.txt"))

# 22.path.exists
# 判断路径是否存在
print(os.getcwd())
print(os.path.exists(r"C:\MySpace\Python\OldBoyPython\Dirs\abc.txt"))

# 23.path.isabs
# 如果路径是绝对路径则返回为True
print(os.path.isabs(r"C:\MySpace\Python\OldBoyPython\Dirs\abc.txt"))

# 24.path.isfile
# 如果是一个存在文件的路径则返回True，否则返回False
os.chdir(r"C:\MySpace\Python\OldBoyPython\Dirs")
print(os.path.isfile(r"C:\MySpace\Python\OldBoyPython\Dirs\stat文件.txt"))

# 25.path.isdir
# 如果目录存在则返回True，否则返回False
print(os.path.isdir(r"C:\MySpace\Python\OldBoyPython\Dirs"))


