# -*- coding: utf-8 -*-
# @File  : ask_for_leave.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-28
# @Desc  :


class Request:
    """请求内容"""

    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__lead = None

    def get_name(self):
        return self.__name

    def get_dayoff(self):
        return self.__dayoff

    def get_reason(self):
        return self.__reason


class Responsible:
    """责任人抽象类"""

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self.__next_handle = None

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def get_next_handler(self):
        return self.__next_handle

    def set_next_handler(self, next_handle):
        self.__next_handle = next_handle

    def handle_request(self, request):
        pass


class Person:
    """请求者"""
    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_leader(self, leader):
        self.__leader = leader

    def get_leader(self):
        return self.__leader

    def send_request(self, request):
        pass


class Supervisor(Responsible):
    """主管"""
    pass


class DepermentManager(Responsible):
    """部门总监"""
    pass


class CEO(Responsible):
    """CEO"""
    pass


class Administrator(Responsible):
    """行政人员"""
    pass


def main():
    pass


if __name__ == '__main__':
    main()
