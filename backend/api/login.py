#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/28 15:35
# @Author  : zc
# @File    : login.py
from flask import g
from flask_restful import Resource

from backend.api.verify_token import auth


class Login(Resource):
    # method_decorators 代表给login接口添加一个装饰器，
    method_decorators = {'get': [auth.login_required]}


    def get(self):
        token = g.user.generate_token()
        return {"access_token":token}
