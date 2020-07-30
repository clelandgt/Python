# -*- coding: utf-8 -*-
# @File  : rent_house.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-30
# @Desc  :


class HouseInfo:
    """房源信息"""
    def __init__(self, area, price, has_window, bathroom, kitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__has_window = has_window
        self.__bathroom = bathroom
        self.__kitchen = kitchen
        self.__address = address
        self.__owner = owner

    def get_address(self):
        return self.__address

    def get_owner_name(self):
        return self.__owner

    def show_info(self, is_show_owner=True):
        print('面积: ' + str(self.__area) + '平米',
              '价格: ' + str(self.__price) + '元',
              '窗户: ' + ('有' if self.__has_window else '没有'),
              '卫生间: ' + str(self.__bathroom),
              '厨房: ' + ('有' if self.__kitchen else '没有'),
              '地址: ' + str(self.__address),
              '房东: ' + self.__owner if is_show_owner else ''
            )


class HosingAgent:
    """房屋中介"""
    def __init__(self, name):
        self.__name = name
        self.__house_info = []

    def get_name(self):
        return self.__name

    def add_house_info(self, house):
        self.__house_info.append(house)

    def remove_house_info(self, house):
        for item in self.__house_info:
            if item == house:
                self.__house_info.remove(item)

    def get_search_condition(self, description):
        pass

    def get_match_infos(self, search_condition):
        pass

    def sign_contract(self, house_info, time):
        pass

    def sign_contracts(self, time):
        pass


class HouseOwner:
    """房东"""
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__house_info = None

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_house_info(self, area, price, has_window, bathroom, kitchen):
        def __init__(self, area, price, has_window, bathroom, kitchen, address, owner):
        self.__house_info = HouseInfo(area, has_window, bathroom, kitchen)


class Custom:
    pass


def main():
    pass
    # 1.初始化中介
    # 2.初始化3个房源
    # 3. 租房


if __name__ == '__main__':
    main()
