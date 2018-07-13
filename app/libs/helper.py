#!/usr/bin/python
# -*- coding: UTF-8 -*-

def is_isbn_or_key(word):
    # isbn13 13个数字组成
    # isbn10 10个数字组成，含有‘-’
    isbn_or_key = 'key'

    # isdigit判断变量是不是全都由数字组成
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key