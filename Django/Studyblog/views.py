# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 自定义函数index中的第一个参数必须是request，与网页发送来的请求有关，request变量里面包含get或post的内容，用户浏览器、系统等信息在里面
# 那问题来了，我们访问什么网址才能看到刚才写的这个函数呢？怎么让网址和函数关联起来呢？
def index(request):
    # print("request: ", request)
    # return HttpResponse(u"女神说好听就是好听😵")

    # 使用render的时候，Django 会自动找到 INSTALLED_APPS 中列出的各个 app 下的 templates 中的文件。
    return render(request, 'home.html')


# 在网页上做加减运算
def cal(request):
    # 用 request.GET.get('a', 0) 当没有传递 a 的时候默认 a 为 0
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return HttpResponse(str(c))


# Django支持优雅的网址
def sub(request, a, b):
    c = int(a) - int(b)
    return HttpResponse(str(c))