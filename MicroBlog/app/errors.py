#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: errors.py
# author: jiangheng
# description: 自定义错误页面（不然每次服务器报错Internal Server Error，很不友好）
# questions:

from flask import render_template
from app import app, db


# 错误函数与视图函数非常类似
# 使用@errorhandler装饰器来声明一个自定义的错误处理器
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    # 为了确保任何失败的数据库会话不会干扰模板触发的其他数据库访问
    # 执行会话回滚来将会话重置为干净的状态
    db.session.rollback()
    return render_template('500.html'), 500


# ---------------------------服务报错发送电子邮件报错配置-----------------------------
# 为Flask的日志对象app.logger添加一个SMTPHandler的实例
import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os


if not app.debug:

    # ---------------------------服务错误发送邮件配置-----------------------------
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_LLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'],
            subject='Microblog Failure',
            credentials=auth,
            secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


        # ---------------------------记录日志到文件中-----------------------------
        # 基于文件类型RotatingFileHandler的日志记录器
        # 日志文件的存储路径位于顶级目录下，相对路径为logs/microblog.log，如果其不存在，则会创建它
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')
