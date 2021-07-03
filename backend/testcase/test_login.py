#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/28 16:58
# @Author  : zc
# @File    : test_login.py


import requests



class TestLogin:

    BASE_URL = "http://127.0.0.1:5000"



    def test_login(self):
        r = requests.get(self.BASE_URL + "/login",auth=("zc1","123456"))
        assert r.status_code == 200
        assert "access_token" in r.json()

        r = requests.get(self.BASE_URL + "/login", auth=("zc11", "123456"))
        assert r.status_code == 401