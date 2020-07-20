# -*- coding: utf-8 -*-
# @File  : state_pattern_01.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-20
# @Desc  :


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


class Water:
    """水"""

    def __init__(self, state):
        self.__state = state
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        if self.__temperature <= 0:
            self.change_state(SolidState('固态'))
        elif self.__temperature <= 100:
            self.change_state(LiquidState('液态'))
        else:
            self.change_state(GaseousState('气态'))

    def set_state(self, state):
        self.__state = state

    def change_state(self, state):
        if self.__state is None:
            print('初始化为: ', state.get_state_name())
        else:
            print('由', self.__state.get_state_name(), '变为', state.get_state_name())
        self.__state = state

    def add_temperature(self, temperature):
        self.set_temperature(self.get_temperature() + temperature)

    def sub_temperature(self, temperature):
        self.set_temperature(self.get_temperature() - temperature)

    def behavior(self):
        self.__state.behavior(self)


def main():
    water = Water(LiquidState('液态'))
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.add_temperature(10)
    water.behavior()
    water.sub_temperature(50)
    water.behavior()
    water.add_temperature(200)
    water.behavior()


if __name__ == '__main__':
    main()
