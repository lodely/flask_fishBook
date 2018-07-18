#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import Flask
from app.models.base import db
from flask_login import LoginManager
from flask_mail import Mail

login_manager = LoginManager()
mail = Mail()

def create_app():
    app = Flask(__name__)
    # 导入配置
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 调用蓝图
    register_blueprint(app)

    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'

    mail.init_app(app)

    # init_app并没有使用self.app保存app
    db.init_app(app)
    # 故需要重新传入
    db.create_all(app=app)
    return app

def register_blueprint(app):
    # 导入蓝图对象，在app中注册蓝图
    from app.web.book import web
    app.register_blueprint(web)

