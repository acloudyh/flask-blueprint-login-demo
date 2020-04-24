# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : auth_controller.py
# Software: PyCharm
# Time    : 2020/3/18 21:07
# Description:
import os
import sys
from datetime import timedelta

from flask import Blueprint, render_template, redirect, url_for, current_app, request, session, flash
from flask_login import login_user, current_user, login_required, logout_user
from werkzeug.utils import secure_filename

from app import login_manager, app, db
from app.common.exception_common import ExceptionCommon
from app.controller.form.authForms import LoginForm, EditPasswordForm, SignupForm
from app.models.user_model import User, check_password
from app.service import auth_service, company_service

auth = Blueprint('auth', __name__)
# 上传文件路径
UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'txt'}


@login_manager.user_loader  # 定义获取登录用户的方法
def load_user(username):
    return User.query.get(username)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login_username = form.username.data
        login_password = form.password.data
        user_info = auth_service.get_user_info(login_username)

        if user_info and check_password(user_info.password, login_password):
            user_info.authenticated = True
            auth_service.save_user(user_info)
            login_user(user_info, remember=True)
            session['username'] = form.username.data

            session.permanent = True
            app.permanent_session_lifetime = timedelta(minutes=30)
            current_app.logger.info("用户[%s]登录成功", login_username)
            return redirect(url_for('company.companys'))
        else:
            current_app.logger.error("用户名或密码错误:[%s]:[%s] ", login_username, login_password)
            flash("用户名或密码密码有误")
    return render_template("auth/login.html", form=form)


@auth.route("/without/login", methods=['GET', 'POST'])
def without_login():
    companys = company_service.get_all_company()
    return render_template("company/index.html", companys=companys)


@auth.route('/logout', methods=('GET', 'POST'))
@login_required
def logout():
    """
    注销登录,解除会话 logout_user()
    :return:
    """
    current_app.logger.error("目前登录用户[%s]", current_user.to_json())
    user = current_user
    user.authenticated = False
    auth_service.save_user(user)
    logout_user()
    session.pop('username', None)
    return redirect(url_for("auth.login"))


@auth.route('/signup', methods=('GET', 'POST'))
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
            auth_service.register(form)
            return redirect(url_for("auth.login"))
        return render_template('auth/signup.html', form=form)


@auth.route('/edit_password', methods=('GET', 'POST'))
@login_required
def edit_password():
    """
    修改密码,重新登录
    :return:
    """
    form = EditPasswordForm(request.form)
    if request.method == 'GET':
        return render_template('auth/edit_password.html', form=form)
    else:
        if form.validate_on_submit():
            username = session['username']
            auth_service.update_password(form, username)
            return redirect(url_for("auth.login"))
        return render_template('auth/edit_password.html', form=form)


@auth.route('/upload_file', methods=['GET', 'POST'])
@login_required
def upload_file():
    """
    文件上传
    :return:
    """
    if request.method == 'GET':
        return render_template('auth/upload_file.html', )
    else:

        if 'file' in request.files:
            f = request.files['file']
            # basepath = os.path.dirname(__file__)  # 当前文件所在路径
            basepath = sys.path[0]  # 项目的根目录 manage.py目录

            if not allowed_file(f.filename):
                raise ExceptionCommon('后缀名不符合哦')
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            upload_path = os.path.join(basepath, UPLOAD_FOLDER, secure_filename(f.filename))
            f.save(upload_path)
            current_app.logger.info("上传文件成功:[%s] ", upload_path)
            return redirect(url_for("auth.upload_file"))
    return render_template('auth/upload_file.html')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@auth.route('/reset', methods=['GET', 'POST'])
@login_required
def reset():
    """
    初始化
    :return:
    """
    # 执行sql脚本,数据清空
    db.drop_all()
    db.create_all(app=app)
    user = User(username='admin', password='admin')
    db.session.add(user)
    db.session.commit()
    # username = session['username']
    # auth_service.reset_password(username)
    return redirect(url_for("auth.login"))
