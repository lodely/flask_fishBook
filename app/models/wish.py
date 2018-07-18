#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, desc, func


from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key = True)
    launched = Column(Boolean, default=False)

    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable = False)
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'))

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False,
                                      status=current_app.config['BOOK_STATUS_OK']).order_by(
                                desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        # 在函数内导入，防止循环导入出错
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
                Gift.launched == False,
                Gift.isbn.in_(isbn_list),
                Gift.status == 1).group_by(
                Gift.isbn).all()
        count_list = [{'count' : w[0], 'isbn' : w[1]} for w in count_list]
        return count_list

    # 把方法转换为属性
    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

