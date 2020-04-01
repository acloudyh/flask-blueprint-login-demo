# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : user_model.py
# Software: PyCharm
# Time    : 2020/3/20 10:05
# Description:


# 建立users数据表
import hashlib

from flask_login import UserMixin

from app import db

salt = 'python-flask'


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32))
    password = db.Column(db.String(256))
    authenticated = db.Column(db.Boolean, default=False)

    @property
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        return self.id

    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_password(self, password):
        self.password = password

    def to_json(self):
        """
        转换json(数据库查询出的对象转换成字典相对应的json)
        :return:
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def init_md5_password(password):
    """
    加盐 acloudchina MD5加密
    :param password:
    """
    md5 = hashlib.md5()
    md5.update((password + salt).encode('utf8'))
    return md5.hexdigest()


def check_password(password, login_password):
    """
    检查密码
    :param password:
    :param login_password:
    :return:
    """
    md5 = hashlib.md5()
    md5.update((login_password + salt).encode('utf8'))
    md5.hexdigest()
    return password == md5.hexdigest()
