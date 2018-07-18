#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import flash, current_app, url_for, redirect, render_template

from app.libs.enums import PendingStatus
from app.models.base import db
from app.models.drift import Drift
from app.models.gift import Gift
from app.view_models.gift import MyGifts
from app.view_models.trade import MyTrades
from . import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)

    # 赠送清单的书名列表
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)

    view_model = MyTrades(gifts_of_mine, wish_count_list)
    return render_template('my_gifts.html', gifts=view_model.trades)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            # 每上传一本书，加0.5分
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)

    else:
        flash('这本书已经在你的赠送清单或者心愿清单中，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
@login_required
def redraw_from_gifts(gid):
    gift = Gift.query.filter_by(id=gid, launched=False, status=current_app.config['BOOK_STATUS_OK']).first_or_404()
    # 查询这本书的交易状态

    drift = Drift.query.filter_by(gift_id=gid, _pending=PendingStatus.Waiting.value).first()
    # drift_test = Drift.query.filter_by(gift_id=gid, pending=PendingStatus.Waiting).first()

    if drift:
        flash('这本书正处于交易状态，请先完成该交易')
    else:
        # 在赠送清单中撤销，减0.5分
        with db.auto_commit():
            current_user.beans -= current_app.config['BEANS_UPLOAD_ONE_BOOK']
            gift.delete()
    return redirect(url_for('web.my_gifts'))

# 测试
@web.route('/mygift/test')
def mygift_test():
    return str(current_app.config['BEANS_UPLOAD_ONE_BOOK'])


