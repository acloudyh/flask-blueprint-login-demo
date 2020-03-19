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
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(32))

# 创建表
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
#
# # 创建 Session 类实例
# session = Session()
#
# company = Company(name='杨', age=1, address='jiangsu', salary=200)
# session.add(company)
# session.commit()
# session.close()
