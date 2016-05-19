# -*- coding: utf-8 -*-

class Station:
    next_station = None

    def __init__(self, from_town, to_town, distance):
        self.origin = from_town
        self.destination = to_town
        self.distance = int(distance)

    def next(self, station):
        self.next_station = station
        return self