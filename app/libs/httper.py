#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests

class HTTP:
    # 和类跟对象都没关系的方法，可以定义为静态方法，参数传入不用填写self
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # 判断返回的状态码，确定是否有该图书
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text

        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r
        # esle:
        #     if return_json:
        #         return {}
        #     else:
        #         return ""
