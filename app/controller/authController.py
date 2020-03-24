# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : authController.py
# Software: PyCharm
# Time    : 2020/3/18 21:07
# Description:
import json

from flask import Blueprint, render_template, redirect, url_for, current_app, request, session, flash
from flask_login import login_user, current_user, login_required, logout_user

from app import login_manager, db
from app.controller.form.authForms import LoginForm, SignupForm, EditPasswordForm
from app.models.user import User, check_password, set_password
from app.service.companyService import getAllCompany

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    emsg = None
    if form.validate_on_submit():
        login_username = form.username.data
        login_password = form.password.data
        user_info = User.query.filter(User.username == login_username).first()

        if user_info and check_password(user_info.password, login_password):
            user_info.authenticated = True
            db.session.add(user_info)
            db.session.commit()
            login_user(user_info, remember=True)
            session['username'] = form.username.data

            current_app.logger.info("用户[%s]登录成功", login_username)
            # 登录成功之后展示首页的数据
            companys = getAllCompany()
            return render_template("company/index.html", companys=companys)
        else:
            current_app.logger.error("用户名或密码错误:[%s]:[%s] ", login_username, login_password)
            flash("用户名或密码密码有误")
    return render_template("auth/login.html", form=form, emsg=emsg)


@auth.route('/signup/', methods=('GET', 'POST'))  #
def signup():
    """
    注册用户
    :return:
    """
    if request.method == 'GET':
        form = SignupForm()
        return render_template('auth/signup.html', form=form)
    else:
        form = SignupForm(request.form)
        if form.validate():
            current_app.logger.info("注册内容%s",
                                    json.dumps(form.data, ensure_ascii=False, indent=4, separators=(',', ':')))
            username = form.username.data
            strPassword = set_password(form.password.data)
            user = User(username, strPassword)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        return render_template('auth/signup.html', form=form)


@auth.route('/logout', methods=('GET', 'POST'))
@login_required
def logout():
    """
    注销登录,解除会话 logout_user()
    :return:
    """
    print(current_user)
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for("auth.login"))


@auth.route('/edit_password', methods=('GET', 'POST'))
@login_required
def edit_password():
    """
    修改密码,重新登录
    :return:
    """

    if request.method == 'GET':
        form = EditPasswordForm()
        return render_template('auth/edit_password.html', form=form)
    else:
        form = EditPasswordForm(request.form)
        if form.validate():
            username = session['username']
            original_password = form.original_password.data
            user_info = User.query.filter(User.username == username).first()
            if user_info and check_password(user_info.password, original_password):
                # 设置新密码
                strPassword = set_password(form.new_password.data)
                user_info.password = strPassword
                user_info.authenticated = False
                db.session.add(user_info)
                db.session.commit()

                current_app.logger.info("修改密码成功:[%s],请重新登录!", username)
                session.pop('username', None)
                # 退出登录,让其重新登录
            return redirect(url_for("auth.login"))
        return render_template('auth/edit_password.html', form=form)


@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(username):
    return User.query.get(username)
