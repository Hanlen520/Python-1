#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/7 20:19
# FileName: 03urlllibInterface_requests.py
# Description: 
# Question: 
# --------------------------------

import urllib.request
import urllib.parse

get_url = 'http://www.baidu.com'

def get_request():
    ru = urllib.request.Request(url=url)
    print('ru: ', ru)  # <urllib.request.Request object at 0x00000186E56117B8> 对象

    ru_response = urllib.request.urlopen(ru)
    print('ru_response: ', ru_response)  # <http.client.HTTPResponse object at 0x0000028268A613C8>

    print('getcode: ', ru_response.getcode())
    print('headers: ', ru_response.headers)
# get_request()


post_url = 'http://www.tuling123.com/openapi/api'
post_data = {
    'key': "Your",
    'info': '你好'
}

def post_request():
    data = urllib.parse.urlencode(post_data).encode('utf-8')
    rp = urllib.request.Request(post_url, data)
    rp_response = urllib.request.urlopen(rp)

    print('getcode: ', rp_response.getcode())
    print('msg', rp_response.msg)
    print('read', rp_response.read())
# post_request()


