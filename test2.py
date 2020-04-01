# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : test2.py
# Software: PyCharm
# Time    : 2020/3/31 15:43
# Description:
import subprocess

password = '6yhn^YHN'
command = 'mkdir t4'
ret = subprocess.call('cd /opt', shell=True)
subprocess.call('echo {} | sudo -S {}'.format(password, command), shell=True, cwd='/opt')
ret = subprocess.call('pwd')
