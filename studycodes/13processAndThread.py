#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 13processAndThread.py
# author:
# description:

# ------------------*************导读************------------------------
# 实现多任务的方式：
#   1. 多进程(multiprocessing)模式
#   2. 多线程模式
#   3. 多进程 + 多线程模式
# 线程是最小的执行单元，而进程由至少一个线程组成


# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，
# 但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），
# 然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID，这样一个父进程可以fork出很多的子进程
# 父进程要记下每个子进程的ID, 而子进程只需要调用getppid()就可以拿到父进程的ID
# Python的os模块封装了常见的系统调用, 其中就包括fork, 可以在Python程序中轻松创建子进程
import os


print("Process (%s) start..." % os.getpid())

# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# print(pid)

# if pid == 0:
#     print("I am child process (%s) and my parent is %s" % (os.getpid(), os.getppid()))
# else:
#     print("I (%s) just created a child process (%s)." % (os.getpid(), pid))
# 有了fork调用, 一个进程在接受到新任务时就可以复制出一个子进程来处理新任务


# multiprocessing模块就是跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来代表一个进程对象
# from multiprocessing import Process
# import os
#
#
# # 子进程要执行的代码
# def run_pro(name):
#     print("Run child process %s (%s)..." % (name, os.getpid()))
#
#
# if __name__ == "__main__":
#     print("Parent process %s" % os.getpid())
#     p = Process(target=run_pro, args=('test', ))
#     print("Child process will start.")
#     p.start()
#     p.join()
#     print("Child process end.")
#
#
# # Pool--启动大量的子进程, 可以使用进程是池的方法批量创建子进程
# from multiprocessing import Pool
# import os, time, random
#
#
# print("================Pool==========================")
#
#
# def long_time_task(name):
#     print("Run task %s (%s)..." % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print("Task %s runs %0.2f second." % (name, (end - start)))
#
#
# if __name__ == "__main__":
#     print("Parent process %s." % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))
#     print("Waiting for all subprocess done...")
#     p.close()
#     p.join()
#     print("All subprocess done.")
#
# # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
# # 调用close()之后就不能继续添加新的Process了
#
#
# # 子进程-----subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
# # import subprocess
# #
# # print('$ nslookup www.python.org')
# # r = subprocess.call(['nslookup', 'www.python.org'])
# # print('Exit code:', r)
#
#
# # 如果子进程还需要输入，则可以通过communicate()方法输入
# # print('$ nslookup')
# # p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# # print(output.decode('utf-8'))
# # print('Exit code:', p.returncode)
#
#
# # 进程间通信
# # Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
# from multiprocessing import Process, Queue
# import os, time, random
#
#
# # 写数据进程执行的代码
# def write(q):
#     print("Process to write: %s" % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print("Put %s to queue..." % value)
#         q.put(value)
#         time.sleep(random.random())
#
#
# # 读数据进程执行的代码
# def read(q):
#     print("Process to read: %s" % os.getpid())
#     while True:
#         value = q.get(True)
#         print("Get %s from queue." % value)
#
#
# if __name__ == "__main__":
#     # 父进程创建Queue,并传给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q, ))
#     pr = Process(target=read, args=(q, ))
#
#     # 启动子进程pw, 写入
#     pw.start()
#
#     # 启动子进程pr, 读取
#     pr.start()
#
#     # 等待结束
#     pw.join()
#
#     # pr是死循环无法结束, 只能强行终止
#     pr.terminate()


# ------------------*************多线程************------------------------
# 多成武可以有多进程完成，也可以由一个进程内的多线程完成
# 进程由若干个线程组成，一个进程至少有一个线程
# 由于线程是操作系统直接支持的执行单元，Python都内置多线程的支持
# Python提供两个模块，_thread（低级模块）和threading（高级模块），但threading高级模块对低级模块_thread进行了封装
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
# import time
# import threading
#
#
# # 新线程执行的代码
# def loop():
#     # 提示某个线程启动了
#     print("thread %s is running...." % threading.current_thread().name)
#
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
#
# print('thread %s is running...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)
# 由于任何默认进程就会启动一个线程，该线程称为主线程，主线程又可以启动新的线程
# Python的threading模块有个current_thread()函数，它永远返回当前线程的实例
# 主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
# 名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……


# Lock
# 多进程：同一个变量，各自有一份拷贝存在于每个进程中，互不影响
# 多线程：所有变量都由所有线程共享，所以任何一个变量都可以被任何一个线程修改，因此线程之间共享数据最大的危险在于多个线程同时更改一个变量，把内容改乱了
# 好处：锁的好处就是确保了某段关键代码只能由一个线程从头到尾完整地执行
# 坏处：首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
#       由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止

# 例如下例：
# import time
# import threading
#
#
# # 假定这是自己的银行存款
# balance = 0
#
#
# def change_in(n):
#     # 先存后取，结果应该为0
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# # def run_thread(n):
# #     for n in range(100000):
# #         change_in(n)
#
# lock = threading.Lock()
#
#
# def run_thread(n):
#     for i in range(100000):
#         # 先获取锁
#         lock.acquire()
#         try:
#             # 放心使用
#             change_in(n)
#         finally:
#             # 使用完锁后要释放
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5, ))
# t2 = threading.Thread(target=run_thread, args=(8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('In the end, my balance is: %s' % balance)
# 两个线程同时一存一取，就可能导致余额不对，我们必须确保一个线程在修改balance时，别的线程一定不能改
# 当一个线程执行时，加上一把锁threading.Lock()，其他的线程不能再同时执行相同方法


# 多核CPU
# 要想把N核CPU的核心全部跑满，就必须启动N个死循环线程
# 写个死循环：
# import threading
# import multiprocessing
#
#
# def loop():
#     x = 0
#     while True:
#         x = x + 1
#
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()


# ------------------*************ThreadLocal************------------------------
# 在多线程环境下，每个线程都有自己的数据
# 一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有自己的线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁
# 但局部变量在函数调用时传递起来很麻烦
# def process_student(name):
#     std = Student(name)
#
#     # std是局部变量，但是每个函数都要用它，因此必须传进去
#     do_task_1(std)
#     do_task_2(std)
#
# def do_task_1(std):
#     do_subtask_1(std)
#     do_subtask_2(std)
#
#
# def do_task_2(std):
#     do_subtask_2(std)
#     do_subtask_2(std)

import threading


# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()


# ------------------*************进程VS线程************------------------------
# 实现多任务，通常我们会设计Master-Worker模式，Master负责分配任务，Worker负责执行任务，因此，多任务环境下，通常是一个Master，多个Worker
# 如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker
# 如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker
# 多进程--优点：稳定性高，一个子进程崩溃了，不会影响主进程和其他子进程--------Apache就是采用多进程的模式
#        缺点：多个进程操作系统调度会成问题
# 多线程--缺点：一个线程挂掉就可能直接造成整个进程崩溃，因为所有线程共享进程的内存


# 线程切换


# 计算密集型vs.IO密集型
# 计算密集型：需要大量的计算，消耗CPU资源，例如计算圆周率-----Python这样的脚本语言运行效率很低不适合计算密集型任务（用C）
# IO密集型：设计到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是----CPU消耗很少，任务大大部分时间都在等待IO操作完成
#          （IO的速度远远低于CPU和内存的速度），对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言


# 异步IO
# 由于CPU和IO之间巨大的速度差异，一个任务在执行的过程中大部分时间都在等待IO操作
# 单进程单线程任务模型会导致别的任务无法并行执行，因此，我们才需要多进程模型或者多线程模型来支持多任务并发执行
# 事件驱动型------充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务
# Nginx就是支持异步IO的Web服务器，它在单核CPU上采用单进程模型就可以高效地支持多任务
# 对应到Python语言，单线程的异步编程模型称为协程


# ------------------*************分布式进程************------------------------
# 在Thread和Process中，应当优先选Process，因为Process更稳定
# Process可以分布到多台机器上
# 而Thread最多只能分布到同一台机器的多个CPU上
# Python的multiprocessing模块不但支持多进程，
# 其中managers子模块还支持把多进程分布到多台机器上


# 例子：有一个通过Queue通信的多进程程序在同一台机器上运行，现在，由于处理任务的进程任务繁重，
#       希望把发送任务的进程和处理任务的进程分布到两台机器上。怎么用分布式进程实现？
#       原有的Queue可以继续使用，但是，通过managers模块把Queue通过网络暴露出去，就可以让其他机器的进程访问Queue了
# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')


# 在另一台机器上启动任务进程（本机上启动也可以）
# task_worker.py

import time, sys, queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
# 从网络连接:
m.connect()
# 获取Queue的对象:
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')






