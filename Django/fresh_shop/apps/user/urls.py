# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-04
# @Desc  :
from django.urls import path
from apps.user.views import LoginView, LogoutView, UserInfoView, UserOrderView, RegisterView, ActiveView, AddressView


urlpatterns = [
    path('register',  RegisterView.as_view(), name='register'),
    path('active/(?P<token>.*)',  ActiveView.as_view(), name='active'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),

    path('', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    path('order/(?P<page>\d+)', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    path('address', AddressView.as_view(), name='address') # 用户中心-地址页

]
