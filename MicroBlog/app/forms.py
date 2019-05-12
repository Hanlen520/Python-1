#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: form.py
# author: jiangheng
# description:
# questions:


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


# 用户登陆表单
class LoginForm(FlaskForm):
    # 由于Flask-WTF插件本身不提供字段类型
    # 从WTForms包中导入了四个表示表单字段的类
    # 每个字段类都接受一个描述或别名作为第一个参数
    # 并生成一个实例来作为LoginForm的类属性
    # 可选参数validators用于验证输入字段是否符合预期，DataRequired验证器仅验证字段输入是否为空
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


# 用户注册
class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


    # @staticmethod
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')


    # @staticmethod
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


# ---------------------------------------------------------------------------
# 个人资料编辑器
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')


    # 修改用户名重复的BUG
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username


    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('你编辑输入的名字已被使用，请重新输入.')


# ---------------------发布用户动态类----------------------
class PostForm(FlaskForm):
    post = TextAreaField('你可以记录下你的最新动态：', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')


# ---------------------请求重置密码的表单类------------------
class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


# -------重置密码的表单类
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')