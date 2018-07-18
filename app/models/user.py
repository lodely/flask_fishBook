#!/usr/bin/python
# -*- coding: UTF-8 -*-
<<<<<<< HEAD
from math import floor
=======
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app

from app import login_manager
<<<<<<< HEAD
from app.libs.enums import PendingStatus
=======
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
from app.libs.helper import is_isbn_or_key
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin

<<<<<<< HEAD
from app.models.drift import Drift
=======
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class User(UserMixin, Base):
    id = Column(Integer, primary_key = True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=False)
    receive_counter = Column(Integer, default=False)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    _password = Column('password', String(128), nullable=False)

    @property
    def password(self):
        return self._password

    # 密码加密
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False

        # 不允许用户同时赠送多本相同的书
        # 一个用户不能同时成为赠送这和索要者

        # 书既不在赠送清单，也不在心愿清单才能添加
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False).first()
<<<<<<< HEAD
        if gifting:
            temp = Gift.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False, status=current_app.config['BOOK_STATUS_DELETE']).first()
            if temp:
                gifting = False

        wising = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                      launched=False).first()
        if wising:
            temp = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                       launched=False, status=current_app.config['BOOK_STATUS_DELETE']).first()
            if temp:
                wising = False

=======
        wising = Wish.query.filter_by(uid=self.id, isbn=isbn,
                                      launched=False).first()
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
        if not gifting and not wising:
            return True
        else:
            return False

    # expiration限制token的有效期600秒
    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        # 返回包含用户id的字符串
        return s.dumps({'id' : self.id}).decode('utf-8')

    @staticmethod
    def reset_password(token, new_password):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode('utf-8'))
        except:
            return False
        uid = data.get('id')
        with db.auto_commit():
            # 查询的值为主键时可以直接使用get方法
            user = User.query.get(uid)
            user.password = new_password
        return True

<<<<<<< HEAD
    def can_send_drift(self):
        if self.beans < 1:
            return False
        # 查询当前用户赠送书籍情况
        success_gifts_count = Gift.query.filter_by(
            uid=self.id, launched=True).count()
        success_receive_count = Drift.query.filter_by(
            requester_id=self.id, pending=PendingStatus.Success).count()

        return True if \
            floor(success_receive_count / 2) <= floor(success_gifts_count) \
            else False

    @property
    def summary(self):
        return dict(
            nickname=self.nickname,
            beans=self.beans,
            email=self.email,
            send_receive=str(self.send_counter) + '/' + str(self.receive_counter)
        )

=======
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))