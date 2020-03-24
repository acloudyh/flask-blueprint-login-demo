from flask_wtf import FlaskForm  # , RecaptchaField
from wtforms import StringField, PasswordField, SubmitField  # , BooleanField
from wtforms.validators import EqualTo, DataRequired, Regexp


class LoginForm(FlaskForm):
    """登录表单类"""
    username = StringField(
        # 标签
        label="用户名",
        # 验证器
        validators=[
            DataRequired('请输入用户名')
        ],
        description="用户名",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )

    password = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码!')
        ],
        description="密码",

        # 附加选项(主要是前端样式),会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'  # 表示输入框不能为空
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )


class SignupForm(FlaskForm):
    """用户注册表单类"""

    username = StringField(
        # 标签
        label="用户名:",
        # 验证器
        validators=[
            DataRequired('请输入用户名'),

            # Regexp("^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{8,}$", message="用户名规则不正确")
        ],
        description="用户名",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )

    password = PasswordField(
        label="新密码:",
        # 验证器
        validators=[
            DataRequired('请输入新密码'),
            Regexp("^[0-9a-zA-Z_]{1,}$", message="密码规则不正确")
        ],
        description="新密码:",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码!",
            "required": 'required'  # 表示输入框不能为空
        }
    )

    confirm_password = PasswordField(
        # 标签
        label="确认密码:",
        # 验证器
        validators=[
            DataRequired('确认密码'),
            Regexp("^[0-9a-zA-Z_]{1,}$", message="密码规则不正确"),
            EqualTo('password', message="两次密码输入不一致")  # 判断两次输入的密码是否一致
        ],
        description="确认密码",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请确认密码!",
            "required": 'required'  # 表示输入框不能为空
        }
    )

    submit = SubmitField(
        label="提交",
        render_kw={
            "class": "btn btn-success btn-block",
        }
    )


class EditPasswordForm(FlaskForm):
    """用户修改密码表单类"""
    original_password = PasswordField('原密码', validators=[DataRequired()])

    new_password = PasswordField(
        label="新密码",
        # 验证器
        validators=[
            DataRequired('请输入新密码'),
            Regexp("^[0-9a-zA-Z_]{1,}$", message="密码规则不正确")
        ],
        description="新密码",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码!",
            "required": 'required'  # 表示输入框不能为空
        }
    )

    confirm_password = PasswordField(
        # 标签
        label="确认密码",
        # 验证器
        validators=[
            DataRequired('确认密码'),
            Regexp("^[0-9a-zA-Z_]{1,}$", message="密码规则不正确"),
            EqualTo('new_password', message="两次密码输入不一致")  # 判断两次输入的密码是否一致
        ],
        description="确认密码",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "确认密码",
            "required": 'required'  # 表示输入框不能为空
        }
    )
    submit = SubmitField(
        label="提交",
        render_kw={
            "class": "btn btn-success btn-block",
        }
    )