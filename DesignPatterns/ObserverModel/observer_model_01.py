# -*- coding: utf-8 -*-
# @File  : observer_model_01.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-10
# @Desc  :
import time


class WaterHeater:
    def __init__(self):
        self.__observers = []
        self.__temperature = 25

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print('current temperature is: ', self.__temperature)
        self.notifies()

    def add_observer(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for item in self.__observers:
            item.update(self)


class Observer:
    """洗澡模式和饮用模式的父类"""
    def update(self, wa):
        pass


class WashingMode(Observer):
    """洗澡: 温度 50~70 """
    def update(self, water_heater):
        if water_heater.get_temperature() >= 50 and water_heater.get_temperature() < 70:
            print("温度刚好，可以洗澡了")


class DrinkingMode(Observer):
    """饮水: 温度 >100"""
    def update(self, water_heater):
        if water_heater.get_temperature() >= 100:
            print("水已烧开，可以喝了")


def main():
    wash = WashingMode()
    drinking = DrinkingMode()
    heater = WaterHeater()
    heater.add_observer(wash)
    heater.add_observer(drinking)

    temperature = 0
    while True:
        time.sleep(0.1)
        temperature += 1
        heater.set_temperature(temperature)
        if temperature >= 200:
            break


if __name__ == '__main__':
    main()
