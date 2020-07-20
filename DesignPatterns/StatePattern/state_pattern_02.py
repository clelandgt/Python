# -*- coding: utf-8 -*-
# @File  : state_pattern_02.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-20
# @Desc  :


class Context:
    """状态模式的上下文环境类"""
    def __init__(self):
        self.__states = []
        self.__cur_state = None
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)

    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print('初始化为: ', state.get_state_name())
        else:
            print('由', self.__cur_state.get_state_name(), '变为', state.get_state_name())
        self.__cur_state = state
        self.add_state(state)
        return True

    def get_state(self):
        return self.__cur_state

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def _get_state_info(self):
        return self.__state_info


class State:
    """状态基类"""
    def __init__(self, name):
        self.__name = name

    def get_state_name(self):
        return self.__name

    def is_match(self, state_info):
        """状态信息stateinfo是否在当前状态范围内"""
        return False

    def behavior(self, context):
        pass


class Water(Context):
    def __init__(self):
        super().__init__()
        self.add_state(SolidState('固态'))
        self.add_state(LiquidState('液态'))
        self.add_state(GaseousState('气态'))
        self.set_temperature(25)

    def get_temperature(self):
        return self._get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def add_temperature(self, steps):
        self._set_state_info(self.get_temperature() + steps)

    def sub_temperature(self, steps):
        self._set_state_info(self.get_temperature() - steps)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


# 单例装饰器
def singleton(cls, *args, **kwargs):
    # 构造一个单例装饰器
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton


@singleton
class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info < 0

    def behavior(self, context):
        if isinstance(context, Water):
            print("我性格高冷，当前体温", context.get_temperature(),
                  "摄氏度，我坚如钢铁，彷如一冷血动物，请用我砸人，嘿嘿....")


@singleton
class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return (state_info >= 0 and state_info < 0)

    def behavior(self, context):
        if isinstance(context, Water):
            print("我性格温和，当前体温", context.get_temperature(),
                  "摄氏度，我可滋润万物，饮用我可让你活力倍增....")


@singleton
class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info):
        return state_info > 1000

    def behavior(self, context):
        if isinstance(context, Water):
            print("我性格热烈，当前体温", context.get_temperature(),
                  "摄氏度，飞向天空是我毕生的梦想，在这你将看不到我的存在，我将达到无我的境界....")


def main():
    water = Water()
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

