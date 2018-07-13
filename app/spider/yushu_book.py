#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app.libs.httper import HTTP
# 导入当前的app核心对象
from flask import current_app

class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    # 定义使用isbn查询
    # 定义为classmethod后可以不用通过类名访问，而是使用cls访问
    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        # 获取到的result是dict类型
        result = HTTP.get(url)
        return result

    # 定义使用关键字查询, 默认搜索15条，从最开始搜索
    @classmethod
    def search_by_keyword(cls, keyword, page = 1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page))
        result = HTTP.get(url)
        return result

    # 使用函数计算从哪条内容开始显示
    @staticmethod
    def calculate_start(page):
        return (page-1) * current_app.config['PER_PAGE']