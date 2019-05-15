#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/14 22:53
# FileName: email.py
# Description: 
# Question:
# --------------------------------------
from threading import Thread
from flask import current_app, render_template
from flask_mail import Message

from flasky import app
from . import mail
# from .. import app


# 异步发送电子邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(template, **kwargs):
    msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'], sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=current_app.config['FLASKY_ADMIN'])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + 'html', **kwargs)
    # mail.send(msg)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr