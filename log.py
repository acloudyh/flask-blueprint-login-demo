# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : log.py
# Software: PyCharm
# Time    : 2020/4/24 10:02
# Description:
import logging
import os
from logging.handlers import RotatingFileHandler


def init_log(app):
    """
    日志初始化
    :param app:
    """
    log_path = app.config.get("LOG_PATH")
    log_name = app.config.get("LOG_NAME")

    if not os.path.exists(log_path):  # 创建日志目录
        os.makedirs(log_path)

    # backupCount 备份日志个数; maxBytes 单个文件大小
    file_handler = RotatingFileHandler(os.path.join(log_path, log_name), maxBytes=10 * 1024 * 1024,
                                       backupCount=2, encoding='UTF-8')
    logging_format = logging.Formatter("%(asctime)s - [%(filename)s:%(funcName)s:%(lineno)d] - [%("
                                       "levelname)s] : %(message)s")
    file_handler.setFormatter(logging_format)
    app.logger.addHandler(file_handler)
