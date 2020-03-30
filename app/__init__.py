# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : __init__.py.py
# Software: PyCharm
# Time    : 2020/3/18 16:58
# Description: __init__.py就是构建app的一个函数，并且将views中的蓝图注册
import logging
import os
from logging.handlers import RotatingFileHandler

from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import DevConfig

# 注意：实例化SQLAlchemy的代码必须要在引入蓝图之前
db = SQLAlchemy()
app = Flask(__name__)

app.config.from_object(DevConfig)
db.init_app(app)  # 初始化SQLAlchemy , 本质就是将以上的配置读取出来

app.secret_key = 'abc'  # 设置表单交互密钥
login_manager = LoginManager()
login_manager.init_app(app)  # 初始化应用
login_manager.session_protection = 'strong'

# 引入蓝图
from app.controller.auth_controller import auth
from app.controller.company_controller import company

# 注册蓝图
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(company, url_prefix='/company')

log_name = 'web-server.log'
log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
if not os.path.exists(log_path):  # 创建日志目录
    os.makedirs(log_path)

# backupCount 备份日志个数; maxBytes 单个文件大小
file_handler = RotatingFileHandler(os.path.join(log_path, log_name), maxBytes=10 * 1024 * 1024,
                                   backupCount=10, encoding='UTF-8')
logging_format = logging.Formatter("%(asctime)s - [%(filename)s:%(funcName)s:%(lineno)d] - [%("
                                   "levelname)s] : %(message)s")
file_handler.setFormatter(logging_format)
app.logger.addHandler(file_handler)


@app.route('/')
def index():
    return redirect(url_for('auth.login'))
