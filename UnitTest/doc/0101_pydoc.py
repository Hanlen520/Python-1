#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   0101_pydoc.py
@Time    :   2019/8/16 11:36
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

NMAE = 'PyDOC'


class CreatePyDOC(object):
    name = 'pydoc'
    """
    定义一个CreatePyDOC，该类包括两个变量：name、language
    """
    def __int__(self, name, language):
        """
        name --- 初始化文档的名称
        language --- 初始化文档的编写语言
        :param name:
        :param language:
        :return:
        """
        self.name = name
        self.age = language

    def print_info(self, language):
        """
        定义一个print_info方法
        language代表使用的语言
        :param language:
        :return:
        """
        print("%s doc 是用 %s 编写的" % (self.name, language))


def create_doc(name, language, money):
    """
    定义一个打印创建doc信息的函数
    name --- 档的称
    language --- 文档语言
    money --- 售价
    :param name:
    :param language:
    :param money:
    :return:
    """
    print("doc的名字是 %s, 它的语言是 %s, 售价 %d"% (name, language, money))