from .house import House
from .battery import Battery
from .cable import Cable
from typing import Dict
import copy


class Data:
    def __init__(self, houses: Dict[int, House], batteries: Dict[int, Battery]) -> None:
        self.houses = houses
        self.batteries = batteries
        self.cables = {} # Dict containing house_id and Cable object
        self.cost = 0
        self.score = 0
        self.depth = 0
        self.total_cable_length = 0
        self.base = ""
        self.algorithm_used = ""
        self.swaps = 0
    
    # Returns total cost of all cables for one solution
    def cables_cost_no_overlap(self) -> int:
        for house_id in self.cables:
            cost_cable = self.cables[house_id].cost
            self.cost += cost_cable

        self.total_cable_length = float(self.cost / 9)
        return self.cost

    # Adds cables to dictionary 
    def add_cables(self) -> dict:
        for house_id in self.houses:
            house: House = self.houses[house_id]
            # If house is not yet connected to a battery
            if house.to_battery != None:
                # Creates Cable object given a house and connected battery
                cable: Cable = Cable(house, self.batteries[house.to_battery])
                # Adds cable object to self.cables dictionary
                self.cables[house_id] = cable
                self.cables[house_id].add_cables()
        return self.cables
    
    def cost_with_overlay(self) -> int:
        battery_unique_segments = 0
        for battery_id in self.batteries:
            # Adds all segments of cables leading to certain battery to a list [[(x,y),(x,y)][(x,y),(x,y)]] ------
            all_segments = []
            for cable in self.cables:
                if self.cables[cable].end.id == battery_id:
                        current_segments = self.cables[cable].segments #saves segments (which is a list, containing al the segments [[segment][segment][segment]etc]
                        length_current_segments = len(current_segments) #saves length of segments list to use to loop through
                        for segment in range(length_current_segments): #loops through the list of segments of the current cable
                            current_segment = current_segments[segment] #segment of a certain position in the list                          
                            all_segments.append(current_segment) #adds segment to a list which will contain the segments of all the cables which are connected to a certain battery
            
            # Checks if one of the segments appears more than once in list, if so, deletes segment from list
            unique_segments = []
            duplicates = {}
            duplicates_reversed = {}
            for segments in all_segments:

                copy_segment = copy.deepcopy(segments)
                reversed_segment = [copy_segment[1], copy_segment[0]]

                count_segment = all_segments.count(segments)
                count_reversed_segment = all_segments.count(reversed_segment)

                if count_segment < 2 and count_reversed_segment < 1: #if it appears more than once, removes the current value (method of doing this can be done on value in the future)                   
                    unique_segments.append(segments)
                else:
                    # ----- check which segments had duplicates
                    if segments != duplicates.values():
                        duplicates[count_segment] = segments
                    
                    if segments != duplicates_reversed.keys():
                        duplicates_reversed[count_reversed_segment] = segments

            # Counts how many unique of those duplicates there were
            unique_in_duplicates = 0
            for j in duplicates.values():
                unique_in_duplicates += 1

            unique_in_duplicates_reversed = 0
            for z in duplicates_reversed.keys():
                if z != 0:
                    unique_in_duplicates_reversed += 1
            
            total_unique_segments = len(unique_segments) + unique_in_duplicates + unique_in_duplicates_reversed

            battery_unique_segments += total_unique_segments
        
            
        self.cost = battery_unique_segments * 9

        return self.cost
                    

