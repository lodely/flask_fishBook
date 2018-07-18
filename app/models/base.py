#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy
from sqlalchemy import Column, SmallInteger, Integer
from contextlib import contextmanager
from datetime import datetime

class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e


db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            # 判断当前对象是否包含否个属性
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
<<<<<<< HEAD
            return None

    def delete(self):
        self.status = 0
=======
            return None
>>>>>>> 051091b01b3d415ec55f23bd22026d22bbedd24d
