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
        print(self.__name, '申请请假', request.get_dayoff(), "天。请假事由", request.get_reason())
        if (self.__leader is not None):
            self.__leader.handle_request(request)


class Supervisor(Responsible):
    """主管"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, request):
        if (request.get_dayoff() <= 2):
            print("同意", request.get_name(), "请假，签字人: ", self.get_name(), "(", self.get_title(), ")")
        next_handle = self.get_next_handler()
        if(next_handle is not None):
            next_handle.handle_request(request)


class DepermentManager(Responsible):
    """部门总监"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, request):
        if (request.get_dayoff() > 2 and request.get_dayoff() <= 5):
            print("同意", request.get_name(), "请假，签字人: ", self.get_name(), "(", self.get_title(), ")")
        next_handle = self.get_next_handler()
        if(next_handle is not None):
            next_handle.handle_request(request)


class CEO(Responsible):
    """CEO"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, request):
        if (request.get_dayoff() > 5):
            print("同意", request.get_name(), "请假，签字人: ", self.get_name(), "(", self.get_title(), ")")
        next_handle = self.get_next_handler()
        if(next_handle is not None):
            next_handle.handle_request(request)


class Administrator(Responsible):
    """行政人员"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handle_request(self, request):
        print(request.get_name(), '的请假申请已审核，情况属实！已备案处理。处理人: ', self.get_name())
        next_handle = self.get_next_handler()


def main():
    direct_leader = Supervisor("Eren", "客户端研发经理")
    deperment_leader = DepermentManager("Eric", "技术研发中心总监")
    ceo = CEO("Helen", "创新文化公司CEO")
    administrator = Administrator("Nina", "行政中心总监")
    direct_leader.set_next_handler(deperment_leader)
    deperment_leader.set_next_handler(ceo)
    ceo.set_next_handler(administrator)

    sunny = Person('sunny')
    sunny.set_leader(direct_leader)
    sunny.send_request(Request(sunny.get_name(), 1, '参加MDCC大会'))

    tony = Person('tony')
    tony.set_leader(direct_leader)
    tony.send_request(Request(tony.get_name(), 5, '家里有急事'))

    xiaohua = Person('xiaohua')
    xiaohua.set_leader(direct_leader)
    tony.send_request(Request(xiaohua.get_name(), 15, '出国旅游'))

if __name__ == '__main__':
    main()
