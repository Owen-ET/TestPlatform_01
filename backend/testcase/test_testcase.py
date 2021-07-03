#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/28 18:56
# @Author  : zc
# @File    : test_testcase.py
import requests


class TestTestCase:

    def test_get_testcase(self):
        r = requests.get("http://127.0.0.1:5000/login", auth=("zc1","123456"))
        token = r.json().get("access_token")
        r = requests.get("http://127.0.0.1:5000/testcase/get",auth=(token,""))
        assert r.status_code == 200
        assert r.json().get("msg") == 'ok'



    def test_get_error_testcase(self):
        r = requests.get("http://127.0.0.1:5000/login", auth=("zc1","123456"))
        token = ""
        r = requests.get("http://127.0.0.1:5000/testcase/get",auth=(token,""))
        assert r.status_code == 401