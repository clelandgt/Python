from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django_redis import get_redis_connection

from apps.goods.models import GoodsSKU
from utils.mixin import LoginRequiredMixin


# Create your views here.

# /cart
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


# /cart/add
class CartAddView(View):
    """购物车记录添加"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({
                'res': 0,
                'errmsg': '请登录'
            })

        # 接受数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 数据校验
        if not all([sku_id, count]):
            return JsonResponse({
                'res': 1,
                'errmsg': '数据不完整'
            })

        # 校验添加的商品数量
        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({
                'res': 1,
                'errmsg': '数据不完整'
            })

        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoseNotExist:
            return JsonResponse({
                'res': 3,
                'errmsg': '商品不存在'
            })

        # 业务处理
        conn = get_redis_connection('default')
        cart_key = f'cart_{user.id}'
        cart_count = conn.hget(cart_key, sku_id)
        # 累计购物车中商品的数量
        if cart_count:
            count += int(cart_count)

        # 校验商品的库存
        if count > sku.stock:
            return JsonResponse({
                'res': 4,
                'errmsg': '商品库存不足'
            })
        conn.hset(cart_key, sku_id, count)

        total_count = conn.hlen(cart_key)
        return JsonResponse({
            'res': 5,
            'total': total_count,
            'message': '添加成功'
        })


# /cart/update
class CartUpdateView(View):
    """购物车记录更新"""
    def post(self, request):
        '''购物车记录更新'''
        user = request.user
        if not user.is_authenticated():
            # 用户未登录
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})

        # 接收数据
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')

        # 数据校验
        if not all([sku_id, count]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})

        # 校验添加的商品数量
        try:
            count = int(count)
        except Exception as e:
            # 数目出错
            return JsonResponse({'res': 2, 'errmsg': '商品数目出错'})

        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            # 商品不存在
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})

        # 业务处理:更新购物车记录
        conn = get_redis_connection('default')
        cart_key = 'cart_%d'%user.id

        # 校验商品的库存
        if count > sku.stock:
            return JsonResponse({'res':4, 'errmsg':'商品库存不足'})

        # 更新
        conn.hset(cart_key, sku_id, count)

        # 计算用户购物车中商品的总件数 {'1':5, '2':3}
        total_count = 0
        vals = conn.hvals(cart_key)
        for val in vals:
            total_count += int(val)

        # 返回应答
        return JsonResponse({'res':5, 'total_count':total_count, 'message':'更新成功'})


# /cart/delete
class CartDeleteView(View):
    """购物车记录删除"""
    def post(self, request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({
                'res': 0,
                'errmsg': '清先登录'
            })

        # 接受参数
        sku_id = request.POST.get('sku_id')

        # 数据校验
        if not sku_id:
            return JsonResponse({
                'res': 1,
                'errmsg': '无效的商品id'
            })

        # 校验商品是否存在
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({
                'res': 2,
                'errmsg': '商品不存在'
            })

        # 业务处理
        conn = get_redis_connection('default')
        cart_key = f'cart_{user.id}'
        # 删除hdel
        conn.hdel(cart_key, sku_id)

        total_count = 0
        vals = conn.hvals(cart_key)
        for val in vals:
            total_count += int(val)

        return JsonResponse({
            'res': 3,
            'total_count': total_count,
            'message': '删除成功'
        })

