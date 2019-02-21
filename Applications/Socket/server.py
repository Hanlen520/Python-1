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


# family: AF_INET---服务器之间的通信、
#         AF_UNIX---UNIX不同进程之间的通信
#
# type: SOCK_STREAM --- TCP
#       SOCK_Dgram---UDP


# sk = socket.socket(family=AF_INET, type=SOCK_STREAM)
# 1.创建服务端的socket对象
sk = socket.socket()
# print(sk)
# <socket.socket fd=564, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>

# 2.绑定服务器的通信IP地址
address = ('127.0.0.1', 8000)
sk.bind(address)

# 3.创建监听的最大连接数
sk.listen(3)
print("waiting.....等待连接")

# 4.accept阻塞，等待别人连接它
# 一旦客户端有连接则返回下面的返回值
# (<socket.socket fd=472, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8000), raddr=('127.0.0.1', 63898)>, ('127.0.0.1', 63898))
# conn = sk.accept()
# print(conn)
conn, addr = sk.accept()

# 服务端发送信息
# send, sendall发送数据都是bytes类的数据
inp = input(">>>")
conn.send(bytes(inp, 'utf-8'))
# 关闭conn对象的通信
conn.close()






# ============================ 2 =========================
# 服务端接受信息
# server_revData = conn.recv(1024)
# print(str(server_revData, 'utf-8'))


