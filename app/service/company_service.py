# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : company_service.py
# Software: PyCharm
# Time    : 2020/3/20 10:20
# Description:
from app.models.company import Company


def get_all_company():
    companys = Company.query.all()
    return companys
