#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: __init__.py
# author: jiangheng
# description:
# questions:

from flask import Flask
# 导入全局的配置文件
from config import Config
from flask_login import LoginManager
# 也不知道干什么用的
# from flask_login import UserMixin
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from flask import request


# ------
# 需要在Flask应用创建之后创建一个邮件实例
from flask_mail import Mail
app = Flask(__name__)

# -----初始化邮件模块
mail = Mail(app)

# -------初始化Flask-Bootstrap
bootstrap = Bootstrap(app)


# Flask-Moment插件中的moment.js是一个小型的JavaScript开源库
# 它将日期和时间可以转换成目前可以想象到的所有格式
moment = Moment(app)


# Flask-Babel初始化
babel = Babel(app)


# Babel实例提供一个 localeselector 装饰器，为每个请求调用装饰器函数已选择用于该请求的语言
# @babel.localeselector
# def get_locale():
#     # request对象提供了一个高级接口，用于处理客户端发送的带Accept-Language头部的请求
#
#     return request.accept_languages.best_match(app.config['LANGUAGES'])



# 调用它的模块的名字
# 把Flask对象生成并赋给变量app
# app = Flask(__name__)----------Flask的实例化一个服务里面一次就够了
# 一种加密方式，免受Cross-Site Request Forgery(CSRF)的恶意攻击
app.config.from_object(Config)
# app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
# ------------------------Flask-Login---------------------------
# Flask-Login必须的四项
#   ·is_authenticated: 一个用来表示用户是否通过登陆认证的属性，用True和False
#   ·is_active: 如果用户账户是活跃的，那么这个属性是True，否则就是False（活跃用户的定义是该用户登陆状态
#               是否通过用户名密码登陆，通过记住我功能保持登陆状态的用户是非常活跃的）
#   · is_anonymous: 常规用户的该属性是False，对特定的匿名用户是True
#   · get_id(): 返回用户的唯一id的方法，返回值类型是字符串(python2下返回Unicode字符串）
login = LoginManager(app)



# 数据库在应用的表现形式是一个数据库实例，数据库迁移引擎同样如此
# 它们将会在应用实例化之后进行实例化和注册操作
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




# Flask-Login提供了强制在查看某些页面时必须登陆的功能
login = LoginManager(app)
# 上面的'login'值是登录视图函数（endpoint）名，换句话说该名称可用于url_for()函数的参数并返回对应的URL
login.login_view = 'login'


# from app import models



# 接下来就是生成数据库迁移了, Alembic可以使用自动和手动来创建数据库迁移
# 由于是第一次: flask db migrate -m "users table"子命令生成这些自动迁移
# flask db migrate命令不会对数据库进行任何更改，只会生成迁移脚本。
# 要将更改应用到数据库, 必须使用flask db upgrade命令

# db对象来表示数据库----实例化
db = SQLAlchemy(app)
# 添加数据库迁移引擎migrate
migrate = Migrate(app, db)


# 不写上这句话的话会报错：
#       if not force and not user.is_active:
#       AttributeError: 'User' object has no attribute 'is_active'
# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)


# --------------------不要移动这个的顺序--------------------------
# models用来定义数据库模型
# 特别注意:先要生成迁移文件才能导入
# 创建数据库迁移存储库: 先配置入口环境变量FLASK_APP=microblog.py, 再通过flask db init来创建microblog的迁移存储库
from app import routes, models


# -------------------error错误处理程序注册--------------------------
# 为了让error错误处理程序在Flask中注册，需要在应用实例创建后导入新的app/errors.py模块
from app import errors















