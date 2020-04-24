import re
import unittest

from bs4 import BeautifulSoup

from app import app


class AuthTest(unittest.TestCase):

    def setUp(self):
        app.app_context().push()
        self.app = app.test_client()
        self.app.testing = True
        self.username = 'admin'
        self.password = 'admin'
        self.original_password = 'admin'
        self.new_password = 'admin123'
        self.confirm_password = 'admin123'
        print('-------------------------------开始测试-------------------------------')

    def tearDown(self):
        print('-------------------------------结束测试-------------------------------\n')

    def test_01_login(self):
        # 获取csrf_token
        csrf_token = self.get_csrf_token('auth/login')

        params = {'username': self.username, 'password': self.password, 'csrf_token': csrf_token}
        response = self.app.post('/auth/login', data=params, follow_redirects=True)

        # True为登录成功，False未登录失败
        self.assertTrue(not re.search('登录', bytes.decode(response.data)), msg='用户名或密码错误')

    def test_02_logout(self):
        # 先登录
        self.test_01_login()
        response = self.app.post('/auth/logout', follow_redirects=True)
        self.assertTrue('登录' in bytes.decode(response.data), msg='注销失败')

    def test_03_edit_password(self):
        # 先登录
        self.test_01_login()
        # 获取csrf_token
        csrf_token = self.get_csrf_token('/auth/edit_password')
        params = {'original_password': self.original_password, 'new_password': self.new_password,
                  'confirm_password': self.confirm_password, 'csrf_token': csrf_token}

        response = self.app.post('/auth/edit_password', data=params, follow_redirects=True)

        self.assertFalse('密码必须包含8到20个字母+数字+特殊字符' in bytes.decode(response.data), msg='密码必须包含8到20个字母+数字+特殊字符')
        self.assertFalse('两次密码输入不一致' in bytes.decode(response.data), msg='两次密码输入不一致')

    def test_04_reset_password(self):
        self.password = self.new_password
        self.test_01_login()

        response = self.app.post('/auth/reset', follow_redirects=True)
        self.assertTrue('登录' in bytes.decode(response.data), msg='重置失败')

    def get_csrf_token(self, url):
        login_html = bytes.decode(self.app.get(url).data)
        login_bs = BeautifulSoup(login_html, 'html5lib')
        csrf_token = login_bs.find(id='csrf_token')['value']
        return csrf_token


if __name__ == '__main__':
    unittest.main()
