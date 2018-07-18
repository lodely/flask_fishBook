#!/usr/bin/python
# -*- coding: UTF-8 -*-


from app.models.gift import Gift
from app.view_models.book import BookViewModel
from . import web
from flask import render_template
from flask_login import current_user




@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html', recent=books)


@web.route('/personal')
def personal_center():
    user = current_user.summary
    return render_template('personal.html', user=user)
