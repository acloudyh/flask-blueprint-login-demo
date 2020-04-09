# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : test2.py
# Software: PyCharm
# Time    : 2020/3/31 15:43
# Description:
import hashlib

salt = 'python-flask'
password = 'admin'
md5 = hashlib.md5()
md5.update((password + salt).encode('utf8'))

print(md5.hexdigest())
