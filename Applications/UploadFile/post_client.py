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
import os

# 1.创建客户端的socket对象
sk = socket.socket()

# 2.建立与服务器通信的IP地址绑定
address = ('127.0.0.1', 8000)
sk.connect(address)

# 3. 获取要上传文件的路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)     # C:\MySpace\Python\Applications\UploadFile


# =============================== 2 =================
# 客户端发送信息
while True:
    # 输入操作方式和要上传的文件
    inp = input("CLIENT INPUT>>>").strip()

    # 分离输入的值  post|upload_file.txt
    # cmd --- 文件操作的方式 post
    # path --- 文件操作路径  post_file.txt
    cmd, path = inp.split("|")
    path = os.path.join(BASE_DIR, path)

    # 获取文件名称和文件大小
    file_name = os.path.basename(path)
    file_size = os.stat(path).st_size

    # 打包文件信息
    file_info = "post|%s|%s" % (file_name, file_size)
    sk.sendall(bytes(file_info, 'utf-8'))

    # 定义变量已经传送的数据
    has_sent = 0
    while has_sent != file_size:
        with open(path, 'rb') as f:
            data = f.read(1024)
            sk.sendall(data)
            has_sent += len(data)

    print("...上传成功")


# 关闭客户端与服务端的通信
sk.close()





