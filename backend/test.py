#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/19 13:49
# @Author  : zc
# @File    : test.py


from flask import Flask

app = Flask(__name__)


@app.route('/')
def url1():
    return '<H1>hello world!</H1>'

@app.route('/test')
def url2():
    return '<p>hello flask!</p>'


if __name__ == '__main__':
    app.run(debug=True)




# a = 12597450.05
# b = 12597448.04
# 
# c = a - b
# print("支付金额："+str(round(c,2)))