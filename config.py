# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : config.py
# Software: PyCharm
# Time    : 2020/3/18 16:59
# Description:


class Config(object):
    pass


# 初始化app配置，专门针对SQLAlchemy 进行配置
class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./sqlite3flask.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_QUERY_TIME = 0.0001
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = True
    JSON_AS_ASCII = False
