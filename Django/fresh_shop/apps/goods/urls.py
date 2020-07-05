# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :
from django.urls import path, include
from apps.goods.views import IndexView


urlpatterns = [
    path(r'index', IndexView.as_view(), name='Index')
]

