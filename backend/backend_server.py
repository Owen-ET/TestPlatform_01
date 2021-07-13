#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/23 13:06
# @Author  : zc
# @File    : backend_server.py
from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_


app = Flask(__name__)
# 配置数据库的详细信息
# 单位数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567@192.168.10.113:8881/ZC_17'
# 家里数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@127.0.0.1:3306/ZC_17'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 配置数据库的详细信息
app.config['SECRETY_KEY'] = "ZC17"
# 初始化一个db
db = SQLAlchemy(app)
# 将flask实例加载到flask_restful
api = Api(app)
# 使用同源
CORS(app)

# # 使用db，可以让类映射到数据库中的表
# class TestCase(db.Model):
#
#
#     id = db.Column(db.Integer, primary_key=True)
#     nodeId = db.Column(db.String(80), unique=True, nullable=False)
#     # 描述字段
#     description = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return f'< {self.id} {self.nodeId} {self.description}>'
#
#
#     def as_dict(self):
#         return {'id':self.id,'nodeId':self.nodeId,'description':self.description}
#
#
# # 测试用例新增接口
# class TestCaserAdd(Resource):
#
#
#     def post(self):
#         """
#         新增用例
#         :return:
#         """
#         # nodeId = request.json.get('nodeId')
#         # description = request.json.get('description')
#         # return [nodeId,description]
#
#         # 把请求体中的数据发送到数据库
#         data = TestCase(**request.json)
#         db.session.add(data)
#         db.session.commit()
#         return {'msg':'add is OK！'}
#
#
#
# class TestCaserDelete(Resource):
#
#     def get(self):
#         """
#         获取所有测试用例数据
#         :return:
#         """
#         # return {'hello':'get'}
#
#
#         if "nodeId" in request.args:
#             nodeId = request.args.get("nodeId")
#             data = TestCase.query.filter_by(nodeId=nodeId).first()
#             if data != None:
#                 db.session.delete(data)
#                 db.session.commit()
#                 return {'msg':'del is success!'}
#             else:
#                 return {'msg':'nodeId is null'}
#
#         elif "nodeIds" in request.args:
#             nodeIds = request.args.get("nodeIds")
#             for nodeId in nodeIds.split(","):
#                 data = TestCase.query.filter_by(nodeId=nodeId).first()
#                 if data != None:
#                     db.session.delete(data)
#                 else:
#                     return {'msg':'nodeId is null'}
#             db.session.commit()
#             return {'msg': 'del is success!'}
#
#
#
# # 测试用例接口2
# class TestCaserUpdate(Resource):
#
#
#     def post(self):
#         """
#         更新用例
#         :return:
#         """
#         request_body = request.json
#         data = TestCase.query.filter_by(nodeId=request_body.get("nodeId")).first()
#         data.description = request_body.get("description")
#         db.session.commit()
#         return {'msg':'update is success'}
#
#
#
# class TestCaserGet(Resource):
#
#     def get(self):
#
#         testcase = TestCase.query.all()
#         format_testcase = [i.as_dict() for i in testcase]
#         return format_testcase


def router():
    from backend.api.testcase import TestCaserAdd
    from backend.api.testcase import TestCaserDelete
    from backend.api.testcase import TestCaserGet
    from backend.api.testcase import TestCaserUpdate
    from backend.api.login import Login
    # 新增路由
    api.add_resource(TestCaserAdd, '/testcase/add')
    # 删除路由
    api.add_resource(TestCaserDelete, '/testcase/delete')
    # 查询路由
    api.add_resource(TestCaserGet, '/testcase/get')
    # 更新路由
    api.add_resource(TestCaserUpdate, '/testcase/update')
    # 登录接口
    api.add_resource(Login, '/login')


if __name__ == '__main__':

    # db.drop_all()
    # db.create_all()
    #
    # for i in range(10):
    #     data = TestCase(nodeId='nodeId_'+str(i),description='用例'+str(i))
    #     db.session.add(data)
    # db.session.commit()

    # data = TestCase.query.all()
    # print(data)
    router()
    app.run(debug=True)