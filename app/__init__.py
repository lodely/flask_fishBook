#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 调用蓝图
    register_blueprint(app)
    return app

def register_blueprint(app):
    # 导入蓝图对象，在app中注册蓝图
    from app.web.book import web
    app.register_blueprint(web)