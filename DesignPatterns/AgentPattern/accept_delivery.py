# -*- coding: utf-8 -*-
# @File  : accept_delivery.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-02
# @Desc  :


class ReceiveParcel:
    """主题接口"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def receive(self, parcel_content):
        pass


class RealReceive(ReceiveParcel):
    """主题"""
    def __init__(self, name, phone_num):
        self.__name = name
        self.__phone_num = phone_num

    def get_phone_num(self):
        return self.__phone_num

    def receive(self, parcel_content):
        print("货物主人: " + self.get_name(), "手机号: " + self.get_phone_num())
        print('接收到一个包裹，包裹内容: ' + parcel_content)


class ProxyReceive(RealReceive):
    """代理主题"""
    pass



def main():
    pass


if __name__ == '__main__':
    main()
