from sys import argv
from .house import House
from .battery import Battery
from .cable import Cable


class Data():
    def __init__(self, houses, batteries, cables):
        self.houses = houses
        self.batteries = batteries
        self.cables = cables
        self.cost = 0
    
    def costs(self):
        costs = 0
        for i in self.cables:
            cost = self.cables[i].calculate_price()
            costs += cost
        self.cost = costs
        
        return self.cost

    def add_cables(self):
        cables = {}
        for i in self.houses:
            designated_battery_id = self.houses[i].to_battery
            designated_battery = self.batteries[designated_battery_id]
            cable = Cable(self.houses[i], designated_battery)
            cables[self.houses[i].id] = cable #Key = house.id: Value = Cable
        self.cables = cables
        #data = Data(self.houses, self.batteries, cables)

        return self.cables
    
