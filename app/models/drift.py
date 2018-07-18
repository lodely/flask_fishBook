#!/usr/bin/python
# -*- coding: UTF-8 -*-
<<<<<<< HEAD
from app.libs.enums import PendingStatus
from app.models.base import Base
from sqlalchemy import Column, Integer, String, SmallInteger

=======

from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, desc, func
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d

class Drift(Base):
    id = Column(Integer, primary_key=True)

    # 邮寄信息
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    # 书籍信息
    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    # 请求者信息
<<<<<<< HEAD
    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    # 赠送者信息
    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    _pending = Column('pending', SmallInteger, default=1)

    # 将_pending转换为枚举类型
    @property
    def pending(self):
        return PendingStatus(self._pending)

    # 将枚举类型转换为数字类型
    @pending.setter
    def pending(self, status):
        # 枚举类型加上.value转换为数字类型
        self._pending = status.value

=======
    requester_id = Column(Integer)
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
