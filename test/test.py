from flask import Flask, current_app

app = Flask(__name__)
# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext

# 手动将应用上下文入栈
# ctx = app.app_context()
# ctx.push()

# a = current_app
# 使用
# d = current_app.config['DEBUG']
# 出栈
# ctx.pop()


# 使用with改写
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']

# 存在__enter__和__exit__方法，即为上下文管理器

class A:
    def __enter__(self):
        a = 1
    def __exit__(self):
        b = 2
with A() as obj_A:
    pass