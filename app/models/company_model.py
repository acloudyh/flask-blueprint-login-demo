# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : company_model.py
# Software: PyCharm
# Time    : 2020/3/20 10:06
# Description:
from app import db


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(50), nullable=False)

    def to_json(self):
        """
        转换json(数据库查询出的对象转换成字典相对应的json)
        :return:
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
