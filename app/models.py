# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : models.py
# Software: PyCharm
# Time    : 2020/3/18 17:50
# Description:
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)


# 建立users数据表
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


if __name__ == '__main__':
    from app import create_app

    app = create_app()
    # 离线脚本:
    with app.app_context():
        db.drop_all()  # 删除所有表
        db.create_all()  # 创建表
