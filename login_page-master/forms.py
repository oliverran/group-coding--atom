# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField(u'请输入用户名：', validators=[DataRequired()])
    password = PasswordField(u'请输入密码：', validators=[DataRequired()])
    identity = SelectField(u'请选择身份', choices=[('0', u'管理员'),('1', u'教师'),('2', u'学生')], default='2')
    submit = SubmitField(u'登录')