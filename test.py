# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : test.py
# Software: PyCharm
# Time    : 2020/3/18 21:49
# Description:

# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : SQLAlchemy-demo.py
# Software: PyCharm
# Time    : 2020/3/12 10:50
# Description: SQLAlchemy demo
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('sqlite:///app/sqlite3flask.db', echo=True)
# 映射基类
Base = declarative_base()


# 具体映射类
class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password_hash = Column(String(256))
    authenticated = Column(Boolean, default=False)


import hashlib
salt = 'gateway'
md5 = hashlib.md5()
print('ad123min'.encode('utf8'))
md5.update('ad123min'.encode('utf8'))
print(md5.hexdigest())




