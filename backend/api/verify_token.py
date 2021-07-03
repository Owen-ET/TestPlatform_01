#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/28 15:42
# @Author  : zc
# @File    : verify_token.py


# https://flask-httpauth.readthedocs.io/en/latest/
from flask import g
from flask_httpauth import HTTPBasicAuth

from backend.data_base.user_table import User

auth = HTTPBasicAuth()


"""

"""
@auth.verify_password
def verify_password(username, password):


    print(username,password)
    user = User.check_token(username)

    if not user:
        user = User.query.filter_by(username=username).first()

        if not user or user.password != password:
            return False

    g.user = user
    return True