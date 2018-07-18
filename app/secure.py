#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 数据库密码之类机密的参数写到这个文件

DEBUG = True
# SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/fisher'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:root@localhost:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'GHOIAHGOIAHTGAngbaiohga'

# Email配置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = 'nodely@qq.com'
MAIL_PASSWORD = 'zecnurdmzrzbbcij'
