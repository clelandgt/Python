# -*- coding: utf-8 -*-
# @File  : __init__.py.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-02
# @Desc  :

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS

cors = CORS()  # 跨站请求伪造保护
bootstrap = Bootstrap()  # 引入著名的CSS前端框架


def create_app():
    app = Flask(__name__)

    bootstrap.init_app(app)
    cors.init_app(app, supports_credentials=True)

    from .calc import calc
    app.register_blueprint(calc)

    return app
