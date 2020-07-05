# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :
from django.urls import path
from apps.goods.views import IndexView


urlpatterns = [
    path('index', IndexView.as_view(), name='index')
]