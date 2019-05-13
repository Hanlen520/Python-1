#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: __init__.py
# author: jiangheng

# description: 程序配置到腾讯云教程：https://www.linuxidc.com/Linux/2016-07/133064.htm

# description:

# questions:

# 导入应用程序实例
# https://segmentfault.com/q/1010000004418410
from app import app
from app import db

# 通过添加数据库实例和模型来创建一个shell上下文环境
from app.models import User, Post



def start_microblog(port):
    app.run(port=port, debug=False)
    db.run()



# 通过添加数据库实例和模型来创建一个shell上下文环境
from app.models import User, Post



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == "__main__":

    start_microblog(5000)


    start_microblog(5000)
