# -*- coding: utf-8 -*-
from An_login import app
from forms import LoginForm
from flask import render_template, redirect, request, flash, session

from orm import Admin, Student, Teacher

__author__ = 'cyk'

role_ = {
    '0': [Admin, u'管理员'],
    '1': [Teacher, u"教师"],
    '2': [Student, u"学生"]
}


@app.route('/', methods=['GET', 'POST'])
def role_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        identity = form.identity.data

        if identity in role_.keys():
            return user_login(role_[identity][0], username, password, role_[identity][1])
        else:
            return "ERROR!"

    return render_template('login.html', form=form)


def user_login(role_class, username, password, dscr):
    user = role_class.query.filter_by(id=username).first()
    if user:
        if verify_login(username, password, role_class):
            session['login'] = True
            return u"%s登录页面！登录状态：%s" % (dscr ,session['login'])
        else:
            return goto_login(u"用户名或密码错误！请重新输入！")
    else:
        return goto_login(u"该用户不存在！")


def verify_login(id, password, role):
    user = role.query.filter_by(id=id, password=password).first()
    if not user:
        return False
    else:
        return user.id


def goto_login(msg=None):
    form = LoginForm()
    flash(msg)
    return render_template('login.html', form=form)