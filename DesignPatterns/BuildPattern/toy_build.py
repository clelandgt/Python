# -*- coding: utf-8 -*-
# @File  : toy_build.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-27
# @Desc  :


class Toy:
    """玩具"""
    def __init__(self, name):
        self._name = name
        self.__components = []

    def get_name(self):
        return self._name

    def add_component(self, component, count=1, unit='个'):
        self.__components.append([component, count, unit])

    def feature(self):
        pass


class Car(Toy):
    """小车"""
    def feature(self):
        print('我是' + self._name, ', 我可以快速奔跑...')


