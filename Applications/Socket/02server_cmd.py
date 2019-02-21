#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/21 7:23
# FileName: server.py
# Description: 
# Question:
# --------------------------------------

import socket
import subprocess


# family: AF_INET---服务器之间的通信、
#         AF_UNIX---UNIX不同进程之间的通信
#
# type:
#       SOCK_STREAM --- TCP
#       SOCK_Dgram---UDP


# sk = socket.socket(family=AF_INET, type=SOCK_STREAM)
# 1.创建服务端的socket对象
sk = socket.socket()
# print(sk)
# <socket.socket fd=564, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

# 2.绑定服务器的通信IP地址
address = ('127.0.0.1', 8888)
sk.bind(address)

# 3.创建监听的最大连接数
sk.listen(3)
print("waiting.....等待连接")


# 4.accept阻塞，等待别人连接它
# 一旦客户端有连接则返回下面的返回值
# (<socket.socket fd=472, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 63898)>, ('127.0.0.1', 63898))
# conn = sk.accept()
# print(conn)
# conn, addr = sk.accept()


# ============================ 2 =========================
# 服务端接受信息
while 1:
    conn, addr = sk.accept()
    print(addr)
    while 1:
        try:
            server_revData = conn.recv(1024)
        except Exception as e:
            print(e)
            break

        if not server_revData:
            break
        print('......', str(server_revData, 'utf-8'))
        # 一个client断开连接后，服务端不会退出
        # 如果有一个新的client开启后，会和服务端建立连接

        # 执行shell命令
        sub = subprocess.Popen(str(server_revData, 'utf-8'), shell=True, stdout=subprocess.PIPE)
        cmd_result = sub.stdout.read()
        cmd_result_len = bytes(str(len(cmd_result)), 'utf-8')

        conn.sendall(cmd_result_len)
        conn.sendall(cmd_result)

# 关闭conn对象的通信
conn.close()


