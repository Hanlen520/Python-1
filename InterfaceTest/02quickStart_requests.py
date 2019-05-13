#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/7 10:42
# FileName: 23quickStart_requests.py
# Description: 
# Question: 
# --------------------------------
import requests

url = 'http://httpbin.org/get'
bad_url = 'http://httpbin.org/status/404'
cookies_url = 'http://example.com/some/cookie/setting/url'
cookies_server_url = 'http://example.com/some/cookie/setting/url'
redirect_url = 'http://github.com'

def response_code():
    r = requests.get(url)
    r_code = r.status_code
    print(r_code)

    # requests 内置状态码查询对象
    if requests.codes.ok == r_code:
        print("---ok---")

    # 请求错误，response.raise_for_status() 抛出异常
    br = requests.get(bad_url)
    br_code = br.status_code
    print("br_code: ", br_code)
    print("br.raise_for_status: ", br.raise_for_status())
    print("r.raise_for_status: ", r.raise_for_status())
# response_code()

def response_headers():
    r = requests.get(url)
    r_headers = r.headers
    print('r_headers: ', r_headers)
# response_headers()


def get_cookie():
    r = requests.get(cookies_url)
    r_cookie = r.cookies
    # 返回一个 <RequestsCookieJar[]> 的对象，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用
    jar = requests.cookies.RequestsCookieJar()
    jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
    jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
    r2 = requests.get(cookies_server_url, cookies=jar)
    print('r2.text', r2.text)

    print('r_cookie: ', r_cookie)

    # 发送自己的 cookies 到服务器
    cookies = dict(cookies_are='working')
    rs = requests.get(cookies_server_url, cookies=cookies)
    print('rs.text: ', rs.text)
# get_cookie()


# ==重定向与请求历史
def redirect_history():
    r = requests.get(redirect_url)
    r_url = r.url
    print('r_url: ', r_url)
    r_code = r.status_code
    print('r_code: ', r_code)

    # 请求历史
    r_history = r.history
    print('r_history: ', r_history)

    # 参数禁用重定向处理
    r_no = requests.get(redirect_url, allow_redirects=False)
    print('r_no.status_code: ', r_no.status_code)
    print('r_no.history: ', r_no.history)

    # 使用 DEAD，启用重定向
    r_start_redirect = requests.get(redirect_url, allow_redirects=True)
    print('r_start_redirect.status_code: ', r_start_redirect.status_code)
    print('r_start_redirect.history: ', r_start_redirect.history)
# redirect_history()

def timeout():
    r = requests.get(redirect_url, timeout=5)
    print(r)
# timeout()

butian_url = 'https://butian.360.cn'
def test_butian():
    r = requests.get(butian_url)
    print('r_url: ', r.url)
    print('r_history: ', r.history)
# test_butian()

z_url_cn = 'https://butian.360.cn'
z_url_net = 'https://butian.360.net'
def test_zhongce_butian():
    r_cn = requests.get(z_url_cn)
    print('r_cn: ', r_cn.url)
    print('r_history: ', r_cn.history)
test_zhongce_butian()

import urllib
