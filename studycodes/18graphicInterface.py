#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 17graphicInterface.py
# author:
# description:


# Python自带图形库Tkinter，支持多种图形界面的第三方库
#   Tk、wxWidgets、Qt、GTK


# 按钮交互
from tkinter import *


# 从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()


# 第三步，实例化Application，并启动消息循环
app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()


# 文本输入框
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()


    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题
app.master.title('Hello Word')
# 主消息循环
app.mainloop()