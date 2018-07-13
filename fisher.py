#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask

from app import create_app

app = create_app()


if __name__ == '__main__':

    app.run(host='0.0.0.0', debug=app.config['DEBUG'])
