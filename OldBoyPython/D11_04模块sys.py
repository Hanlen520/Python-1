#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/23 11:58
# FileName: D11_04模块sys.py
# Description: 
# Question: 
# --------------------------------

# sys是在跟python解释器进行交互
import sys
import os

# 1. sys.argv
# 实现从程序外部向程序传递参数
print(sys.argv)     # 打印要执行的文件名和参数，返回一个列表


def upload():
    print("上传成功...")


def download():
    print("下载成功")

# python D11_04模块sys.py upload
# ['D11_04模块sys.py', 'upload']
# 上传成功...
# if sys.argv[1] == "upload":
#     upload()
# elif sys.argv[1] == "download":
#     download()

# 2. sys.exit([arg])
# 程序中间的退出，arg=0为正常退出


# 3. sys.version
# 查看当前python解释器的版本
print(sys.version)

# 4. sys.path
# 寻找所引用模块的路径
print(sys.path)
print(sys.path.append("D:\\MySpace\\Python\\OldBoyPython"))

# 5. sys.platform
# 查看当前运行的平台名称
print(sys.platform)

if sys.platform == "win32":
    os.system("dir")
elif sys.platform == "Unix":
    os.system("ls")
else:
    print("wrong command")

# 5. 标准打印
# stdin: sys.stdin是一个标准化输入的方法,
#        sys.stdin.readline()可以实现标准输入，其中默认输入的格式是字符串，
#        如果是int，float类型则需要强制转换。
# 与input不同的是，input可以直接在输入中输入信息print(input("请输入你的名字："))
print("请输入你的昵称：")
nickname = sys.stdin.readline()
print("Hello %s" % nickname)

# stdout：打印到控制台的标准输出
#        print 将你需要的内容打印到了控制台，然后追加了一个换行符
sys.stdout.write("标准")
print("Hello")
# 相当于下面的代码块
sys.stdout.write("Hello" + '\n')

# stderr: 一般是错误信息。stderr对象接收出错的信息
# 以上三个变量包含与标准I/O 流对应的流对象.









