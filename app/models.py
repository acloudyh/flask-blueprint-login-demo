# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : models.py
# Software: PyCharm
# Time    : 2020/3/18 17:50
# Description:
from app import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)


# 建立users数据表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    password = db.Column(db.String(32))


if __name__ == '__main__':
    from app import create_app

    app = create_app()
    # 离线脚本:
    with app.app_context():
        db.drop_all()  # 删除所有表
        db.create_all()  # 创建表
