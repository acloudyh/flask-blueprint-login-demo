# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : controller.py
# Software: PyCharm
# Time    : 2020/3/18 21:07
# Description:

from flask import Blueprint, render_template, redirect, url_for, g
from flask_login import login_user, current_user, login_required
from werkzeug.security import check_password_hash

from app import login_manager, db
from app.auth.forms import LoginForm, SignupForm

auth = Blueprint('auth', __name__)

from app.models import User


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    emsg = None
    if form.validate():
        username = form.username.data
        password = form.password.data

        user_info = User.query.filter(User.username == username).first()
        if user_info and check_password_hash(user_info.password_hash, password):
            user_info.authenticated = True
            login_user(user_info, remember=True)
            return redirect(url_for("auth.index"))
        else:
            emsg = "用户名或密码密码有误"

    return render_template("auth/login.html", form=form, emsg=emsg)


@auth.route('/signup/', methods=('GET', 'POST'))  # 注册
def signup():
    form = SignupForm()
    emsg = None
    if form.validate():
        username = form.username.data
        password = form.password.data
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))

    return render_template('auth/signup.html', form=form, emsg=emsg)


@auth.route('/')  # 首页
@login_required  # 需要登录才能访问
def index():
    print("hahah")
    return render_template('index.html', username=current_user.username)


@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(username):
    return User.query.get(username)


@auth.before_app_request
def load_user():
    g.user = current_user
