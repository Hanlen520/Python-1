#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: 16commonUsedThirdPartyModule.py
# author:
# description:


# 强烈推荐安装Anaconda，安装后，数十个常用的第三方模块就已经就绪，不用pip手动安装


# -----------------------Pillow---------------------------
# Pillow，支持最新Python 3.x，又加入了许多新特性

# 图像缩放操作
from PIL import Image

# 打开一个图像文件
im = Image.open('./ioFile/GitHubpng.png')
print("im: ", im)

# 获取文件的尺寸（宽和高）
w, h = im.size
print("Original image size: %spx %spx" % (w, h))

# 缩放到50%
im.thumbnail((w//2, h//2))
print("Rise image size: %spx %spx" % (w//2, h//2))

# 把缩放后的图片保存
im.save('./ioFile/thumbnailGithub.png', 'png')


# 模糊图像
from PIL import Image, ImageFilter

# 打开一个图片
imb = Image.open('./ioFile/GitHub.png')
print('imb: ', imb)

# 应用模糊滤镜
imb2 = imb.convert('RGB').filter(ImageFilter.BLUR)
imb2.save('./ioFile/blurGithub.png', 'png')


# PIL的ImageDraw提供了一系列绘图方法，可以直接绘图
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 生成随机字母
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 随机颜色2:
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('./ioFile/code.jpg', 'jpeg')



# -----------------------requests---------------------------
# 用于处理URL资源
# 使用requests，用GET访问页面
import requests


r = requests.get('http://www.douban.com/')
r_code = r.status_code
print('r_code: ', r_code)
r_text = r.text
# print(r_text)


# 带参数的URL，传入一个dict作为params参数
r_url = requests.get('http://www.douban.com/', params={'q': 'Python', 'cat': '1001'})
print("r_url: ", r_url.url)


# 自动检测编码
r_coding = r.encoding
print('r_coding: ', r_coding)


# 获取content
r_content = r.content
print('r_content: ', r_content)


# 对于特定类型的响应，例如json
r_type = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
r_json = r_type.json()
print('r_json: ', r_json)


# 需要传入HTTP Header时，我们传入一个dict作为headers参数
rh = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
r_headers = rh.text
print('r_header: ', r_headers)


# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据
rp = requests.get('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print('rp: ', rp.cookies)
# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数
params = {'key': 'value'}
rpa = requests.post(url='https://accounts.douban.com/login', json=params)
print('rpa: ', rpa.url)
# 类似的上传文件需要更加复杂的编码格式，但是requests可以把它简化成files参数
upload_files = {'file': open('./ioFile/test.txt', 'rb')}
ruf = requests.post(url='https://accounts.douban.com', files=upload_files)
print('ruf: ', ruf)


# requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie
rco = rpa.cookies
print('rco: ', rco)


# 在请求中传入Cookie, 只需要准备一个dict传入cookies参数
cs = {'token': '12345', 'status': 'working'}
rcs = requests.get(url='https://accounts.douban.com', cookies=cs, timeout=2.5)
print('rcs: ', rcs)


# -----------------------chardet---------------------------
# Python提供了Unicode表示的str和bytes两种数据类型，并且可以通过encode()和decode()方法转换
# 但是，在不知道编码的情况下，对bytes做decode()不好做
# chardet可以用来检测编码
import chardet


# 拿到一个bytes时，就可以对其检测编码
cr = chardet.detect(b'Hello Word')
print('cr: ', cr)


# 检测gbk
g_data = '遥遥不知你何方ss'.encode('gbk')
gbkr = chardet.detect(g_data)
print('gbkr: ', gbkr)


# 检测utf-8
utf_data = '你的笑'.encode('utf-8')
utfr = chardet.detect(utf_data)
print('utfr: ', utfr)


# 检测日文
j_data = '最新の主要ニュース'.encode('euc-jp')
jr = chardet.detect(j_data)
print('jr: ', jr)



# ------------------------psutil--------------------------
# psutil做系统监控


# 获取CPU信息
import psutil


# CUP的逻辑数量
l_count = psutil.cpu_count()
print('l_count: ', l_count)


# CPU的物理数
w_count = psutil.cpu_count(logical=False)
print('w_count: ', w_count)


# 统计CPU的用户/系统/空闲时间
c_count = psutil.cpu_times()
print('c_count: ', c_count)


# 动态每一秒查看CPU的运行情况
def per_cpu():
    for x in range(10):
        pc = psutil.cpu_percent(interval=1, percpu=True)
        print('pc: ', pc)


# per_cpu()


# 获取内存信息
# psutil可获取磁盘分区、磁盘使用率、磁盘IO情况
dp = psutil.disk_partitions()
print('dp: ', dp)
du = psutil.disk_usage('/')
print('du: ', du)
dic = psutil.disk_io_counters()
print('dic: ', dic)


# 获取网络信息
# psutil可以获取网络接口和网络连接信息
# 获取网络读写字节/包的个数
nic = psutil.net_io_counters()
print('nic: ', nic)


# 获取网络接口信息
nia = psutil.net_if_addrs()
print('nia: ', nia)


# 获取网络接口状态
nis = psutil.net_if_stats()
print('nis: ', nis)


# 获取当前网络连接信息
netc = psutil.net_connections()
print('netc: ', netc)


# 获取进程信息
print('所有进程: ', psutil.pids())
# print('获取指定进程ID=3776，其实就是当前Python交互环境: ', psutil.Process(3776))
# print('获取指定进程ID=3776，进程名称: ', psutil.Process(3776).name())
# print('获取指定进程ID=3776，进程exe路径: ', psutil.Process(3776).exe())
# print('获取指定进程ID=3776，进程工作目录: ', psutil.Process(3776).cwd())
# print('获取指定进程ID=3776，进程启动的命令行: ', psutil.Process(3776).cmdline())
# print('获取指定进程ID=3776，父进程ID: ', psutil.Process(3776).ppid())
# print('获取指定进程ID=3776，父进程: ', psutil.Process(3776).parent())
# print('获取指定进程ID=3776，子进程列表: ', psutil.Process(3776).children())
# print('获取指定进程ID=3776，进程状态: ', psutil.Process(3776).status())
# print('获取指定进程ID=3776，进程用户名: ', psutil.Process(3776).username())
# print('获取指定进程ID=3776，进程创建时间: ', psutil.Process(3776).create_time())
# print('获取指定进程ID=3776，进程终端: ', psutil.Process(3776).terminal())
# print('获取指定进程ID=3776，进程使用CPU的时间: ', psutil.Process(3776).cpu_time())
# print('获取指定进程ID=3776，进程使用的内存: ', psutil.Process(3776).memory_info())
# print('获取指定进程ID=3776，进程打开的文件: ', psutil.Process(3776).open_files())
# print('获取指定进程ID=3776，进程相关网络连接: ', psutil.Process(3776).connections())
# print('获取指定进程ID=3776，进程的线程数量: ', psutil.Process(3776).num_thread())
# print('获取指定进程ID=3776，所有线程信息: ', psutil.Process(3776).threads())
# print('获取指定进程ID=3776，进程环境变量: ', psutil.Process(3776).environ())
# print('获取指定进程ID=3776，结束进程: ', psutil.Process(3776).terminate())


# Python的test()函数可以模拟ps命令的效果
# print(psutil.test())




















