# -*- coding: utf-8 -*-
# @File  : orders.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-11
# @Desc  :
from abc import  ABCMeta, abstractmethod
# 引入ABCMeta和abstractmethod来定义抽象类和抽象方法


class Chef:
    """厨师"""
    def steam_food(self, original_material):
        print(original_material + '清蒸中...')
        return '清蒸' + original_material

    def stir_fried_food(self, original_material):
        print(original_material + '爆炒中')
        return '爆炒' + original_material


class Order(metaclass=ABCMeta):
    """订单"""
    def __init__(self, name, original_material):
        self._chef = Chef()
        self._name = name
        self._original_material = original_material

    def get_display_name(self):
        return self._name + self._original_material

    @abstractmethod
    def processing_order(self):
        pass


class SteameOrder(Order):
    """清蒸"""
    def __init__(self, original_material):
        super().__init__('清蒸', original_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.steam_food(self._original_material)
        return ''


class SpicyOrder(Order):
    """香辣炒"""
    def __init__(self, original_material):
        super().__init__('香辣', original_material)

    def processing_order(self):
        if self._chef is not None:
            return self._chef.stir_fried_food(self._original_material)
        return ''


class Waiter:
    """服务员"""
    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receive_order(self, order):
        self.__order = order
        print('服务员' + self.__name  + ': 您的' + order.get_display_name() + '订单已收到')

    def place_order(self):
        food = self.__order.processing_order()
        print('服务员' + self.__name + ': 您的餐' + food  + '订单已准备好，请您慢用!')


def main():
    waiter = Waiter('小华')
    steam_order = SteameOrder('小鸡')
    print('客户Davoid：我要一份' + steam_order.get_display_name())
    waiter.receive_order(steam_order)
    waiter.place_order()
    print()

    spic_order = SpicyOrder('毛肚')
    print('客户Tom: 我要一份' + spic_order.get_display_name())
    waiter.receive_order(spic_order)
    waiter.place_order()
    print()


if __name__ ==  '__main__':
    main()
