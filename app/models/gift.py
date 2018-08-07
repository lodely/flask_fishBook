#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, desc, func
from collections import namedtuple

from app.spider.yushu_book import YuShuBook

EachGiftWishCount = namedtuple('EachGiftWishCount', ['count', 'isbn'])

class Gift(Base):
    id = Column(Integer, primary_key = True)
    launched = Column(Boolean, default=False)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable = False)
    book = relationship('Book')
    bid = Column(Integer, ForeignKey('book.id'))

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_user_gifts(cls, uid):
        # 添加Gift.status，判断礼物状态，如果是为0，则表示已撤销，不需要再赠送清单中显示
        gifts = Gift.query.filter(
                    Gift.uid==uid, Gift.launched==False,
                    Gift.status!=current_app.config['BOOK_STATUS_DELETE']).order_by(
                desc(Gift.create_time)).all()
        return gifts

    # 把方法转换为属性
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_wish_counts(cls, isbn_list):
        # 函数内导入
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
                Wish.launched == False,
                Wish.isbn.in_(isbn_list),
                Wish.status == 1).group_by(
                Wish.isbn).all()
        count_list = [{'count' : w[0], 'isbn' : w[1]} for w in count_list]
        return count_list

    # 对象代表一个礼物
    # 类代表礼物这个事物
    # 类方法和类对应，而不是和具体的实例对应
    @classmethod
    def recent(cls):
        # 分组、排序、限制查询数量
        # 链式调用，主体query，子函数，最后需要触发语句，如first(),all()
        recent_gift = Gift.query.filter_by(
                launched=False).group_by(
                Gift.isbn).order_by(
                desc(Gift.create_time)).limit(
                current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift

