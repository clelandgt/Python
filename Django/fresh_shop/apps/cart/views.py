from django.shortcuts import render
from django.views.generic import View
from django_redis import get_redis_connection

from apps.goods.models import GoodsSKU
from utils.mixin import LoginRequiredMixin


# Create your views here.


class CardInfoView(LoginRequiredMixin, View):
    """购物车页面显示"""
    def get(self, request):
        user = request.user

        # 获取用户购物车中的商品信息
        conn = get_redis_connection('default')
        cart_key = f'cart_{user.id}'
        cart_dict = conn.hgetall(cart_key)
        skus = []

        # 保存用户购物车中的商品的总数目和总价格
        total_count = 0
        total_price = 0
        # 遍历商品信息
        for sku_id, count in cart_dict.items():
            sku = GoodsSKU.objects.get(id=sku_id)
            amount = sku.price * int(count)
            sku.amount = amount
            sku.count = count
            skus.append((sku))

            total_count += int(count)
            total_price += amount

        # 填充上下文
        context = {
            'total_count': total_count,
            'total_price': total_price,
            'skus': skus
        }
        return render(request, 'cart.html', context)
