# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :
from django.urls import path
from apps.goods.views import IndexView, DetailView, ListView


urlpatterns = [
    path('index', IndexView.as_view(), name='index'),  # 首页
    path('goods/(?P<goods_id>\d+)', DetailView.as_view(), name='detail'),  # 详情页
    path('list/(?P<type_id>\d+)/(?P<page>\d+)', ListView.as_view(), name='list')  # 列表页

]