#!/usr/bin/python
# -*- coding: UTF-8 -*-

class _BookViewModel:

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

# 重构BookViewModel类，使用面向对象的思想，放弃上面使用面向过程的思想
class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher =  book['publisher']
        self.pages = book['pages']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    # 添加property装饰器，可以使用属性的方式调用函数
    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])
        return ' / '.join(intros)

class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

