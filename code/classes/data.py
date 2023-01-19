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
        self.total_cable_length = 0
    
    # Returns total cost of all cables for one solution
    def cables_cost(self) -> int:
        for house_id in self.cables:
            cost_cable = self.cables[house_id].cost
            self.cost += cost_cable

        self.total_cable_length = float(self.cost / 9)
        return self.cost

    # Adds cables to dictionary 
    def add_cables(self):
        for house_id in self.houses:
            # Gives battery object connected to given house
            connected_battery: Battery = self.batteries[self.houses[house_id].to_battery]

            # Creates Cable object given a house and connected battery
            cable: Cable = Cable(self.houses[house_id], connected_battery)
            
            self.cables[house_id] = cable

            #for house_id in self.cables: 
            self.cables[house_id].calculate_segments()
            self.cables[house_id].calculate_distance()
            self.cables[house_id].calculate_cost()

        return self.cables
    
