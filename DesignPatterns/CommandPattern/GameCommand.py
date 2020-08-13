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


class Left(GameCommand):
    """左移命令"""
    def execute(self):
        self.__role.left_move()
        self.__role.show_position()


class Right(GameCommand):
    """右移命令"""
    def execute(self):
        self.__role.right_move()
        self.__role.show_position()


class Up(GameCommand):
    """上移命令"""
    def execute(self):
        self.__role.up_move()
        self.__role.show_position()


class Down(GameCommand):
    """下移命令"""
    def execute(self):
        self.__role.down_move()
        self.__role.show_position()


class Jump(GameCommand):
    """上跳命令"""
    def execute(self):
        self.__role.jump_move()
        self.__role.show_position()


class Squat(GameCommand):
    """下蹲命令"""
    def execute(self):
        self.__role.squat_move()
        self.__role.show_position()


class Attack(GameCommand):
    """攻击命令"""
    def execute(self):
        self.__role.attack()
        self.__role.show_position()


class MacroCommand(GameCommand):
    def __init__(self, role=None):
        super().__init__(role)
        self.commands = []

    def add_command(self,command):
        self.commands.append(command)

    def remove_command(self, command):
        self.commands.remove(command)

    def execute(self):
        for command in self.commands:
            command.excute()


class GameInvoker:
    def __init__(self):
        self.__command = None

    def set_command(self, command):
        self.__command = command
        return self

    def action(self):
        if self.__command is not None:
            self.__command.action()


def main():
    pass


if __name__ == '__main__':
    main()
