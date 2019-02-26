#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/24 20:56
# FileName: D14_02进程_进程通信和数据共享.py
# Description:
#   进程之间数据不共享的
# Question:
# --------------------------------------

from multiprocessing import Process, Queue, Pipe, Manager


def f1(q):
    # NameError: name 'q' is not defined
    q.put([42, 3, 'Hello'])
    print("q 进程id: ", id(q))


def f2(conn):
    conn.send([42, None, "Process"])
    conn.close()


def f3(d, l, n):
    d[n] = '1'
    d[2] = 2
    d[0.25] = None
    l.append(d)
    print(l)


if __name__ == "__main__":
    # 进程之间实现数据的共享
    q = Queue()
    print("main q 进程id: ", id(q))
    p_list = []
    for i in range(3):
        p1 = Process(target=f1, args=(q, ))
        p_list.append(p1)
        p1.start()

    print(q.get())
    print(q.get())
    print(q.get())

    for p in p_list:
        p.join()

    # 进程之间实现数据的共享
    parent_conn, child_conn = Pipe()
    p2 = Process(target=f2, args=(child_conn, ))
    p2.start()
    print(parent_conn.recv())   # [42, None, 'Process']
    p.join()

    # 进程之间实现进程的通信
    # manager = Manager()
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))

        m_list = []
        for i in range(10):
            m = Process(target=f3, args=(d, l, i))
            m.start()
            m_list.append(m)

        for m in m_list:
            m.join()





