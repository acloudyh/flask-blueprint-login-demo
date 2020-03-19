# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : __init__.py.py
# Software: PyCharm
# Time    : 2020/3/18 16:58
# Description: __init__.py就是构建app的一个函数，并且将views中的蓝图注册

from flask import Flask, redirect, url_for
from flask_login import login_required
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

# 注意：实例化SQLAlchemy的代码必须要在引入蓝图之前
db = SQLAlchemy()

# 引入蓝图
from app.users.acc import acc_bp
from app.users.views import user_bp
from app.auth.controller import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.config['JSON_AS_ASCII'] = False  # 这个配置可以确保http请求返回的json数据中正常显示中文
    app.config["DEBUG"] = True
    db.init_app(app)  # 初始化SQLAlchemy , 本质就是将以上的配置读取出来

    app.register_blueprint(auth, url_prefix='/auth')
    return app


app = create_app()


@app.route('/')
def index():
    return redirect(url_for('auth.login'))
