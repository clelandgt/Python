# -*- coding: utf-8 -*-
# @File  : views.py
# @Author: clelandgt@163.com
# @Date  : 2020-06-02
# @Desc  :

from . import calc
from flask import render_template, request
import re


@calc.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# 返回计算结果的API
@calc.route('/api/getresult', methods=['POST'])
def get_calc_result():
    data = request.get_json()
    expr_val = data['expr']
    return str(eval(expr_val))

