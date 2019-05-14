#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# --------------------------------------
# ProjectName: MySpace
# Author: crisimple
# CreateTime: 2019/5/12 10:57
# FileName: initial_flask.py
# Description: 
# Question:
# --------------------------------------

from flask import Flask, render_template, session, redirect, url_for, flash
from flask import request
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
import config
from flask_migrate import Migrate, MigrateCommand
from flask_mail import Mail, Message
from datetime import datetime
from threading import Thread

# 1. Flask 类的构造函数只有一个必须指定的参数，即程序主模块或包的名字。通常 Python 的 __name__变量就是所需的值
app = Flask(__name__)
# 设置 flask_wtf
app.config['SECRET_KEY'] = 'hard to guess string'
# flask_script 初始化
manager = Manager(app)
# flask_bootstrap 初始化
bootstrap = Bootstrap(app)
# flask_moment 初始化
moment = Moment(app)
# flask_sqlalchemy 初始化


# 2. 路由和视图函数
# 路由：处理 URL 和函数之间关系的程序
@app.route('/user/<name>')
# 视图函数：客户端接受到响应需要处理的函数
def user(name):
    return render_template('user.html', name=name)


# 六、配置 Flask-Mail 使用 163 邮箱
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_USERNAME'] = 'crisimple@163.com'
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_PASSWORD'] = '132Wj7916h3709'
# 电子邮件支持
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[FLASKY MAIL Test]'
app.config['FLASKY_MAIL_SENDER'] = 'crisimple@163.com'
app.config['FLASKY_ADMIN'] = 'crisimple@qq.com'
mail = Mail(app)


# 异步发送电子邮件
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'], sender=app.config['FLASKY_MAIL_SENDER'],
                  recipients=app.config['FLASKY_ADMIN'])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + 'html', **kwargs)
    # mail.send(msg)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_mail(app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('恭喜你提交成功了！！！！！')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False), current_time=datetime.utcnow())


# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(FlaskForm):
    name = StringField("请少侠报上你的大名：", validators=[DataRequired()])
    submit = SubmitField()


# 五、配置数据库
basedir = os.path.abspath(os.path.dirname(__file__) + '/')
print(basedir)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + 'flask_data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config.from_object(config)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


# 用 Flask_Script 的 shell 命令自动导入数据库实例和模型
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context()))

# 5.11、数据库迁移
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 3. 启动服务器
if __name__ == '__main__':
    # run 方法启动 Flask 集成的开 Web 服务器
    # app.run(debug=True)
    manager.run()
