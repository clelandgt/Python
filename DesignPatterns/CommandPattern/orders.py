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


def main():
    pass


if __name__ ==  '__main__':
    main()
