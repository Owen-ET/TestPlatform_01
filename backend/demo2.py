#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/19 14:06
# @Author  : zc
# @File    : user_table.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
# 配置数据库的详细信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567@192.168.10.113:8881/ZC_17'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 初始化一个db
db = SQLAlchemy(app)

# 使用db，可以让类映射到数据库中的表
class User(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    email2 = db.Column(db.String(120), unique=True, nullable=False)
    email3 = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.username} {self.email}>'



class Task(db.Model):


    task_id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.task_name


if __name__ == '__main__':

    # # 删库
    # db.drop_all()
    # # 在远程数据库创建表
    # db.create_all()


    # # 对User表插入数据，实例化User类
    # for i in range(20):
    #     data = User(username="zc"+str(i),email='123'+str(i)+'@qq.com',email2='321'+str(i)+'@qq.com',email3='231@q.com')
    #     db.session.add(data)
    #     db.session.commit()
    #
    # data = User(username='zc10',email='12310@qq.com',email2='32110@qq.com',email3='hello')
    # db.session.add(data)
    # db.session.commit()


    # # 查询
    # result = User.query.filter(or_(User.id=='15',User.email3.like('%h%'))).all()
    # print(result)
    # result1 = [i for i in result if '1' in i.username]
    # print(result1)



    # # 更新
    # data = User.query.filter_by(username='zc10').first()
    # data.email3 = 'hello'
    # db.session.commit()


    # # 删除
    data = User.query.filter_by(username='zc10').first()
    db.session.delete(data)
    db.session.commit()
