#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 20networkProgramming.py
# author:
# description:


# -----------------TCP/IP简介------------------
# 为了实现全球通用的网络通信协议，采用了互联网协议簇（Internet Protocol Suite）
# Internet = inter + net
# TCP和IP协议是网络通信中最重要的两个通信协议，大家把互联网的协议简称TCP/IP协议
# IP地址对应的实际上是计算机的网络接口，通常是网卡
# IP协议负责把数据从一台计算机通过网络发送到另一台计算机。数据被分割成一小块一小块，然后通过IP包发送出去
# 由于互联网链路复杂，两台计算机之间经常有多条线路，因此，路由器就负责决定如何把一个IP包转发出去
# P包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
# IP地址实际上是一个32位整数（称为IPv4）
# IPv6地址实际上是一个128位整数

# TCP协议则是建立在IP协议之上的
# TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达
# TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发
# 许多常用的更高级的协议都是建立在TCP协议基础上的，比如用于浏览器的HTTP协议、发送邮件的SMTP协议等
# 一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口

# 端口的作用：
# 因为同一台计算机上跑着多个网络程序。一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分
# 每个网络程序都向操作系统申请唯一的端口号
# 这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号
# 一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。


# -------------------TCP编程----------------
# Socket是网络编程的一个抽象概念
# 通常用一个Socket表示---打开了一个网络连接，而打开一个Socket需要知道目标计算机的IP地址和端口号，再指定协议类型即可

# 客户端
# 创建TCP连接时，主动发起的连接叫客户端，被动响应连接的叫服务器

# 基于TCP连接创建的Socket：
# import socket
#
# # 创建一个socket
# # AF_INET指定使用IPv4协议；IPv6，就指定为AF_INET6
# # SOCK_STREAM指定使用面向流的TCP协议，这样Socket对象就创建成功，但是还没有建立连接。
# import threading
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 建立连接
# # 客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号
# # IP地址可以用域名www.360.net自动转换到IP地址，但是怎么知道360服务器的端口号呢？
# # 答案是作为服务器，提供什么样的服务，端口号就必须固定下来。
# # 由于我们想要访问网页，因此360提供网页服务的服务器必须把端口号固定在80端口，因为80端口是Web服务的标准端口
# # 其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口
# # 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
# # 注意参数是一个tuple，包含地址和端口号。
# s.connect(('www.sina.com.cn', 80))
#
#
# # 发送数据
# # TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要根据具体的协议来决定
# # HTTP协议规定客户端必须先发请求给服务端，服务器收到后才发数据给客户端
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#
# # 接受数据
# # 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环
# buffer = []
# while True:
#     # 每次最多接受一个字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
#
# data = b''.join(buffer)
#
# # 关闭连接
# s.close()
#
# # 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接受的数据写入文件
# with open('./ioFile/sina.html', 'wb') as f:
#     f.write(html)
#
#
# # 服务器
# # 服务器进程首先要绑定一个端口并监听来自其他客户端的连接
# # 如果某个客户端连接过来了，服务器就与该客户端简历Socket连接，随后的通信就靠这个Socket连接了
# # 所以，服务器就会打开固定端口（比如80）监听，每来一个客户端连接就创建一个Socket连接
# # 由于，服务器会有大量来自客户端的连接，所以，服务器要能区分Socket连接是和那个客户端绑定的
# # 一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来确定一个Socket
# # 服务器还需要同时响应多个客户端的请求，每个连接都需要一个新的进程或者新的线程来处理，否则服务器一次就只能服务一个客户端了
#
# # 下面创建一个客户端与服务端简单通信的例子
# import socket
#
# # 创建一个基于IPV4和TCP协议的Socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 监听端口
# s.bind('127.0.0.1', 9999)
#
# # 调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量
# s.listen(5)
# print("Waiting for connection...")
#
# # 通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
# while True:
#     # 接受一个新的连接
#     sock, addr = s.accept()
#     # 创建新线程来处理TCP连接
#     t = threading.Thread(target=tcplink, args=(sock, addr))
#     t.start()
#
#
# # 每个连接都必须创建新线程（或进程）来处理，否则单线程在处理连接的过程中，无法接受其他客户端的连接
# def tcplink(sock, addr):
#     print("Accept new connection form %s: %s" % addr)
#     sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if not data or data.decode('utf-8') == 'exit':
#             break
#         sock.send('Hello, %s!' % data.decode('utf-8').encode('utf-8'))
#     sock.close()
#     print('Connection from %s: %s closed.' % addr)
#
#
# # 测试服务器的客户端程序
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接
# s.connect('127.0.0.1', 9999)
# # 接受欢迎消息
# print(s.recv(1024).decode('utf-8'))
# for data in [b'Michel', b'Tracy', b'Sarah']:
#     # 发送数据
#     s.send(data)
#     print(s.recv(1024).decode('utf-8'))
# s.send(b'exit')
# s.close()


# --------------------------UDP编程-----------------------
# TCP是简历可靠连接，并且通信双方都可以以流的形式发送数据
# UDP则是面向无连接的协议，使用UDP协议是不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发送数据包，但是能不能到达就不知道了
# 虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议
# 和TCP类似，使用UDP的通信双方也分为客户端和服务器，服务器首先需要绑定端口
import socket

su = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 锁定端口号
su.bind(('127.0.0.1', 8888))

# 创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP
# 绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据
print('Bind UDP on 8888...')
while True:
    # 接受数据
    # recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
    data, addr = su.recvfrom(1024)
    print("Received from %s: %s" % addr)
    su.sendto(b'Hello, %s!' % data, addr)


# 客户端基于UDP时，首先仍然创建基于UDP的Socket。然后，不需要调用connect(), 直接通过sendto()给服务器发数据

