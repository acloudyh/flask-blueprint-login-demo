# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : __init__.py.py
# Software: PyCharm
# Time    : 2020/3/18 16:58
# Description: __init__.py就是构建app的一个函数，并且将views中的蓝图注册

from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

# 注意：实例化SQLAlchemy的代码必须要在引入蓝图之前
db = SQLAlchemy()
app = Flask(__name__)

login_manager = LoginManager()
app.secret_key = 'abc'  # 设置表单交互密钥
login_manager.init_app(app)  # 初始化应用
login_manager.session_protection = 'strong'

# 引入蓝图
from app.auth.controller import auth

app.config.from_object(DevConfig)
db.init_app(app)  # 初始化SQLAlchemy , 本质就是将以上的配置读取出来

app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def index():
    return redirect(url_for('auth.login'))
