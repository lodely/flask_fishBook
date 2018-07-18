#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json

from flask import jsonify, request, render_template, flash, current_app
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook

# 从当前目录导入蓝图
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
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
    books = BookCollection()

    if form.validate():
        # 取得q、page的值
        # strip()将q的空格去掉
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return jsonify(books.__dict__)

    else:
        flash('搜索关键字不符合要求，请重新输入')
        # return json.dumps(result), 200, { 'content-type' : 'application/json'}
    return render_template('search_result.html', books=books)

@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    # 一本书默认不在赠送清单，也不在心愿清单
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍的详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    # MVC MVT
    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn,
                               launched=False, status=current_app.config['BOOK_STATUS_OK']).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn,
                               launched=False, status=current_app.config['BOOK_STATUS_OK']).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False, status=current_app.config['BOOK_STATUS_OK']).all()
    trade_wishs = Wish.query.filter_by(isbn=isbn, launched=False, status=current_app.config['BOOK_STATUS_OK']).all()
    trad_gift = TradeInfo(trade_gifts)
    trad_wish = TradeInfo(trade_wishs)

    return render_template('book_detail.html',
                           book=book,
                           wishes=trad_wish,
                           gifts=trad_gift,
                           has_in_gifts=has_in_gifts,
                           has_in_wishes=has_in_wishes)
    # return render_template('book_detail.html', book=book, wishes=[], gifts=[])



