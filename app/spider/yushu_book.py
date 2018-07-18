#!/usr/bin/python
# -*- coding: UTF-8 -*-

from app.libs.httper import HTTP
# 导入当前的app核心对象
from flask import current_app

class YuShuBook:
    # 模型层 MVC M层
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    # 定义使用isbn查询
    # 定义为classmethod后可以不用通过类名访问，而是使用cls访问
    # @classmethod
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        # 获取到的result是dict类型
        result = HTTP.get(url)
        self.__fill_single(result)

    # 定义使用关键字查询, 默认搜索15条，从最开始搜索
    # @classmethod
    def search_by_keyword(self, keyword, page = 1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    # 使用函数计算从哪条内容开始显示
    # @staticmethod
    def calculate_start(self, page):
        return (page-1) * current_app.config['PER_PAGE']

    # 定义私有的实例方法
    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    @property
    def first(self):
        return self.books[0] if self.total >=1 else None