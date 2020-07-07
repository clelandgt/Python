# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-05
# @Desc  :

from django.urls import path
from apps.order.views import OrderPlaceView
#
urlpatterns = [
    path('place', OrderPlaceView.as_view(), name='place'),  # 提交订单页面显示

]