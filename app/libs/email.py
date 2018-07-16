#!/usr/bin/python
# -*- coding: UTF-8 -*-
from threading import Thread

from flask import current_app, render_template

from app import mail
from flask_mail import Message

# 异步发送邮件
def send_async_email(app, msg):
    with app.app_context():
        try:
            mail.send(msg)
        except Exception as e:
            pass


def send_mail(to, subject, template, **kwargs):
    # msg = Message('测试邮件', sender='nodely@qq.com', body='Test',
    #               recipients=['noveltty@qq.com'])

    msg = Message('[鱼书]' + ' ' + subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    # 获取真实的核心app
    app = current_app._get_current_object()
    # 开启新线程
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
