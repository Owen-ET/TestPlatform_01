#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/28 17:06
# @Author  : zc
# @File    : testcase.py


# 测试用例新增接口
from flask import request
from flask_restful import Resource

from backend.api.verify_token import auth
from backend.backend_server import db
from backend.data_base.testcase_table import TestCase


class TestCaserAdd(Resource):

    method_decorators = [auth.login_required]
    def post(self):
        """
        新增用例
        :return:
        """
        # nodeId = request.json.get('nodeId')
        # description = request.json.get('description')
        # return [nodeId,description]

        # 把请求体中的数据发送到数据库
        data = TestCase(**request.json)
        db.session.add(data)
        db.session.commit()
        return {'msg':'add is OK！'}



class TestCaserDelete(Resource):

    method_decorators = [auth.login_required]

    def get(self):
        """
        获取所有测试用例数据
        :return:
        """
        # return {'hello':'get'}


        if "nodeid" in request.args:
            nodeId = request.args.get("nodeid")
            data = TestCase.query.filter_by(nodeid=nodeId).first()
            if data != None:
                db.session.delete(data)
                db.session.commit()
                return {'msg':'del one is success!'}
            else:
                return {'msg':'nodeId is null'}

        elif "nodeids" in request.args:
            nodeIds = request.args.get("nodeids")
            for nodeId in nodeIds.split(","):
                data = TestCase.query.filter_by(nodeid=nodeId).first()
                if data != None:
                    db.session.delete(data)
                else:
                    return {'msg':'nodeId is null'}
            db.session.commit()
            return {'msg': 'del many is success!'}



# 测试用例接口2
class TestCaserUpdate(Resource):

    method_decorators = [auth.login_required]
    def post(self):
        """
        更新用例
        :return:
        """
        request_body = request.json
        data = TestCase.query.filter_by(nodeid=request_body.get("nodeid")).first()
        data.description = request_body.get("description")
        db.session.commit()
        return {'msg':'update is success'}



class TestCaserGet(Resource):

    method_decorators = [auth.login_required]
    def get(self):

        testcase = TestCase.query.all()
        format_testcase = [i.as_dict() for i in testcase]
        return {"msg":"ok","data": format_testcase}