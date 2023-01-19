from sys import argv
from .house import House
from .battery import Battery
from .cable import Cable
from typing import Dict, List, Tuple


class Data():
    def __init__(self, houses: Dict[int, House], batteries: Dict[int, Battery]) -> None:
        self.houses = houses
        self.batteries = batteries
        self.cables: Dict[int, Cable] = {} # Dict containing house_id and Cable object
        self.cost = 0
        self.score = 0
    
    # Returns total cost of all cables for one solution
    def cables_cost(self) -> int:
        for house_id in self.cables:
            self.cost += self.cables[house_id].calculate_price()
        return self.cost

    # 
    def add_cables(self):
        for house_id in self.houses:
            # Gives battery object connected to given house
            connected_battery: Battery = self.batteries[self.houses[house_id].to_battery]

            # Creates Cable object given a house and connected battery
            cable: Cable = Cable(self.houses[house_id], connected_battery)
            self.cables[house_id] = cable
            
        return self.cables
    
