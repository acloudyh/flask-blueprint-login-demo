# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : config.py
# Software: PyCharm
# Time    : 2020/3/18 16:59
# Description:


import os


def getDevConfigLogPath():
    """
    开发环境配置文件获取日志路径
    """
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    if not os.path.exists(log_path):  # 创建日志目录
        os.makedirs(log_path)
    return log_path


class BaseConfig(object):
    """
    基础配置文件,配置不同环境参数在 DevConfig,ProdConfig 中覆盖配置即可
    """
    LOG_NAME = 'deb-web-server.log'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite3flask.db'


# 初始化app配置，专门针对SQLAlchemy 进行配置
class DevConfig(BaseConfig):
    """
    开发环境配置文件
    """
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////Users/neo/code/sqlite3flask.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_QUERY_TIME = 0.0001
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 上传文件最大限制20M
    LOG_PATH = getDevConfigLogPath()
    LOG_NAME = 'deb-web-server.log'


class ProdConfig(BaseConfig):
    """
    生产环境配置文件
    """
    pass


configs = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'default': DevConfig
}
