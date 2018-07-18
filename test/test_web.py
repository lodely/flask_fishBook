#!/usr/bin/python
# -*- coding: UTF-8 -*-
from app.web import web

@web.route('/test')
def test():
    from flask import request
    from app.libs.none_local import n
    print(n.v)
    n.v += 1
    print('-----------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print('-----------------')

    return ''