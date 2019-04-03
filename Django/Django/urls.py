"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Django的网站是写在urls.py文件中，用正则表达式对应views.py中的一个函数(或generic类)
from django.contrib import admin
from django.urls import path
from Studyblog import views as studyblog_view

urlpatterns = [
    path('', studyblog_view.index, name='home'),


    # 这里的 name='sub' 是用来干什么的呢？
    # name 可以用于在 templates, models, views ……中得到对应的网址，相当于“给网址取了个名字”，只要这个名字不变，网址变了也能通过名字获取到。
    # 用正则表达式改造网站，使其更通用
    path(r'^sub/(\d+)/(\d+)/$', studyblog_view.sub, name='sub'),
    path('add/', studyblog_view.cal, name='add'),
    # path('', studyblog_view.index),
    path('admin/', admin.site.urls),
]
