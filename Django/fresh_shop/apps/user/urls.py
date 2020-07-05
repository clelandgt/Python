# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-04
# @Desc  :
from django.urls import path, include
from apps.user.views import LoginView, LogoutView, UserInfoView, UserOrderView


urlpatterns = [
    # path(r'^register$', name='register'),
    # path(r'^active/(?P<token>.*)$', name='active'),
    path(r'login', LoginView.as_view(), name='login'),
    path(r'^logout$', LogoutView.as_view(), name='logout'),

    path(r'', UserInfoView.as_view(), name='user'),
    path(r'order/(?P<page>\d+)', UserOrderView.as_view(), name='order')
]
