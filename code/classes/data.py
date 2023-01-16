from sys import argv
from .house import House
from .battery import Battery


class Data():
    def __init__(self, houses, batteries):
        self.houses = houses
        self.batteries = batteries
        self.cables = None

