#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/19 14:06
# @Author  : zc
# @File    : user_table.py
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired
from backend.backend_server import app, db



# 使用db，可以让类映射到数据库中的表
class User(db.Model):
    """
    用户表：账号、密码、邮箱、创建日期
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    # 创建日期

    def __repr__(self):
        return f'<User {self.username} {self.password}>'


    def generate_token(self,expires_in=3600*3):
        """
        生成token
        :param expires_in:超时
        :return:
        """
        # app.config['SECRETY_KEY']种子
        serializer = TimedJSONWebSignatureSerializer(app.config['SECRETY_KEY'],expires_in=expires_in)
        token_id = self.username + self.password + str(datetime.now())
        # dumps 用于反序列化，生成Token，字典转为字符串
        token = serializer.dumps({"id":self.id, "token_id": token_id}).decode()
        return token


    # 方便外界进行调用，同时此方法不会用到对象中的数据
    @classmethod
    def check_token(cls,token):
        """
        校验Token
        :return:
        """
        serializer = TimedJSONWebSignatureSerializer(app.config['SECRETY_KEY'])
        try:
            # loads用于序列化，把字符串转为字典
            token_loads_result = serializer.loads(token)
        except (BadSignature,SignatureExpired):
            return None

        return  User.query.get(token_loads_result['id'])





# class Task(db.Model):
#
#
#     task_id = db.Column(db.Integer, primary_key=True)
#     task_name = db.Column(db.String(80), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.task_name


if __name__ == '__main__':

    # 删库
    db.drop_all()
    # 在远程数据库创建表
    db.create_all()


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
    # data = User.query.filter_by(username='zc10').first()
    # db.session.delete(data)
    # db.session.commit()
