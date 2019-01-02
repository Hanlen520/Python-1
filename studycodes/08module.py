#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 08module.py
# author:
# description:

# 导读：
# 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对比较少，
# 在Python中，一个.py文件就称之为一个模块(Module)
# 使用模块的好处
#   1. 提高了代码的可维护性。其次，编写代码不必从零开始。当一个模块编写完毕，就可以被其他地方引用。
#   2. 避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中
# 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）

# -------------------------**********使用模块*********------------------------
import sys


def test():
    # sys模块有一个argv变量，用list存储了命令行的所有参数。
    # argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    args = sys.argv
    if len(args) == 1:
        print("Hello Word!")
    elif len(args)==0:
        print("Hello, %s!" % args[1])
    else:
        print("Too many arguments!")


if __name__ == '__main__':
    test()


# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用
# 有的函数和变量我们希望仅仅在模块内部使用，在Python中，是通过_前缀来实现的
# 正常的函数和变量名是公开的(public)，可以被直接使用。
# _xxx和__xxx这样的函数或变量是非公开的(private)，不能被直接引用。
# __xxx__这样的变量是特殊变量，可以直接被直接引用，但是又特殊用途
def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 解读：在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了
#       这样，调用greeting()函数不用关心内部的private函数细节
#       这是一种非常有用的代码封装和抽象的方法
#       外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义成public


# -------------------------**********安装第三方模块*********------------------------
# pip install 需要安装的第三方库
# pip install Pillow
# MySQL驱动程序，Web框架Flask，科学计算Numpy
# 推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，
# 我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用
# 模块搜索路径： import sys
#               sys.path
#               sys.path.append('/要搜索的目录')






















