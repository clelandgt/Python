# -*- coding: utf-8 -*-
# @File  : adapter_model_01.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-13
# @Desc  :


class IHightPerson:
    """接口类，提供空实现的方法，由子类实现"""

    def get_name(self):
        """获取姓名"""
        pass

    def get_height(self):
        """获取身高"""
        pass


class HightPerson(IHightPerson):
    """个高的人"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_height(self):
        return 170


class ShortPerson:
    """个矮的人"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_real_height(self):
        return 160

    def get_shoes_height(self):
        return 6


class DecoratePerson(ShortPerson, IHightPerson):
    """有高跟鞋搭配的人"""

    def get_height(self):
        return super().get_real_height() + super().get_shoes_height()


def can_play_receptionise(person):
    return person.get_height() >= 165


def main():
    lira = HightPerson('Lira')
    print(lira.get_name() + '身高' + str(lira.get_height()) + ', 完美如你，天生的美女！')
    print('是否适合做接待员：', '符合' if can_play_receptionise(lira) else '不符合')
    print()

    demi = DecoratePerson('Demi')
    print(demi.get_name() + '身高' + str(demi.get_height()) + '在高跟鞋的适配下，你身上不输高圆圆，气质不输范冰冰！')
    print('是否适合做接待员：', '符合' if can_play_receptionise(demi) else '不符合')


if __name__ == '__main__':
    main()
