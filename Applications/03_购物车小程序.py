#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: jiangheng
# CreateTime: 2019/1/3 21:02
# FileName: D6_01购物车小程序.py
# Description: 
# Question: 
# --------------------------------

# 用列表存储商品信息
shopping_mall = [
    ("小米笔记本", 8000),
    ("小米MIX3", 3500),
    ("小米手环3", 180),
    ("去探索", 20000)
]

# 定义空列表充当购物车
shopping_cart = []

balance = input("请存入您的金额：")
if balance.isdigit():
    balance = int(balance)
    print("您当前的余额为：", balance)

    while True:
        '''
            enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)
            组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        '''
        # 打印商品列表信息
        for i, j in enumerate(shopping_mall, 1):
            print("    ", i, "*****>", j, "***")

        # 选择商品信息
        choice = input("请选择商品【退出请输入：q】：")
        # 用户购买的逻辑判断
        if choice.isdigit():
            choice = int(choice)
            if 0 < choice <= len(shopping_mall):

                # 用户选择商品
                product = shopping_mall[choice-1]

                # 根据用户选择的商品与当前余额比较看是否有能力进行消费
                if product[1] <= balance:
                    # 如果满足上面的条件，则消费并得到新的余额，还需将用户购买的商品加入到购物车里去
                    balance -= product[1]
                    shopping_cart.append(product[0])
                    print("""
                            【 当前你已购买的商品有 %s 】
                          """ % shopping_cart)
                else:
                    print("抱歉您的余额不足，您当前余额为：%s" % balance)

            else:
                print("您选择的商品不存在...")
        elif choice == "q":
            print("------------END 你已经购买了以下商品 END--------")
            for i in shopping_cart:
                print(i)
            print("您还剩%s元钱" % balance)
            break
        else:
            print("你的输入不合法")
else:
    print("请检查您的输入，必须是数字哦！")

