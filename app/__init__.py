# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : __init__.py.py
# Software: PyCharm
# Time    : 2020/3/18 16:58
# Description: __init__.py就是构建app的一个函数，并且将views中的蓝图注册

from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig, configs

# 注意：实例化SQLAlchemy的代码必须要在引入蓝图之前
from log import init_log

db = SQLAlchemy()
app = Flask(__name__)

# 初始化配置
app.config.from_object(DevConfig)

# 初始化 DB
db.init_app(app)  # 初始化SQLAlchemy , 本质就是将以上的配置读取出来

# 初始化配置文件 默认DevConfig
config = configs['dev']
app.config.from_object(config)

# 初始化日志
init_log(app)

app.secret_key = 'abc'  # 设置表单交互密钥
login_manager = LoginManager()
login_manager.init_app(app)  # 初始化应用
# 未登录时,遇见@login_required,Flask-Login 会拦截请求，把用户发往登录页面 自动跳转登录页的视图
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'
login_manager.login_message = '请先登录'
# 引入蓝图

from app.controller.auth_controller import auth
from app.controller.company_controller import company

# 注册蓝图
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(company, url_prefix='/company')


@app.route('/')
def index():
    return redirect(url_for('auth.login'))
