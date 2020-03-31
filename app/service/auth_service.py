# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : auth_service.py
# Software: PyCharm
# Time    : 2020/3/30 10:19
# Description: 权限相关service
# 密码初始化
from flask import current_app, session, json

from app import db
from app.models.user import User, init_md5_password, check_password

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
    try:
        username = session['username']
        original_password = form.original_password.data
        new_password = form.new_password.data
        user_info = User.query.filter(username == username).first()
        if user_info and check_password(user_info.password, original_password):
            # 设置新密码
            user_info.set_password(init_md5_password(new_password))
            user_info.authenticated = False
            db.session.add(user_info)
            db.session.commit()

            current_app.logger.info("修改密码成功:[%s],请重新登录!", username)
            session.pop('username', None)
    except Exception as e:
        db.session.rollback()
        raise e


def register(form):
    current_app.logger.info("需要注册内容%s",
                            json.dumps(form.data, ensure_ascii=False, indent=4, separators=(',', ':')))
    username = form.username.data
    # 查询用户是否已存在

    strPassword = init_md5_password(form.password.data)
    user = User(username, strPassword)
    db.session.add(user)
    db.session.commit()
