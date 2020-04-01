# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : auth_service.py
# Software: PyCharm
# Time    : 2020/3/30 10:19
# Description: 权限相关service
from flask import current_app, session, json

from app import db
# 密码初始化
from app.common.exception_common import ExceptionCommon
from app.models.user_model import User, init_md5_password, check_password

init_password = 'admin'


def reset_password(username):
    user = User.query.filter(username == username).first()
    if user is not None:
        password = init_md5_password(init_password)
        user.set_password(password)
        user.authenticated = False
        db.session.add(user)
        db.session.commit()
        current_app.logger.info("重置密码成功:[%s],请重新登录!", username)
        session.pop('username', None)


def update_password(form):
    username = session['username']
    original_password = form.original_password.data
    new_password = form.new_password.data
    user_info = User.query.filter(username == username).first()
    if user_info is None:
        current_app.logger.error("用户不存在:[%s]", username)
        raise ExceptionCommon("用户不存在")
    else:
        if check_password(user_info.password, original_password):
            user_info.set_password(init_md5_password(new_password))
            user_info.authenticated = False
            db.session.add(user_info)
            db.session.commit()
            current_app.logger.info("修改密码成功:[%s],请重新登录!", username)
            session.pop('username', None)


def register(form):
    current_app.logger.info("需要注册内容%s",
                            json.dumps(form.data, ensure_ascii=False, indent=4, separators=(',', ':')))
    username = form.username.data
    # 查询用户是否已存在
    user_info = User.query.filter(username == username).first()
    if user_info:
        current_app.logger.error("用户名已存在:[%s],请重新输入", username)
        raise ExceptionCommon("用户名已存在")
    else:
        strPassword = init_md5_password(form.password.data)
        user = User(username, strPassword)
        db.session.add(user)
        db.session.commit()
