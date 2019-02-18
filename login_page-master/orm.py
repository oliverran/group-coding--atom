# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime, os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),os.path.pardir))

from An_login import app

db = SQLAlchemy(app)

class Admin(db.Model):
    _tablename_ = u"admin"
    id = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))
 
    def __init__(self, id=None, password=None):
        self.id = user_id
        self.password = password

    def __repr__(self):
        return '<Admin %s>' % self.id


class Student(db.Model):
    _tablename_ = u"student"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    idcard = db.Column(db.String(50))
    address = db.Column(db.String(50))
    nation = db.Column(db.String(50))
    classid = db.Column(db.String(50))
    time = db.Column(db.DateTime)
    elseinfo = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
    lessions = db.relationship(u"Lession", backref = "student", cascade = "all")

    def __init__(self, id, name, sex, idcard, address, nation, classid, time, elseinfo, password):
        self.id = id
        self.name = name
        self.sex = sex
        self.idcard = idcard
        self.address = address
        self.nation = nation
        self.classid = classid
        self.time = time
        self.elseinfo = elseinfo
        self.password = password

    def __repr__(self):
        return '<Student %s>' % self.id  
        
        
class Teacher(db.Model):
    _tablename_ = u"teacher"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    sex = db.Column(db.String(50))
    idcard = db.Column(db.String(50))
    address = db.Column(db.String(50))
    nation = db.Column(db.String(50))
    department = db.Column(db.String(50))
    title = db.Column(db.String(50))
    password = db.Column(db.String(50))
    
    lectures = db.relationship(u"Lecture", backref = "teacher", cascade = "all")

    def __init__(self, id, name, sex, idcard, address, nation, department, title, password):
        self.id = id
        self.name = name
        self.sex = sex
        self.idcard = idcard
        self.address = address
        self.nation = nation
        self.department = department
        self.title = title
        self.password = password

    def __repr__(self):
        return '<Teacher %s>' % self.id


class Course(db.Model):
    _tablename_ = u"course"
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    credit = db.Column(db.String(50))
    period = db.Column(db.String(50))
    kind = db.Column(db.String(50))
    number = db.Column(db.Integer)
    describe = db.Column(db.String(50))  
    
    lectures = db.relationship(u"Lecture", backref = "course", cascade = "all")    

    def __init__(self, id, name, credit, period, kind, number, describe):
        self.id = id
        self.name = name
        self.credit = credit
        self.period = period
        self.kind = kind
        self.number = number
        self.describe = describe

    def __repr__(self):
        return '<Course %s>' % self.id

     
class Lession(db.Model):
    _tablename_ = u"lession"
    id = db.Column(db.String(50), primary_key=True)
    lecture_id = db.Column(db.String(50), db.ForeignKey(u'lecture.id'))
    student_id = db.Column(db.String(50), db.ForeignKey(u'student.id'))
    grade = db.Column(db.Integer)
    
    def __init__(self, id, lecture_id, student_id, grade):
        self.id = id
        self.lecture_id = lecture_id
        self.student_id = student_id
        self.grade = grade
        
    def __repr__(self):
        return '<Lession %s>' % (self.id)


class Lecture(db.Model):
    _tablename_ = u"lecture"
    id = db.Column(db.String(50), primary_key=True)
    course_id = db.Column(db.String(50), db.ForeignKey(u'course.id'))
    teacher_id = db.Column(db.String(50), db.ForeignKey(u'teacher.id'))
    year = db.Column(db.String(50))
    
    lessions = db.relationship(u"Lession", backref = "lecture", cascade = "all")
    
    def __init__(self, id, course_id, teacher_id, course_year):
        self.id = id
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.year = year
        
    def __repr__(self):
        return '<Lecture %s>' % (self.id)




        