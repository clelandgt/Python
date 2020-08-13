# -*- coding: utf-8 -*-
# @File  : GameCommand.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-13
# @Desc  :
from abc import ABCMeta, abstractmethod

STEP = 5


class GameRole:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def left_move(self):
        self.__x -= STEP

    def right_move(self):
        self.__x += STEP

    def up_move(self):
        self.__y += STEP

    def down_move(self):
        self.__y -= STEP

    def jump_move(self):
        self.__z += STEP

    def squat_move(self):
        self.__z -= STEP

    def attack(self):
        print('攻击')

    def show_position(self):
        print('x: ' + self.__x + ', y: ' + self.__y + ', z:' + self.__z)


class GameCommand(metaclass=ABCMeta):
    """游戏角色的命令类"""
    def __init__(self, role):
        self.__role = role

    def set_role(self, role):
        self.__role = role

    @abstractmethod
    def execute(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
