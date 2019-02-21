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
import os


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
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================ 2 =========================
# 服务端接受信息
while 1:
    conn, addr = sk.accept()
    print(addr)
    while 1:
        server_recvData = conn.recv(1024)
        cmd, file_name, file_size = str(server_recvData, 'utf-8').split("|")
        path = os.path.join(BASE_DIR, 'cloud_file', file_name)
        file_size = int(file_size)

        has_receive = 0
        f = open(path, 'ab')
        while has_receive != file_size:
            data = conn.recv(1024)
            f.write(data)
            has_receive += len(data)
        print("...文件上传到云端了...")
        f.close()

# 关闭conn对象的通信
conn.close()


