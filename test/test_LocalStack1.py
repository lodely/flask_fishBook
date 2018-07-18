#!/usr/bin/python
# -*- coding: UTF-8 -*-

from werkzeug.local import  LocalStack
import threading
import time

my_stack = LocalStack()
my_stack.push(1)
print("I am main thread, and first query top data is: %d\n" % my_stack.top)

def new_work():
    print("I am new branch thread, and first query top data is: %s\n" % str(my_stack.top))
    my_stack.push(2)
    print("I am new branch thread, and top data is: %d\n" % my_stack.top)

new_t = threading.Thread(target=new_work, name='new branch thread')
new_t.start()
time.sleep(1)

# my_stack.push(3)
print("I am main thread, and top data is: %d" % my_stack.top)
print('I am main thread, and top data is: %d' % my_stack.top)


