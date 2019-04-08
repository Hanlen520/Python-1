# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 自定义函数index中的第一个参数必须是request，与网页发送来的请求有关，request变量里面包含get或post的内容，用户浏览器、系统等信息在里面
# 那问题来了，我们访问什么网址才能看到刚才写的这个函数呢？怎么让网址和函数关联起来呢？
def index(request):
    print("request: ", request)
    return HttpResponse(u"女神说好听就是好听😵")

def home(request):
    # 使用render的时候，Django 会自动找到 INSTALLED_APPS 中列出的各个 app 下的 templates 中的文件。
    # 在APP：Studyblog的templates目录下在新建Studyblog目录的目的是，避免Django在一个Project下查找home.html时会找到其他APP下的同名文件从而找错；
    # 因此在每个APP的templates下建立与APP同名的目录可以有效解决因同名文件引起的错误

    # 显示字符串
    # string = '我是一个string，我要显示在页面上'
    # return render(request, 'studyblog/home.html', {'string': string})

    # 这是一个坑，urls对应方法的渲染只能一次渲染一个
    # 显示列表数据
    # TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    # return render(request, 'studyblog/home.html', {'TutorialList': TutorialList})

    # 显示字典数据
    # info_dict = {'host': u'127.0.0.1', 'port': u'8080'}
    # return render(request, 'studyblog/home.html', {"info_dic": info_dict})

    # 4.模板进行 条件判断和 for 循环的详细操作
    # List = map(str, range(100))     # 一个长度为100的list
    # return render(request, 'studyblog/home.html', {'List': List})

    # 5.模板上得到视图对应的网址-----sub

    # 7.获取当前用户
    return render(request, 'studyblog/home.html')


# 计算器部分
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