#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/1/18 16:46
# FileName: Turtle_drawPig.py
# Description: 最近小猪佩奇很火，我也来跟一波耍一下
# Question: 
# --------------------------------

import turtle as t
import time

# 设置画笔的大小
t.pensize(5)

# 设置GBK颜色范围为0-255
t.colormode(255)

# 设置画笔颜色和填充颜色(pink)
t.color((255, 155, 192), "pink")

# 设置主窗口的大小为840*500
t.setup(840, 500)

# 设置画笔速度为10
t.speed(20)


# 鼻子
def nose():
    # 提笔
    t.pu()
    # 定位坐标，画笔前往坐标(-100,100)
    t.goto(-100, 100)
    # 下笔
    t.pd()
    # 笔的角度为-30°
    t.seth(-30)
    # 外形填充的开始标志
    t.begin_fill()

    a = 0.4
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            t.lt(3)
            # 向前走a的步长
            t.fd(a)
        else:
            a = a - 0.08
            t.lt(3)
            t.fd(a)

    # 依据轮廓填充, 到此鼻子画完并填充了
    t.end_fill()

    # 提笔
    t.pu()
    # 笔的角度为90度
    t.seth(90)
    # 向前移动25
    t.fd(25)
    # 转换画笔的角度为0
    t.seth(0)
    t.fd(10)
    t.pd()
    # 设置画笔颜色
    t.pencolor(255, 155, 192)
    t.seth(10)
    t.begin_fill()
    # 画一个半径为5的圆
    t.circle(5)
    # 设置画笔和填充颜色
    t.color(160, 82, 45)
    t.end_fill()

    # 提笔
    t.pu()
    t.seth(0)
    t.fd(20)
    t.pd()
    t.pencolor(255, 155, 192)
    t.seth(10)
    t.begin_fill()
    t.circle(5)
    t.color(160, 82, 45)
    t.end_fill()


# 头
def header():
    t.color((255, 155, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(41)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.begin_fill()
    t.seth(180)
    # 顺时针画一个半径为300,圆心角为30°的园
    t.circle(300, -30)
    t.circle(100, -60)
    t.circle(80, -100)
    t.circle(150, -20)
    t.circle(60, -95)
    t.seth(161)
    t.circle(-300, 15)
    t.pu()
    t.goto(-100, 100)
    t.pd()
    t.seth(-30)
    a = 0.4
    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a+0.08
            # 向左转3度
            t.lt(3)
            # 向前走a的步长
            t.fd(a)
        else:
            a = a-0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()


# 耳朵
def are():
    t.color((255, 155, 192), "pink")
    t.pu()
    t.seth(90)
    t.fd(-7)
    t.seth(0)
    t.fd(70)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 54)
    t.end_fill()
    t.pu()
    t.seth(90)
    t.fd(-12)
    t.seth(0)
    t.fd(30)
    t.pd()
    t.begin_fill()
    t.seth(100)
    t.circle(-50, 50)
    t.circle(-10, 120)
    t.circle(-50, 56)
    t.end_fill()


# 眼睛
def eye():
    t.color((255,155,192),"white")
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-95)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.color((255, 155, 192), "white")
    t.pu()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.pd()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.pu()
    t.seth(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pd()
    t.begin_fill()
    t.circle(3)
    t.end_fill()


# 佩奇的腮
def sai():
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(-95)
    t.seth(0)
    t.fd(65)
    t.pd()
    t.begin_fill()
    t.circle(30)
    t.end_fill()


# 佩奇的嘴
def mouse():
    t.color(239, 69, 19)
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(-100)
    t.pd()
    t.seth(-80)
    t.circle(30, 40)
    t.circle(40, 80)


# 佩奇的身体
def body():
    t.color("red", (255, 99, 71))
    t.pu()
    t.seth(90)
    t.fd(-20)
    t.seth(0)
    t.fd(-78)
    t.pd()
    t.begin_fill()
    t.seth(-130)
    t.circle(100, 10)
    t.circle(300, 30)
    t.seth(0)
    t.fd(230)
    t.seth(90)
    t.circle(300, 30)
    t.circle(100, 3)
    t.color((255, 155, 192), (255, 100, 100))
    t.seth(-135)
    t.circle(-80, 63)
    t.circle(-150, 24)
    t.end_fill()


# 佩奇的手
def hand():
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(-40)
    t.seth(0)
    t.fd(-27)
    t.pd()
    t.seth(-160)
    t.circle(300, 15)
    t.pu()
    t.seth(90)
    t.fd(15)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.seth(-10)
    t.circle(-20, 90)
    t.pu()
    t.seth(90)
    t.fd(30)
    t.seth(0)
    t.fd(237)
    t.pd()
    t.seth(-20)
    t.circle(-300, 15)
    t.pu()
    t.seth(90)
    t.fd(20)
    t.seth(0)
    t.fd(0)
    t.pd()
    t.seth(-170)
    t.circle(20, 90)


# 佩奇的脚
def foot():
    t.pensize(10)
    t.color((240, 128, 128))
    t.pu()
    t.seth(90)
    t.fd(-75)
    t.seth(0)
    t.fd(-180)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)
    t.pensize(10)
    t.color((240, 128, 128))
    t.pu()
    t.seth(90)
    t.fd(40)
    t.seth(0)
    t.fd(90)
    t.pd()
    t.seth(-90)
    t.fd(40)
    t.seth(-180)
    t.color("black")
    t.pensize(15)
    t.fd(20)


# 佩奇的尾巴
def tail():
    t.pensize(4)
    t.color((255, 155, 192))
    t.pu()
    t.seth(90)
    t.fd(70)
    t.seth(0)
    t.fd(95)
    t.pd()
    t.seth(0)
    t.circle(70, 20)
    t.circle(10, 330)
    t.circle(70, 30)


def main():
    nose()
    header()
    are()
    eye()
    sai()
    mouse()
    body()
    hand()
    foot()
    tail()
    time.sleep(3)


if __name__ == "__main__":
    main()
