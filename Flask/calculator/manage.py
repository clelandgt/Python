# -*- coding: utf-8 -*-
# @File  : manage.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-02
# @Desc  :
# 导入模块 flask_cors, flask_bootstrap


from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', debug=True, port=8080)
