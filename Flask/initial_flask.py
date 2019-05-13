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
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os
import config

from datetime import datetime

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


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('你已经改变了你的信息！')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),current_time=datetime.utcnow())


# 自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField()


# 七、配置数据库
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir + 'flask_data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config.from_object(config)
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username



# 3. 启动服务器
if __name__ == '__main__':
    # run 方法启动 Flask 集成的开 Web 服务器
    # app.run(debug=True)
    manager.run()
