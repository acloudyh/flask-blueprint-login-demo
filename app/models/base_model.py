# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : base_model.py
# Software: PyCharm
# Time    : 2020/4/1 12:02
# Description:

class BaseModel(object):

    def to_json(self):
        """
        查询结果转换json (单表)
        :return:
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
