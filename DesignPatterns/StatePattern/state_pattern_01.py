# -*- coding: utf-8 -*-
# @File  : state_pattern_01.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-20
# @Desc  :


class Water:
    """水"""

    def __init__(self):
        pass


class State:
    """状态"""
    def __init__(self, name):
        self.__name = name

    def get_state_name(self):
        return self.__name

    def behavior(self, water):
        pass


class SolidState(State):
    """固态"""
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格高冷，当前体温", water.get_temperature(),
              "摄氏度，我坚如钢铁，彷如一冷血动物，请用我砸人，嘿嘿....")


class LiquidState(State):
    """液态"""
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格温和，当前体温", water.get_temperature(),
              "摄氏度，我可滋润万物，饮用我可让你活力倍增....")


class GaseousState(State):
    """气态"""
    def __init__(self, name):
        super().__init__(name)

    def behavior(self, water):
        print("我性格热烈，当前体温", water.get_temperature(),
              "摄氏度，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界....")



def main():
    pass


if __name__ == '__main__':
    main()
