# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : views.py
# Software: PyCharm
# Time    : 2020/3/18 21:07
# Description:

from flask import Blueprint, request, render_template

user_bp = Blueprint('users', __name__, template_folder='templates')

from app import db
from app.models import User


@user_bp.route("/login", methods=['GET', 'POST'])
def user_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        db.session.add(User(name=username, password=password))
        db.session.commit()
        # 查询
        user_obj = User.query.filter(User.name == username and User.password == password).first()
        if user_obj:
            return f"{user_obj.name}登录成功"
    return render_template("login.html")
