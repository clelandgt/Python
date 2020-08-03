# -*- coding: utf-8 -*-
# @File  : coffee.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-03
# @Desc  :


class Coffee:
    """咖啡"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_teste(self):
        pass


class CaffeeLatte(Coffee):
    """拿铁咖啡"""
    def __init__(self, name):
        super().__init__(name)

    def get_teste(self):
        return '轻柔而香醇'


class MochaCoffee(Coffee):
    """摩卡咖啡"""
    def __init__(self, name):
        super().__init__(name)

    def get_teste(self):
        return '丝滑与醇厚'


class CoffeeMaker:
    """咖啡机"""

    @staticmethod
    def mark_coffee(coffee_bean):
        if coffee_bean == '拿铁风味咖啡豆':
            coffee = CaffeeLatte('拿铁咖啡')
        elif coffee_bean == '摩卡风味咖啡豆':
            coffee = MochaCoffee('摩卡咖啡')
        else:
            coffee = Coffee()
        return coffee


def main():
    latte = CoffeeMaker.mark_coffee('拿铁风味咖啡豆')
    print(latte.get_name() + '已为您准备好了，口感: ' + latte.get_teste() + '请慢慢享用!')
    mocha = CoffeeMaker.mark_coffee('摩卡风味咖啡豆')
    print(mocha.get_name() + '已为您准备好了，口感: ' + mocha.get_teste() + '请慢慢享用!')


if __name__ == '__main__':
    main()
