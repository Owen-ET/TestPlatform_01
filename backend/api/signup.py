#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/07/19 18:48
# @Author  : zc
# @File    : signup.py
from flask import request
from flask_restful import Resource

from backend.backend_server import db
from backend.data_base.user_table import User


class SignUp(Resource):


    def post(self):
        json = request.json
        new_user = User(**json)
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        # return {"info": json,"errcode": 200}
        return {"msg": "OK","errcode": 200}