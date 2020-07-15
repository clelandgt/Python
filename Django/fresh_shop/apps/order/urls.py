# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :

from django.urls import path
from apps.order.views import OrderPlaceView, OrderCommitView, OrderPayView, CheckPayView,CommentView
#
urlpatterns = [
    path('place', OrderPlaceView.as_view(), name='place'),  # 提交订单页面显示
    path('commit', OrderCommitView.as_view(), name='commit'),  # 订单创建
    path('pay', OrderPayView.as_view(), name='pay'),  # 订单支付
    path('check', CheckPayView.as_view(), name='check'),  # 订单支付
    path('comment/(?P<order_id>.+)', CheckPayView.as_view(), name='comment'),  # 订单支付
]