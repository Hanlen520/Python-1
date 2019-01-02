#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 22connectDatabase.py
# author:
# description:
# questions:


# 软件开始主要运行在桌面上，而数据库这样的软件运行在服务器端，这种Client/Server模式简称CS架构
# CS架构不适合Web，最大的原因是Web应用程序的修改和升级非常迅速，而CS架构需要每个客户端逐个升级桌面App
# 这就开始了Browser/Server模式，简称BS架构：
# 在BS架构下，客户端只需要浏览器，应用程序的逻辑和数据都存储在服务器端。浏览器只需要请求服务器，获取Web页面，并把Web页面展示给用户
# Web应用经历的阶段：
#   1. 静态Web页面
#   2. CGI
#   3. ASP/JSP/PHP
#   4. MVC: Model-View-Controller
#   5. 异步开发
#   6. MVVM


# -------------------------HTTP协议简介-------------------------------
# HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信

# 打开Chrome浏览器的开发模式：
#   1. Elements显示网页的结构
#   2. Network显示浏览器和服务器的通信
#      ---：Response Headers，点击view source，显示服务器返回的原始响应数据
#      ---：Content-Type指示响应的内容，这里是text/html表示HTML网页
#      ---：浏览器就是依靠Content-Type来判断响应的内容是网页还是图片，是视频还是音乐

# 客户端响应的状态码：
# 200表示一个成功的响应，后面的OK是说明。
# 失败的响应有404 Not Found：网页不存在，
# 500 Internal Server Error：服务器内部出错

# HTTP请求流程：
#   1. 浏览器先向服务器发送HTTP请求，请求包括：
#       （1）方法：GET还是POST，GET仅请求资源；POST会附带用户数据，还会请求包括一个Body，包含用户数据
#       （2）路径：/full/url/path
#       （3）域名：由Host头指定：Host：www.sina.com.cn
#       （4）以及其他相关的Header
#   2. 服务器向浏览器返回HTTP请求，响应包括
#       （1）响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；
#       （2）响应类型：由Content-Type指定
#       （3）以及其他相关的Header
#   3. 如果浏览器还需要继续向服务请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2
# 一个HTTP请求只处理一个资源

# HTTP格式
# 一个HTTP包含Header和Body两部分，其中Body是可选的
# 每个Header一行一个，换行符是\r\n
# 当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body。
# HTTP响应如果包含body，也是通过\r\n\r\n来分隔的
# 请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，如果是图片，Body就是图片的二进制数据。

# Web应用的实质：
#   1. 浏览器发送一个HTTP请求；
#   2. 服务器收到请求，生成一个HTML文档
#   3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器
#   4. 浏览器收到HTTP响应，从HTTP Body中取出HTML文档并显示


# -------------------------WSGI接口-------------------------------
# Apache、Nginx、Lighttpd等这些常见的静态服务器
# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求
# WSGI就是一个封装好的接口，是我们不用从底层的TCP连接、HTTP原始请求和响应格式开始。专注于生成HTML文档
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text-html')])
    return [b'<h1>Hello, web!</h1>']


# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
#       environ：一个包含所有HTTP请求信息的dict对象；
#       start_response：一个发送HTTP响应的函数


# -------------------------使用Web框架-------------------------------
# Flask

# -------------------------使用模板----------------------------------
# Flask