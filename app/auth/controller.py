# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : controller.py
# Software: PyCharm
# Time    : 2020/3/18 21:07
# Description:

from flask import Blueprint, request, render_template

auth = Blueprint('auth', __name__)

from app import db
from app.models import User


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db.session.add(User(name=username, password=password))
        db.session.commit()
        # 查询
        user_obj = User.query.filter(User.name == username and User.password == password).first()
        if user_obj:
            return f"{user_obj.name}登录成功"
    return render_template("auth/login.html")
