#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 24asynchronization.py
# author:
# description: 异步IO


# 多线程解决了应用为多个用户同时服务，一个用户的线程被挂起，其他用户的线程不被影响
# 但是在一个线程中，IO设备的龟速和CPU高速的执行能力之间的严重不匹配，多线程和多进程只是解决这一问题的一种方法
# 另一种方法是：异步IO------当代码 需要执行一个耗时的IO操作时，它只发出IO指令，并不等待IO的结果，然后就去执行其他代码了
#                          一段时间后，当IO返回结果时，再通知CPU进行处理
# 同步IO模型下，主线程只能挂起，但异步IO模型下，主线程并没有休息，而是在消息循环中继续处理其他消息
# 普通无异步IO处理的代码：
# def do_some_code():
#     f  = open('./ioFile/test.txt', 'r')
#     r = f.read()    # <=== 线程停在此处等到IO的操作结果
#     # IO操作完以后线程才能继续执行
#     do_some_code(r)


# 异步IO模型需要一个消息循环，在消息循环中，主线程不断地重复"读取消息-处理消息"这一过程
# 在异步IO模型下，一个线程就可以同时处理多个IO请求，并且没有切换线程的操作
# 对于大多数IO密集型的应用程序，使用异步IO将大大提升系统的多任务处理能力。
# def get_event_loop():
#     pass
#
#
# def process_event():
#     pass
#
#
# looped = get_event_loop()
#
# while True:
#     event = looped.get_event()
#     process_event(event)


# ---------------------------协程---------------------------
# 学习异步IO之前，先了解一下协程
# 协程----又名微线程
# 子程序，又称为函数。在所有语言中都是层级调用：A调用B，B执行时又调用C，C执行完毕返回，B执行完返回，最后A执行完毕
# 所以子程序是通过栈实现的，一个线程就是执行一个子程序，子程序的调用总是一个入口，依次返回，调用顺序是明确的。
# -------
# 而协程和子程序很像，但是又不一样：
#   协程看起来也是子程序，但执行过程中，在子程序内部可以中断，然后转而执行别的子程序，在适当的时候再返回来接着执行
def A():
    print('1')
    print('2')
    print('3')


def B():
    print('x')
    print('y')
    print('z')


# 按协程的概念：执行A的同时可以随时中断去执行B，B也可以随时中断去执行A
# 协程有点在于是一个线程执行，
# 第一大优势：
#   协程的执行效率极高，因为子程序切换不是线程切换，而是由程序自身控制，因此没有线程切换的开销，和多线程相比，线程数量越多，协程的性能优势就越明显
# 第二大优势：
#   协程不需要多线程锁的机制，因为只有一个线程，也不存在同时写变量的冲突
#   在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多

# 因为协程是一个线程执行，那怎么利用多核CPU呢？
#   最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
#   Python对协程的支持是通过generator实现的。

# 在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。
# Python的yield不但可以返回一个值，它还可以接收调用者发出的参数
def customer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CUSTOMER] Consuming %s...' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCE] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = customer()
produce(c)


# --------------------------asyncio-------------------------
# asyncio是Python3.4版本引入的标准库，直接内置了对异步IO的支持
# asyncio的编程就是一个消息循环，从该模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
import asyncio


@asyncio.coroutine
def hello():
    print("Hello Python")
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!")


# 获取EventLoop：
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
