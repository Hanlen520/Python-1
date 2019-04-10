#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/4/10 17:36
# FileName: txt2db.py
# Description: 
# Question: 
# --------------------------------


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

# 否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
import django
django.setup()

if django.VERSION >= (1, 7):
    django.setup()

# Blog.objects.create()每保存一条就执行一次SQL
def objects_create():
    from studyblog.models import Blog
    f = open('Blog_data.txt')
    for line in f:
        name, tagline = line.split('*****')
        Blog.objects.get_or_create(name=name, tagline=tagline)
    f.close()

# bulk_create()是执行一条SQL存入多条数据，做会快很多！
def bulk_create():
    from studyblog.models import Blog
    f = open('Blog_data.txt')
    BlogList = []
    for line in f:
        params = line.split('*****')
        blog = Blog(name=params[0], tagline=params[1])
        BlogList.append(blog)
    f.close()

    Blog.objects.bulk_create(BlogList)

if __name__ == "__main__":
    objects_create()
    print('ToLead Done!')


