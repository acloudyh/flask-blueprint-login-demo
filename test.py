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
    username = Column(String(10), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    address = Column(String(50), nullable=False)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32))
    password_hash = Column(String(256))
    authenticated = Column(Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


# 创建表
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
#
# # 创建 Session 类实例
# session = Session()
#
# company = Company(username='杨', age=1, address='jiangsu', salary=200)
# session.add(company)
# session.commit()
# session.close()
