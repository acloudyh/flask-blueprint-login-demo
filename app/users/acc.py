# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : acc.py
# Software: PyCharm
# Time    : 2020/3/18 21:04
# Description:
from flask import Blueprint

acc_bp = Blueprint('acc', __name__)


@acc_bp.route("/acc")
def accfunction():
    return "这是acc的蓝图路由"
