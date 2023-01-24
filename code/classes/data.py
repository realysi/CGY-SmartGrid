from sys import argv
from .house import House
from .battery import Battery
from .cable import Cable
from typing import Dict, List, Tuple
import copy


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
    
    def overlay(self):
        for i in range(1,6):
            tempory_list = []
            flat_tempory_list = []
            mini_list_cables = []
            list_cables = []
            for j in self.cables:
                if self.cables[j].battery.id == i:
                    tempory_list.append(self.cables[j].segments)
                    #print(self.cables[j].segments)

            length = len(tempory_list)
            for a in range(length):
                length_sublist = len(tempory_list[a])
                for b in range(length_sublist):
                    flat_tempory_list.append(tempory_list[a][b])

            length_flat = len(flat_tempory_list)
            for h in range(length_flat):
                mini_list_cables.append(flat_tempory_list[h])
                if len(mini_list_cables) == 2:
                    #a = flat_tempory_list.count(mini_list_cables)
                    mini_deepcopy = copy.deepcopy(mini_list_cables)
                    #print(mini_list_cables)
                    list_cables.append(mini_deepcopy)
                    mini_list_cables.pop(0)

            length_list_cables = len(list_cables)
            for k in range(length_list_cables):
                a = list_cables.count(list_cables[k]) #alleen kabels in dezelfde richting deelt nu
                kopie = copy.deepcopy(list_cables[k])
                new_kopie = [kopie[1], kopie[0]]
                b = list_cables.count(new_kopie) # nu beide richtingen
                totaal = a + b
                print(list_cables[k])
                print(totaal)
                if totaal > 1:
                    overlay = True
                #print(totaal)


    
