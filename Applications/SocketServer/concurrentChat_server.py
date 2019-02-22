#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/2/21 7:23
# FileName: concurrentChat_server.py
# Description: 
# Question:
# --------------------------------------

import socket
import socketserver


# family: AF_INET---服务器之间的通信、
#         AF_UNIX---UNIX不同进程之间的通信
#
# type:
#       SOCK_STREAM --- TCP
#       SOCK_Dgram---UDP


# ====================== 1 ====================
# 服务端发送信息
# send, sendall发送数据都是bytes类的数据
# inp = input(">>>")
# conn.send(bytes(inp, 'utf-8'))


class ChatServer(socketserver.BaseRequestHandler):
    # handle中写的便是处理通信逻辑
    def handle(self):
        print("......服务端启动了......")
        conn = self.request
        print(self.client_address)

        while True:
            client_data = conn.recv(1024)
            print(str(client_data, 'utf-8'))
            print("waiting......")
            server_response = input("【SERVER】:")
            conn.sendall(bytes(server_response, 'utf-8'))


if __name__ == "__main__":
    # sk = socket.socket(family=AF_INET, type=SOCK_STREAM)
    # 1.创建服务端的socket对象
    # sk = socket.socket()
    # print(sk)
    # <socket.socket fd=564, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>
    # 2.绑定服务器的通信IP地址
    # address = ('127.0.0.1', 8000)
    # sk.bind(address)
    # 3.创建监听的最大连接数
    # sk.listen(3)
    # print("waiting.....等待连接")
    # 4.accept阻塞，等待别人连接它
    # 一旦客户端有连接则返回下面的返回值
    # conn = sk.accept()
    # print(conn)
    # conn, addr = sk.accept()
    # ===================下一行代码封装了上面的socket建立连接的过程===========================
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8000), ChatServer)
    server.serve_forever()


