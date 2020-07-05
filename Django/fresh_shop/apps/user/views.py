from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.views.generic import View

# Create your views here.


# /user/login
class LoginView(View):
    """登录"""
    def get(self, request):
        """显示登录页面"""
        if 'user_name' in request.COOKIES:
            username = request.COOKIES.get('user_name')
            checked = 'checked'
        else:
            username = ''
            checked = ''
        return render(request, 'login.html', {'username': username, 'checked': checked})

    def post(self, request):
        """登录校验"""
        username = request.POST.get('username')
        password = request.POST.get('pwd')

        # 校验数据
        if not all([username, password]):
            return render(request, 'login.html', {'errmsg': '数据不完整'})

        # 业务处理: 登录校验
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # 用户已激活
                login(request, user)
                next_url = request.GET.get('next', reversed('goods:index'))
                response = redirect(next_url)

                # 判断是够需要记住用户名
                remember = request.POST.get('remember')
                if remember == 'on':
                    # 有效期一周
                    response.set_cookie('username', username, max_age=7*24*3600)
                else:
                    response.delete_cookie('username')
            else:
                # 用户未激活
                return render(request, 'login.html', {'errmsg':'账户未激活'})
        else:
            # 用户名和密码错误
            return render(request, 'login.html', {'errmsg': '用户名或密码错误'})
