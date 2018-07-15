#!/usr/bin/python
# -*- coding: UTF-8 -*-

class BookViewModel:
    # 处理单本数据
    @classmethod
    def package_single(cls, data, keyword):
        returned = {
            'books' : [],
            'total' : 0,
            'keyword' : keyword
        }
        if data:
            returned['total'] = 1
            returned['books'] = [cls.__cut_book_data(data)]
        return returned

    # 处理多本书
    @classmethod
    def package_collection(cls, data, keyword):
        returned = {
            'books' : [],
            'total' : 0,
            'keyword' : keyword
        }
        if data:
            # 书籍数量
            returned['total'] = data['total']
            returned['books'] = [cls.__cut_book_data(book) for book in data['books']]
        return returned

    # 处理查询到的书籍信息
    @classmethod
    def __cut_book_data(cls, data):
        book = {
            # 书名
            'title' : data['title'],
            # 出版社
            'publisher' : data['publisher'],
            # 页数
            'pages' : data['pages'] or '',
            # 由于作者使用列表存储，可能存在多个作者，所以使用“、”连接
            'author' : '、'.join(data['author']),
            # 价格
            'price' : data['price'],
            # 简介
            'summary' : data['summary'] or '',
            # 图片
            'image' : data['image']
        }
        return book

    # 处理查询到的书籍信息
    @classmethod
    def __cut_books_data(cls, data):
        books = []
        for book in data['books']:
            r = {
                # 书名
                'title' : book['title'],
                # 出版社
                'publisher' : book['publisher'],
                # 页数
                'pages' : book['pages'],
                # 由于作者使用列表存储，可能存在多个作者，所以使用“、”连接
                'author' : '、'.join(book['author']),
                # 价格
                'price' : book['price'],
                # 简介
                'summary' : book['summary'],
                # 图片
                'image' : book['image']
            }
            books.append(r)
        return books