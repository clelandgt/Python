# -*- coding: utf-8 -*-
# @File  : Person.py
# @Author: clelandgt@163.com
# @Date  : 2020-10-28
# @Desc  :

from copy import copy, deepcopy


class Person:
    """人"""
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__pet_list = []

    def show_my_self(self):
        print('我是' + self.__name + '. 年龄' + str(self.__age) + '. 我养了这些宠物')
        for pet in self.__pet_list:
            print(pet + '\t', end='')
        print()

    def add_pet(self, pet):
        self.__pet_list.append(pet)

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


def test_proto_type2():
    tony = Person('Tony', 26)
    tony.add_pet('小狗CoCo')
    print('父本tony: ', end='')
    tony.show_my_self()

    tony1 = tony.deep_clone()
    tony1.add_pet('小猫Amy')
    print('副本tony1: ', end='')
    tony1.show_my_self()
    print('父本tony: ', end='')
    tony.show_my_self()

    tony2 = tony.clone()
    tony2.add_pet('小兔Ricky')
    print('副本tony2: ', end='')
    tony2.show_my_self()
    print('父本tony: ', end='')
    tony.show_my_self()


if __name__ == '__main__':
    test_proto_type2()
