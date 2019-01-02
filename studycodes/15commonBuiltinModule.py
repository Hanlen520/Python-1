#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 14commonBuiltinModule.py
# author:
# description:

# Python称之为Batteries included
# ----------------------------------**********datetime**********------------------------------
import urllib
from datetime import datetime


# 获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))


# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)


# datetime转换为timestamp
# 把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，记为0（1970年以前的时间timestamp为负数）


# timestamp转换为datetime, 使用datetime提供fromtimestamp()方法：
from datetime import datetime


t = 1429417200.0
print("============fromtimestamp==============")
print(datetime.fromtimestamp(t))        # 本地时间
print(datetime.utcfromtimestamp(t))     # UTC时间


# str转换为datetime
# 很多时候用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime------用datetime.strptime()实现
from datetime import datetime


cday = datetime.strptime('2018-7-31 20:48:36', '%Y-%m-%d %H:%M:%S')
print("============strptime==============")
print(cday)


# datetime转换为str
# 有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的
from datetime import datetime


now = datetime.now()
print("============strftime==============")
print(now.strftime('%a, %b %d %H:%M'))


# datetime加减
# 对日期和时间进行加减可以用+/-，不过需要导入timedelta这个类
from datetime import datetime, timedelta


dnow = datetime.now()
print("============dnow==============")
print(dnow)
print(dnow + timedelta(hours=10))
print(dnow - timedelta(days=1))
print(dnow + timedelta(days=2, hours=12))


# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None
from datetime import datetime, timedelta, timezone


# 创建时区UTC+8：00
tz_utc_8 = timezone(timedelta(hours=8))
tnow = datetime.now()
print("============tnow==============")
print(tnow)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)


# 时区转换
# 先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print("============utc_dt==============")
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)



# ----------------------------------**********collections**********------------------------------
# collections是Python内建的集合模块

print("\n")
print("\n")
print("\n")
# namedtuple
# tuple表示不变集合，用tuple来表示一个点tp = (1, 2)，看不出来
# namedtuple是一个函数，可以用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的元素
print("==========namedtuple===========")
from collections import namedtuple


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(isinstance(p, Point))
print(isinstance(p, tuple))


# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque实现了高效插入和删除操作的双向列表，适合与队列和栈
from collections import deque


q = deque(['a', 'b', 'c'])
q.append('x')
print("==========deque===========")
print(q)
q.appendleft('y')
print(q)
q.popleft()
print(q)


# defaultdict
# 使用dict的时候，如果key不存在会报KeyError, 如果不存在key可以用defaultdict返回一个默认值
from collections import defaultdict


dd = defaultdict(lambda :'N/A')
dd['key1'] = 'abc'
print("============defaultdict==================")
print(dd['key1'])
print(dd['key2'])


# OrderedDict
# 使用dict的时候，key是无效的，所以在对dict做迭代的时候，无法确定key的顺序
# 若要保持key的顺序，使用OrderedDict
from collections import OrderedDict


d1 = dict([('a', 1), ('b', 2), ('c', 3), ('f', 5), ('e', 4)])
print("-----------OrderedDict-----------")
print(d1)
d2 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('f', 5), ('e', 4)])
print(d2)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
d3 = OrderedDict()
d3['z'] = 1
d3['x'] = 2
d3['y'] = 4
print(list(d3.keys()))
# OrderedDict实现一个先进先出FIFO的dict，当容量超出限制的时候，删除最早添加的key
from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity


    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter
# Counter是一个简单的计数器，统计字符出现的个数, Counter实际上是dict的一个子类
from collections import Counter


c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1


print(c)


# ------------------------*********base64**********--------------------------
# 用64个字符表示任意二进制数据
import base64


a = base64.b64encode(b'binary\x00string')
print(a)
b = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print(b)
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容


# ------------------------*********struct**********--------------------------
# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
# struct的pack函数把任意数据类型变成bytes
import struct


# '>I': >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
sa = struct.pack('>I', 10240099)
print(sa)


# >IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
sb = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')


# 解读位图.bmp
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
sc = struct.unpack('<ccIIIIIIHH', s)
print(sc)


# ------------------------*********hashlib**********--------------------------
# 摘要算法简介
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
# 摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难


# 计算一个字符串的MD5值
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
import hashlib


md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print("==========md5==========")
print(md5.hexdigest())


# 另一种常见的摘要算法是SHA1
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
import hashlib


sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print("==========sha1==========")
print(sha1.hexdigest())


# 摘要算法应用
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误


# ------------------------*********hmac**********--------------------------
# 判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果，如果一致，用户输入的口令就是正确的
# 为了防止黑客通过彩虹表根据哈希值反推原始口令
# 计算哈希的时候，不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希，增加破解的难度
# md5(message + salt)
# 采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全
import hmac


# hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes
message = b'Hello, Python!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
hd = h.hexdigest()
print('\n')
print("=============hd==============")
print(hd)


# ------------------------*********itertools**********--------------------------
# Python的内建模块itertools提供用于操作迭代对象的函数
import itertools


print('\n')
print("=============itertools==============")
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
nsre = list(ns)
print(nsre)

# natuals = itertools.cycle('ABC')
# natuals = itertools.repeat('A', 3)
# for n in natuals:
#     print(n)


# itertools----chain()
print('\n')
print("=============chain==============")
chained = itertools.chain('ABC', 'XYZ')
for c in chained:
    print(c)


# itertools----groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起
print('\n')
print("=============groupby==============")
groupbyed = itertools.groupby('ABCAAaaBBBBCCCCAAAADDD', lambda gb: gb.upper())
for g, group in groupbyed:
    print(g, list(group))


# ------------------------*********contexlib**********--------------------------
# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的， 就可以用with语句了
# class Query('object'):
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('begin')
#         return self
#
#     def __exit__(self, exc_type, exc_val, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)


# with Query('Bob') as q:
#     q.query()


# @contextmanager
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法
# from contextlib import contextmanager
#
#
# class Query(object):
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print("query info about %s" % self.name)
#
#
# @contextmanager
# def create_query(name):
#     print("Begin")
#     q = Query(name)
#     yield q
#     print("End")


# ------------------------*********urllib**********--------------------------
# Get
# urllib的request模块可以非常方便的抓取URL的内容
# 也就是发送一个GET请求到指定的页面，然后返回HTTP的响应
from urllib import request


print("\n")
print("====================urllib======================")
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print("Status", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s: %s" % (k, v))
    print('Data:', data.decode('utf-8'))


# Post
from urllib import request, parse


print("Login to my weibo.cn......")
email = input("Email: ")
passwd = input("Password: ")


login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))


# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理
proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass


# ------------------------*********XML**********--------------------------
# DOM vs SAX
# 操作XML有两种方法：DOM和SAX
# DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
# SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件
# 正常情况下，优先考虑SAX，因为DOM实在太占内存
# Python使用SAX解析XML非常简洁，通常关心的事件是start_element，end_element和char_data，这3个函数就可以解析xml
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)


xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''


handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)


# ------------------------*********HTMLParser**********--------------------------
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML
# Python提供了HTMLParser来非常方便地解析HTML
from html.parser import HTMLParser
from html.entities import name2codepoint


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('</%s>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)


parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')











































