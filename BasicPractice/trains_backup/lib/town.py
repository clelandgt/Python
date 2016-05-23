# -*- coding: utf-8 -*-

class Town:
    visited = False

    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        try:
            return self.name == other.name
        except:
            return False