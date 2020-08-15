# -*- coding: utf-8 -*-
# @File  : computer.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-15
# @Desc  :


class Component:
    """配件，所有子配件的基类"""

    def __init__(self, name):
        self._name = name

    def show_info(self, indent=''):
        pass

    def is_composite(self):
        return False

    def startup(self, indent=''):
        print(indent + self._name + ' 准备开始工作...')

    def shutdown(self, indent=''):
        print(indent + self._name + ' 即将结束工作...')


class CPU(Component):
    """中央处理器"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('CPU: ' + self._name + ', 可以高速计算。')


class MemoryCard(Component):
    """内存条"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('内存条: ' + self._name + ', 可以缓冲数据，读写速度快。')


class HardDisk(Component):
    """硬盘"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('硬盘: ' + self._name + ', 可以永久存储数据，容量大。')


class GraphicsCard(Component):
    """显卡"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('显卡: ' + self._name + ', 可以高速计算和处理图形图像。')


class Battery(Component):
    """电源"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('电源: ' + self._name + ', 可以持续给主板和外接配件供电。')


class Fan(Component):
    """风扇"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('风扇: ' + self._name + ', 辅助CPU降热。')


class Displayer(Component):
    """显示器"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent, end='')
        print('风扇: ' + self._name + ', 负责内容的显示。')


class Composite(Component):
    """配件组合器"""
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def show_info(self, indent):
        print(self._name + ', 由以下部件组成:')
        indent += '\t'
        for element in self._components:
            element.show_info(indent)

    def is_composite(self):
        return True

    def add_component(self, component):
        self._components.append(component)

    def remove_component(self, component):
        self._components.remove(component)

    def startup(self, indent):
        super().startup(indent)
        indent += '\t'
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent):
        super().shutdown(indent)
        indent += '\t'
        for element in self._components:
            element.shutdown(indent)


class MainBoard(Composite):
    """主板"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent + '主板: ', end='')
        super().show_info(indent)


class ComputeCase(Composite):
    """机箱"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent + '机箱: ', end='')
        super().show_info(indent)


class Computer(Composite):
    """电脑"""
    def __init__(self, name):
        super().__init__(name)

    def show_info(self, indent):
        print(indent + '电脑: ', end='')
        super().show_info(indent)


def main():
    cpu = CPU('Inter Core i5-6600K')
    memory_card = MemoryCard('Kingston Fury DDR4')
    hard_disk = HardDisk('Kingston V300')
    graphics_card = GraphicsCard('Colorful iGame750')
    main_board = MainBoard('GIGABYTE Z170M M-ATX')
    main_board.add_component(cpu)
    main_board.add_component(memory_card)
    main_board.add_component(hard_disk)
    main_board.add_component(graphics_card)

    battery = Battery('Antec VP 450P')
    fan = Fan('DEEPCOOL 120T')
    computer_case = ComputeCase('SAMA MATX')
    computer_case.add_component(battery)
    computer_case.add_component(fan)
    computer_case.add_component(main_board)

    displayer = Displayer('AOC LV243')
    computer = Computer('Tony DIY电脑')
    computer.add_component(displayer)
    computer.add_component(computer_case)

    computer.show_info('')
    print('\n开机过程')
    computer.startup('')
    print('\n关机过程')
    computer.shutdown('')


if __name__ == '__main__':
    main()
