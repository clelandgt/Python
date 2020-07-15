# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :

from django.urls import path
from apps.cart.views import CardInfoView, CartAddView, CartUpdateView, CartDeleteView


urlpatterns = [
    path('', CardInfoView.as_view(), name='show'),  # 购物车页面显示
    path('add', CartAddView.as_view(), name='add'),  # 购物车记录添加
    path('update', CartUpdateView.as_view(), name='update'),  # 购物车记录更新
    path('delete', CartDeleteView.as_view(), name='delete'),  # 购物车记录删除
]