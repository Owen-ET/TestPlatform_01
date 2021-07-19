#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/07/19 18:48
# @Author  : zc
# @File    : signup.py
from flask import request
from flask_restful import Resource


class SignUp(Resource):


    def post(self):
        json = request.json
        return {"info": json}