from sys import argv
from .house import House
from .battery import Battery


class Data():
    def __init__(self, houses, batteries, cables):
        self.houses = houses
        self.batteries = batteries
        self.cables = cables
    
    def costs(self):
        costs = 0
        for i in self.cables:
            cost = self.cables[i].calculate_price()
            costs += cost
        return costs

    
