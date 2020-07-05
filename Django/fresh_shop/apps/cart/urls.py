# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :

from django.urls import path, include
from apps.cart.views import CardInfoView


urlpatterns = [
    path(r'', CardInfoView.as_view(), name='show')  # 购物车页面显示
]