from flask_wtf import FlaskForm  # , RecaptchaField
from wtforms import StringField, PasswordField  # , BooleanField
from wtforms.validators import EqualTo, DataRequired


class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])


class SignupForm(FlaskForm):
    """用户注册表单类"""
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', [
        DataRequired(),
        EqualTo('confirm', message='两次输入的密码不一致')
    ])
    confirm = PasswordField('确认密码')
