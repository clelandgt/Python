# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-01
# @Desc  : A Minimal Application: https://flask.palletsprojects.com/en/1.1.x/quickstart/#sessions

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def main():
    hello_world()


if __name__ == '__main__':
    main()
