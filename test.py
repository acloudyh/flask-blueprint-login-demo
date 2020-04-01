# -*- coding: utf-8 -*-
# Author  : Yang Hao
# File    : test.py
# Software: PyCharm
# Time    : 2020/3/20 18:12
# Description:
# import hashlib
# import subprocess
#
# salt = 'gateway'
# md5 = hashlib.md5()
# print('ad123min'.encode('utf8'))
# md5.update('ad123min'.encode('utf8'))
# print(md5.hexdigest())
#
# import re
#
# pattern = re.compile(r'^(?![0-9]+$)(?![^0-9]+$)(?![a-zA-Z]+$)(?![^a-zA-Z]+$)(?![a-zA-Z0-9]+$)[a-zA-Z0-9\S]{8,20}$')
# str = '6yhn^YHN'
# print(pattern.search(str))
import subprocess

print("---------------1---------------")
# subprocess.run 接受字符串或者列表形式的命令，返回命令执行结果和状态码
ret = subprocess.run(["df", "-h"])
print(ret)
print('\n')

print("---------------2---------------")
# subprocess.call() 执行命令，返回命令执行结果和状态码
# ret = subprocess.call(["ls", "-l"], shell=False)  # shell为False的时候命令必须分开写
# ret = subprocess.call("ls -l", shell=True)
ret = subprocess.call(["ls", "-l"])
print(ret)
print('\n')

print("---------------3---------------")
# subprocess.check_call() 执行命令，返回结果和状态，正常为0；执行错误则抛出异常
ret = subprocess.check_call(["ls", "-l"])
print(ret)
print('\n')

print("---------------4---------------")
# subprocess.getstatusoutput() 接受字符串形式的命令，返回一个元组形式的结果：第一个元素是状态码，第二个为执行结果
ret = subprocess.getstatusoutput('pwd')
print(ret)
print('\n')

print("---------------5---------------")
# subprocess.getoutput() 接受字符串形式的命令，返回执行结果
ret = subprocess.getoutput('pwd')
print(ret)
print('\n')

print("---------------6---------------")
# subprocess.check_output() 执行命令，返回运行结果，而不是打印
ret = subprocess.check_output('pwd')
print(ret)
print('\n')

print("---------------7---------------")
# subprocess.Popen 用于执行复杂的系统命令
# obj = subprocess.Popen("mkdir t3", shell=True, cwd='/opt')
# print(obj)

password = 'xxxxx'
command = 'mkdir t4'
ret = subprocess.call('cd /opt', shell=True)
subprocess.call('echo {} | sudo -S {}'.format(password, command), shell=True, cwd='/opt')
ret = subprocess.call('pwd')
