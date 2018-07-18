#!/usr/bin/python
# -*- coding: UTF-8 -*-

from werkzeug.local import  LocalStack

s = LocalStack()
s.push(3)
print(s.top)
print(s.top)
print(s.pop())
print(s.top)

