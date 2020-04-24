# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : manage.py
# Software: PyCharm
# Time    : 2020/3/18 16:58
# Description:
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, use_reloader=False)
