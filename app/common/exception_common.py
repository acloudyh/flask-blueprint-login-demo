# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : exception_common.py
# Software: PyCharm
# Time    : 2020/3/30 17:35
# Description:
from flask import jsonify, current_app

from app import app


class ExceptionCommon(Exception):
    # 默认的返回码
    status = 400

    # 自己定义了一个 return_code，作为更细颗粒度的错误代码
    def __init__(self, message=None, status=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status is not None:
            self.status = status
        self.payload = payload

    # 构造要返回的错误代码和错误信息的 dict
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['status'] = self.status
        rv['message'] = self.message
        # 日志打印
        current_app.logger.error(rv['status'], rv['message'])
        return rv


@app.errorhandler(ExceptionCommon)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
