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
        return description

    def get_match_infos(self, search_condition):
        print(self.__name, '为你找到以下最适合的房源: ')
        for info in self.__house_info:
            info.show_info(False)
        return self.__house_info

    def sign_contract(self, house_info, time):
        """与房东签订协议"""
        print(self.__name, '与房东', house_info.get_owner_name(), '签订', house_info.get_address(), '的房子的租聘合同，租期',
              time, '年。合同期内', self.get_name(), '有权对其进行使用和转租')

    def sign_contracts(self, time):
        for info in self.__house_info:
            self.sign_contract(info, time)


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
        self.__house_info = HouseInfo(area, price, has_window, bathroom, kitchen, self.__address, self.__name)

    def publish_house_info(self,agency):
        agency.add_house_info(self.__house_info)
        print(self.get_name() + '在', agency.get_name(), '发布房源出租信息: ')
        self.__house_info.show_info()


class Custom:
    """租房人"""
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def find_house(self, description, agency):
        print('我是' + self.get_name(), ', 我想要找一个' + description + '的房子')
        return agency.get_match_infos(agency.get_search_condition(description))

    def see_house(self, house_infos):
        """去看房，选择最使用的房子"""
        size = len(house_infos)
        return house_infos[size-1]

    def sign_contract(self, house_info, agency, time):
        """与中介签订会议"""
        print(self.__name + '与中介', agency.get_name(), '签订', house_info.get_address(), '的房子的租聘合同',
              '租期', time, '年。合同期内', self.__name, '有权对其进行使用!')


def main():
    agent = HosingAgent('自如')

    zhangsan = HouseOwner('张三', '上地西里')
    zhangsan.set_house_info(20, 2500, 1, '独卫', 0)
    zhangsan.publish_house_info(agent)

    xiaohua = HouseOwner('小华', '西二旗')
    xiaohua.set_house_info(18, 2100, 1, '独卫', 0)
    xiaohua.publish_house_info(agent)

    agent.sign_contracts(10)

    qiangqiang = Custom('小强')
    house_infos = qiangqiang.find_house('18平，独卫, 窗户，朝南', agent)
    houses = qiangqiang.see_house(house_infos)
    qiangqiang.sign_contract(houses, agent, 0)


if __name__ == '__main__':
    main()
