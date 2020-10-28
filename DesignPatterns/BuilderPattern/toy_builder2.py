# -*- coding: utf-8 -*-
# @File  : toy_builder2.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-28
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
        print((self._name + '增加了' + str(count) + unit + component))

    def feature(self):
        pass


class Car(Toy):
    """小车"""
    def feature(self):
        print('我是' + self._name, ', 我可以快速奔跑...')


class Manor(Toy):
    """庄园"""
    def feature(self):
        print('我是' + self._name, ', 我可供观赏，也可用来游玩!...')


class ToyBuilder:
    """玩具构建类"""
    def build_product(self):
        pass


class CarBuilder(ToyBuilder):
    """车的构建类"""

    def build_product(self):
        car = Car('迷你小车')
        print('正在构建' + car.get_name() + '...')
        car.add_component('轮子', 4)
        car.add_component('车身')
        car.add_component('发动机')
        car.add_component('方向盘')
        return car


class ManorBuilder(ToyBuilder):
    """庄园的构建类"""
    def build_product(self):
        manor = Manor('淘淘小庄园')
        print('正在构建' + manor.get_name() + '...')
        manor.add_component('客厅', 1, '间')
        manor.add_component('卧室', 2, '间')
        manor.add_component('卫生间', 1, '间')
        manor.add_component('厨房', 1, '间')
        manor.add_component('阳台', 1, '间')
        return manor


class BuilderMgr:
    """构建类的管理类"""
    def __init__(self):
        self.__carBuilder = CarBuilder()
        self.__manorBuilder = ManorBuilder()

    def build_car(self, num):
        count = 0
        product = []
        for i in range(num):
            car = self.__carBuilder.build_product()
            product.append(car)
            count += 1
            print('建造完成第 ' + str(count) + '辆' + car.get_name())
        return product

    def build_manor(self, num):
        count = 0
        product = []
        for i in range(num):
            manor = self.__manorBuilder.build_product()
            product.append(manor)
            count += 1
            print('建造完成第 ' + str(count) + '个' + manor.get_name())
        return product


def test_builder():
    bui = BuilderMgr()
    bui.build_manor(2)
    print()
    bui.build_car(5)


if __name__ == '__main__':
    test_builder()
