# -*- coding: utf-8 -*-
# @File  : observer_model_2.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-11
# @Desc  :
import time


class Observable:
    """被观察者基类"""
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def remove_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observer(self, obj):
        for o in self.__observers:
            o.update(self, obj)


class Observer:
    """观察值基类"""
    def update(self, observable, obj):
        pass


class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 20

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temperature):
        self.__temperature = temperature
        print('current temperature: ', temperature)
        self.notify_observer(temperature)


class WashingMode(Observer):
    """洗澡: 温度 50~70 """
    def update(self, water_heater, obj):
        if isinstance(water_heater, WaterHeater) and  water_heater.get_temperature() >= 50 and water_heater.get_temperature() < 70:
            print("温度刚好，可以洗澡了")


class DrinkingMode(Observer):
    """饮水: 温度 >100"""
    def update(self, water_heater, obj):
        if isinstance(water_heater, WaterHeater) and water_heater.get_temperature() >= 100:
            print("水已烧开，可以喝了")


def main():
    wash = WashingMode()
    drinking = DrinkingMode()
    heater = WaterHeater()
    heater.add_observer(wash)
    heater.add_observer(drinking)

    print('加入观察者：WashingMode, DrinkingMode')
    temperature = 0
    while temperature <= 110:
        time.sleep(0.1)
        temperature += 1
        heater.set_temperature(temperature)

    print('Remove观察者：WashingMode')
    heater.remove_observer(wash)
    temperature = 20
    while temperature <= 110:
        time.sleep(0.1)
        temperature += 1
        heater.set_temperature(temperature)




if __name__ == '__main__':
    main()
