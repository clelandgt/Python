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
        super().__init__(name)
        self.__phone_num = phone_num

    def get_phone_num(self):
        return self.__phone_num

    def receive(self, parcel_content):
        print("货物主人: " + self.get_name(), "手机号: " + self.get_phone_num())
        print('接收到一个包裹，包裹内容: ' + parcel_content)


class ProxyReceive(ReceiveParcel):
    """代理主题"""
    def __init__(self, name, receiver):
        super().__init__(name)
        self.__receiver = receiver

    def receive(self, parcel_content):
        self.pre_receive()
        if(self.__receiver is not None):
            self.__receiver.receive(parcel_content)
        self.after_receive()

    def pre_receive(self):
        print('我是' + self.__receiver.get_name() + '的朋友，我来帮他代收快递!')

    def after_receive(self):
        print('代收人: ' + self.get_name())


def main():
    tony = RealReceive('Tony', '18512345678')
    tom = ProxyReceive('Tom', tony)
    tom.receive('雨伞')


if __name__ == '__main__':
    main()
