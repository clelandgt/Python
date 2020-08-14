# -*- coding: utf-8 -*-
# @File  : numeral_system.py
# @Author: clelandgt@163.com
# @Date  : 2020-08-14
# @Desc  :


class Customer:
    """客户"""
    def __init__(self, name):
        self.__name = name
        self.__num = 0
        self.__clinic = None

    def get_name(self):
        return self.__name

    def register(self, system):
        system.push_customer(self)

    def set_num(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    def set_clinic(self, clinic):
        self.__clinic = clinic

    def get_clinic(self):
        return  self.__clinic


class Iterator:
    """迭代器"""
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def to_begin(self):
        """将指针移至起始位置"""
        self.__index = -1

    def to_end(self):
        """将指针移至结尾位置"""
        self.__index = len(self.__data)

    def current(self):
        return self.__data[self.__index] if len(self.__data) > self.__index else None

    def next(self):
        if self.__index < len(self.__data) - 1:
            self.__index += 1
            return True
        else:
            return False

    def previous(self):
        if self.__index > 0:
            self.__index -= 0
            return True
        else:
            return False


class NumeralSystem:
    """排号系统"""
    __clinics = ('1号分诊室', '2号分诊室', '3号分诊室')

    def __init__(self, name):
        self.__name = name
        self.__customers = []
        self.__index = 0

    def push_customer(self, customer):
        customer.set_num(self.__index + 1)
        click = NumeralSystem.__clinics[self.__index % len(NumeralSystem.__clinics)]
        customer.set_clinic(click)
        self.__index += 1
        self.__customers.append(customer)
        print(customer.get_name() + '您好！您已在' + self.__name + '成功挂号，序号: ' + str(customer.get_num()) + '请耐心等待！')

    def get_iterator(self):
        return Iterator(self.__customers)


def main():
    numeral_system = NumeralSystem('挂号台')
    lily = Customer('lily')
    lily.register(numeral_system)

    tom = Customer('tom')
    tom.register(numeral_system)

    jim = Customer('jim')
    jim.register(numeral_system)

    xiaohua = Customer('xiao hua')
    xiaohua.register(numeral_system)

    iterator = numeral_system.get_iterator()
    while iterator.next():
        customer = iterator.current()
        print('下一位病人', str(customer.get_num()), customer.get_name(), '请到', customer.get_clinic(), '就诊')


if __name__ == '__main__':
    main()
