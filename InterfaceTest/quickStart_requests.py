#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/6 11:07
# FileName: quickStart_requests.py
# Description: 
# Question: 
# --------------------------------

import requests
# import demjson
import json

# ==获取 GitHub 的公共时间线
# So现在，我们就得到了一个名为 r 的 Response 对象
def send_request():
    r = requests.get('https://api.github.com/events')
    print('Response对象：', r.text)

    # requests 的请求类型：
    # GET
    r_get = requests.get('http://httpbin.org/get', data={'key': 'value'})
    print('r_get: ', r_get.text)

    # POST
    r_post = requests.post('http://httpbin.org/post', data={'key': 'value'})
    print('r_post: ', r_post.text)

    # PUT
    r_put = requests.put('http://httpbin.org/put', data={'key': 'value'})
    print('r_put: ', r_put.text)

    # DELETE
    r_delete = requests.delete('http://httpbin.org/delete')
    print('r_delete: ', r_delete.text)

    # DEAD
    r_head = requests.head('http://httpbin.org/get')
    print('r_head: ', r_head.text)

    # OPTIONS
    r_options = requests.options('http://httpbin.org/get')
    print('r_options: ', r_options.text)


# ==传递 URL 参数
def pass_parameters():
    payload = {
        'key1': 'value1',
        'key2': 'value2'
    }
    r_payload = requests.get("http://httpbin.org/get", params=payload)
    print("r_payload.url", r_payload.url)


# ==响应内容
def response_content():
    r_content = requests.get('https://api.github.com/events')

    # 文本式响应
    r_text = r_content.text
    print("r_text: ", r_text)

    # 查看文本编码
    r_coding = r_content.encoding
    print("r_coding: ", r_coding)

    # 二进制响应内容
    r_content = r_content.content
    print("r_content: ", r_content)

    # JSON响应内容（AttributeError: 'bytes' object has no attribute 'json'）
    # r_json = r_content.json
    # print("r_json: ", r_json)

    # 原始响应内容
    r_origin = requests.get("https://api.github.com/events",  stream=True)
    r_raw = r_origin.raw
    r_raw_read = r_raw.read(10)
    print("r_raw: ", r_raw)
    print("r_raw_read: ", r_raw_read)

    # 将数据流保存到文本中
    with open('r_content.txt', 'wb') as fb:
        for chunk in r_origin.iter_content(50):
            fb.write(chunk)

# response_content()

# ==定制请求头
def custom_request_header():
    url = 'https://api.github.com/some/endpoint'
    headers = {
        'user-agent': 'application/json'
    }

    r = requests.get(url, headers=headers)
    print(r)

# custom_request_header()


# ==更加复杂的 POST 请求
def post_request():
    # 传入字典：数据字典会在发送请求时会自动编码为表单形式
    payload1 = {
        'key1': 'value1',
        'key2': 'value2'
    }
    r1 = requests.post("http://httpbin.org/post", data=payload1)
    r1_text = r1.text
    print('r1_text: ', r1_text)

    # 传入元组：应用于在表单中多个元素使用同一 key 的时候
    payload2 = (
        ('key1', 'values1'),
        ('key2', 'values2')
    )
    r2 = requests.post("http://httpbin.org/post", data=payload2)
    r2_text = r2.text
    print('r2_text: ', r2_text)

    # 如果你传递一个 string 而不是一个 dict， 那么数据会被直接发布
    url = 'https://api.github.com/some/endpoint'
    payload3 = {
        'some': 'data'
    }
    r3 = requests.post(url, data=payload3)
    r3_text = r3.text
    print('r3_text: ', r3_text)
    r4 = requests.post(url, data=json.dumps(payload3))
    r4_text = r4.text
    print('r4_text: ', r4_text)

# post_request()


# ==POST 一个多部分编码（Multipart-Encoded）的文件
def post_multipart_file():
    url = 'http://httpbin.org/post'
    files = {
        # 显式滴设置文件名，文件类型和请求头
        'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})
    }
    r = requests.post(url, files=files)
    print(r.text)

    files2 = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
    r2 = requests.post(url, files=files2)
    print(r2.text)

post_multipart_file()


