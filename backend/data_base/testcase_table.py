#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/06/28 17:07
# @Author  : zc
# @File    : testcase_table.py


from backend.backend_server import db


# 使用db，可以让类映射到数据库中的表
class TestCase(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    nodeId = db.Column(db.String(80), unique=True, nullable=False)
    # 描述字段
    description = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'< {self.id} {self.nodeId} {self.description}>'


    def as_dict(self):
        return {'id':self.id,'nodeId':self.nodeId,'description':self.description}