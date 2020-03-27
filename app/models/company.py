# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : company.py
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

    def __init__(self) -> None:
        super().__init__()

    def to_json(self):
        """
        转换成json
        :return:
        """
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict
