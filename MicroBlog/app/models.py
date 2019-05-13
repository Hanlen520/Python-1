#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: models.py
# author: jiangheng
# description:
# questions:

from datetime import datetime

from flask_wtf import FlaskForm
from pip._vendor.appdirs import unicode
from werkzeug.security import generate_password_hash, check_password_hash
# from wtforms import PasswordField
# from wtforms.validators import DataRequired, EqualTo

from app import db
from flask_login import UserMixin
from hashlib import md5
from time import time
import jwt
from app import app


# 实现粉丝机制
# 除了外键没有其他数据的辅助表，所以我创建它的时候没有关联到模型类
followers = db.Table(
        'followers',
        db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
    )


# User类继承自db.Model，它是Flask-SQLAlchemy中所有模型的基类
# SQLAlchemy包做了一层封装以便在Flask中调用更方便，类似SQLAlchemy这样的包叫做Object Relational Mapper（ORM）
# ORM允许应用程序使用高级实体（类，对象和方法）而不是表和SQL来管理数据库
# ORM的工作就是将高级操作转换成数据库命令
# 这个类将表字段定义为类属性，字段被创建为db.Column类的实例，它传入字段类型以及其他可选参数
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # 使用hash密码, 可以大大提高安全性
    password_hash = db.Column(db.String(128))
    # db.relationship的第一个参数表示代表关系“多”的类。 backref参数定义了代表“多”的类的实例反向调用“一”的时候的属性名称。
    # 这将会为用户动态添加一个属性post.author，调用它将返回给该用户动态的用户实例。
    posts = db.relationship('Post', backref='author', lazy='dynamic')


    # 该类的__repr__方法用于调试时实时打印用户实例
    def __repr__(self):
        return '<User {}'.format(self.username)

    # 扩展两个字段about_me、last_seen两个字段分别用来展示用户的个人信息和最近一次登陆的时间
    # 新增加了两个字段那么就得重新生成数据库的迁移文件
    # 重新生成迁移不会覆盖掉之前的数据，迁移步骤为：
    #   FLASK_APP
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # 密码哈希逻辑可以在用户模型中实现为两个新的方法
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)


    @staticmethod
    def is_active():
        return True

    def get_id(self):
        return unicode(self.id)


    @staticmethod
    def is_authenticated():
        return True


    @staticmethod
    def is_anonymous():
        return False


    # 由于头像与用户相关联，所以将头像URL的逻辑添加到用户模型中
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'http://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    followed = db.relationship(
        # secondary 指定了用于该关系的关联表，就是使用我在上面定义的followers
        'User', secondary=followers,
        # primaryjoin 指明了通过关系表关联到左侧实体（关注者）的条件
        primaryjoin=(followers.c.follower_id == id),
        # secondaryjoin 指明了通过关系表关联到右侧实体（被关注者）的条件
        secondaryjoin=(followers.c.follower_id == id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )


    # 用户模型中添加和删除关注关系代码
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)


    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)


    def is_following(self, user):
        return self.followed.filter(followers.c.follower_id == user.id).count() > 0


    # 查询关注人的动态
    # def followed_posts(self):
    #     return Post.query.join(
    #         followers, (followers.c.followed_id == Post.user_id)).filter(
    #         followers.c.follower_id == self.id).order_by(
    #         Post.timestamp.desc())
    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    # -----------
    # 重置密码
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256'
        ).decode('utf-8')


    # verify_reset_password_token()是一个静态方法，这意味着它可以直接从类中调用。
    # 静态方法与类方法类似，唯一的区别是静态方法不会接收类作为第一个参数
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()


# 数据库关系
# 关系数据库擅长存储书库项之间的关系
# 例如:考虑到用户发表动态情况, 用户将在user表中有一个记录, 并且这条用户动态将在post表中有一个记录
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    # author = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # FLASK-SQLAlchemy自动设置类名为小写来作为对应表的名称
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # 添加监测到的语言到Post模型，只需要监测用户提交
    # language = db.Column(db.String(5))


    def __repr__(self):
        return '<Post {}>'.format(self.body)


# 用户加载函数
# 用户会话是Flask分配给每个连接到应用的用户的存储空间
# Flask-Login通过在用户会话中存储唯一的标识来跟踪登陆用户
# 每当已登录的用户导航到新页面时，Flask-Login将从会话中检索用户的ID，然后将该用户实例加载到内存中。
# 因为数据库对Flask-Login透明，所以需要应用来辅助加载用户
# 基于此，用插件应用配置一个用户加载函数，可以调用该函数来加载给固定ID的用户
from app import login


# 使用Flask-Login的@login.user_loader装饰器来为用户加载功能注册函数
# Flask-Login将字符串类型的参数id传入用户加载函数
@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)







