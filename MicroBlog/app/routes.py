#!/bin/usr/env python3
# -*- coding: utf-8 -*-
# filename: routes.py
# author: jiangheng
# description:
# questions:
#   1. 关于from app import app的解释：
#       an: https://segmentfault.com/q/1010000004418410

from app import app
# from flask import render_template   # 渲染模板的方法
from app.forms import LoginForm
# from flask import url_for
from flask_login import login_required
from app.forms import PostForm
from app.models import Post
# from guess_language import guess_language
import os
from flask import send_from_directory


# # ----------
# # ------------------添加icon
#
#
# @app.route('/favicon.ico')
# def favicon():
#
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#
#                                'default.ico', mimetype='image/vnd.microsoft.icon')


# 装饰器的常见模式是使用它们将函数注册为某些事件的回调函数
# 该例子中有两个装饰器，他们将URL / 和 /index索引关联到这个函数
# 这意味着当Web浏览器请求这两个URL中的任何一个时，Flask将调用该函数并将其返回值作为响应传递回浏览器
# 关联到index视图函数的两个路由都新增接受POST请求，以便视图函数处理接收的表单数据
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    # ---------------------用户发表动态消息的路由---------------------
    form = PostForm()
    if form.validate_on_submit():
        # # 用户提交文字语言的判断字段
        # language = guess_language(form.post.data)
        # if language == "UNKNOWN" or len(language) > 5:
        #     language = ''

        # 处理表单的逻辑会为post表插入一条新的数据
        post = Post(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('你的动态消息将会被动态展现!')
        return redirect(url_for('index'))

    # posts = [
    #     {
    #         'author': {'username': 'John'},
    #         'body': '世界很大，我想去看看。。。。。。!'
    #     },
    #     {
    #         'author': {'username': 'Susan'},
    #         'body': '最近上映的碟中谍6还是真的不错的...!'
    #     }
    # ]

    # for post in posts:
    #     return post


    # 上面的Post是模拟用户的登录状态的，下面可以真实的展示用户的登录状态
    # 因为我们已经在models.User类中有followed_posts()方法
    # 它可以返回固定用户希望看到的用户动态的查询结果集
    # posts = current_user.followed_posts().all()
    # return render_template('index.html', title='Home Page', form=form,
    #                        posts=posts)


    # 将用户动态分页处理，解决单页显示太多的问题
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, app.config['POSTS_PER_PAGE'], False)

    # 下一页
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None

    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('index.html', title='Home Page', form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)
    # posts = current_user.followed_posts().all()
    # return render_template('index.html', titile='Home Page', form=form,
    #                        posts=posts)


# 接受表单数据，在表单试图中点击submit会报错Method Not Allowed，因为并没有写它的登陆方法
from flask import render_template, flash, redirect, url_for
from app.models import User
from flask_login import current_user, login_user
from flask import request
from werkzeug.urls import url_parse


# 用户登陆
@app.route('/login', methods=['GET', 'POST'])
def login():
    # 异常处理，如果用户已经登陆那么就直接跳转到首页导引页
    # is_authenticated函数可以方便检查出用户是否处于登陆状态
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    # form.validate_on_submit()实例方法会执行form校验的工作
    if form.validate_on_submit():
        # 下面是用户真正的登陆流程
        #   ·第一步：从数据库加载用户
        # filter_by()的结果是一个只包含具有匹配用户名的对象的查询结果集。
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        # 原始URL设置了next查询字符串参数后，应用就可以在登录后使用它来重定向。
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

        # 调用flash()函数后，Flask会存储这个消息，但是却不会奇迹般地直接出现在页面上
        # 模板需要将消息渲染到基础模板中，才能让所有派生出来的模板显示出来
        # flash()显示消息模拟登陆
        # flash('Login requested for user {}, remember_me={}'.format(
        #     form.username.data, form.remember_me.data
        # ))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# 用户登出
from flask_login import logout_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# 用户注册
from app.forms import RegistrationForm
from app import db


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        # user.check_password(form)
        db.session.add(user)
        db.session.commit()
        flash('恭喜你注册成功，你可以关注其他人的动态了！')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# 用户主页
# 个人主页URL /user/ 新建一个对应的视图函数
# 被<和>包裹的URL <username>是动态的
@app.route('/user/<username>')
@login_required
def user(username):
    # 当有结果时它的工作方式与first()完全相同，但是在没有结果的情况下会自动发送404 error给客户端
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.posts.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    flash("欢迎来到你的个人空间，看看都有些什么吧！")
    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


# ---------------------------------------------------------------------------
# 查看用户最近一次登陆的时间
from datetime import datetime


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


# -----------------------------------------------------------------------------
# 使用视图函数将from类函数与Edit Profile表单结合起来
from app.forms import EditProfileForm


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    # 如果validate_on_submit()返回为True，将表单中的数据复制到用户对象中，然后将对象写入到数据库中
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your have changed your profile and Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    # 若validate_on_submit()返回为False:
    #   可能是因为浏览器刚刚发送了一个GET请求，我们需要通过提供表单模板的初始版本来响应
    #   也可能是因为浏览器发送带有表单数据的POST请求，但该数据中的某些内容无效
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)


# -------------------------------------------------------------------------
# ---------------------用戶关注和取消关注---------------------
@app.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash('You are following {}!'.format(username))
    return redirect(url_for('user', username=username))


@app.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User {} not found.'.format(username))
        return redirect(url_for('index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash('You are not following {}.'.format(username))
    return redirect(url_for('user', username=username))


# ------------看目前该应用上有哪些用户存在，我们好去关注他们-----------------
# ---------------------用户发表动态消息的路由---------------------
@app.route('/explore')
@login_required
def explore():
    # 解决单页显示太多用户动态
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False
    )

    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None

    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template('index.html', title='Explore', posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

    # posts = Post.query.order_by(Post.timestamp.desc()).all()
    # # render_template()引用了我在应用的主页面中使用的index.html模板。
    # # 这个页面与主页非常相似，所以我决定重用这个模板
    # # 但与主页不同的是，在发现页面不需要一个发表用户动态表单
    # # 所以在这个视图函数中，我没有在模板调用中包含form参数。
    # # posts = Post.query.order_by(Post.timestamp.desc()).paginate(
    # #     page, app.config['POSTS_PER_PAGE'], False)
    # return render_template('index.html', title='Explore', posts=posts)


# ----------------视图来处理忘记密码的表单-------------------------
from app.forms import ResetPasswordRequestForm
from app.email import send_email
from app import app


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('请勿回复此邮件，点击链接重置您的密码')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='重置密码', form=form)



def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'][0],
               recipients=['1240281595@qq.com'],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token)
               )


# --------
# --------------重置用户密码----------
from app.forms import ResetPasswordForm


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


# -----------------
# -------------用户示图弹窗
@app.route('/user/<username>/popup')
@login_required
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_popup.html', user=user)






