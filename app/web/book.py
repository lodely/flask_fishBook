#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

# 从当前目录导入蓝图
from . import web
# 该注册路由即为蓝图,可以在flask核心对象app上注册多个蓝图
# 用蓝图来调用视图函数，最终还是通过调用app来显示



@web.route('/book/search')
def search():
    '''
        q: 普通关键字和isbn
        page
    '''

    # 测试URL http://127.0.0.1:5000/book/search?q=9787539123639&page=1
    # q = request.args['q']
    # page = request.args['page']

    # 验证
    form = SearchForm(request.args)
    if form.validate():
        # 取得q、page的值
        # strip()将q的空格去掉
        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
    # return json.dumps(result), 200, { 'content-type' : 'application/json'}