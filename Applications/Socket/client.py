#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/21 7:23
# FileName: client.py
# Description: 
# Question:
# --------------------------------------

import socket

# 1.创建客户端的socket对象
sk = socket.socket()

# 2.建立与服务器通信的IP地址绑定
address = ('127.0.0.1', 8000)
sk.connect(address)

# 客户端接受信息
client_revData = sk.recv(1024)
print(str(client_revData, 'utf-8'))

# 关闭客户端与服务端的通信
sk.close()





# =============================== 2 =================
# 客户端发送信息
# inp = input("client input>>>")
# sk.send(bytes(inp, 'utf-8'))




