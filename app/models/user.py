# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : user.py
# Software: PyCharm
# Time    : 2020/3/20 10:05
# Description:


# 建立users数据表
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.String(256))
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

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
