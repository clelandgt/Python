# -*- coding: utf-8 -*-
# @File  : singleton_model_01.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-15
# @Desc  :


class Singleton1(object):
    """单例的实现方式"""
    __instance = None
    __is_first_init = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__is_first_init:
            self.__name = name
            Singleton1.__is_first_init = True

    def get_name(self):
        return self.__name


def main():
    tony = Singleton1('Tony')
    karry = Singleton1('Karry')
    print(tony.get_name(), karry.get_name())
    print(f'id(tony): {id(tony)}', f'id(karry): {id(karry)}')


if __name__ == '__main__':
    main()
