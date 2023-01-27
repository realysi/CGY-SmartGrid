from sys import argv
from .house import House
from .battery import Battery
from .cable import Cable
from typing import Dict, List


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
            # Gives Battery connected to given house
            connected_battery: Battery = self.batteries[self.houses[house_id].to_battery]

            # Creates Cable object given a house and connected battery
            cable: Cable = Cable(self.houses[house_id], connected_battery)
            
            self.cables[house_id] = cable

            # for house_id in self.cables: 
            self.cables[house_id].calculate_segments()
            self.cables[house_id].calculate_distance()
            self.cables[house_id].calculate_cost()

        return self.cables
    
    def overlay(self):
        total_segments = 0
        for i in range(1,6):
            #------ Adds al segments of cables leading to certain battery to a list [[(x,y),(x,y)][(x,y),(x,y)]] ------
            all_segments = []
            for cable in self.cables: #loops through all the cables in this dataset
                if self.cables[cable].battery.id == i:  #if battery.id = 1,2,3,4 or 5
                        current_segments = self.cables[cable].segments #saves segments (which is a list, containing al the segments [[segment][segment][segment]etc]
                        length_current_segments = len(current_segments) #saves length of segments list to use to loop through
                        for segment in range(length_current_segments): #loops through the list of segments of the current cable
                            current_segment = current_segments[segment] #segment of a certain position in the list                          
                            all_segments.append(current_segment) #adds segment to a list which will contain the segments of all the cables which are connected to a certain battery
            
            #------- will check if one of the segments appears more than once in the list --> if so, deletes it from the list
            set_all_segments = set(all_segments)
            print(set_all_segments)


            """for segment in all_segments:
                copy_segment = copy.deepcopy(segment)
                reversed_segment = [copy_segment[1], copy_segment[0]]
                
                count_segment = all_segments.count(segment)
                count_reversed_segment = all_segments.count(reversed_segment)

                if count_segment > 1: #if it appears more than once, removes the current value (method of doing this can be done on value in the future)
                    all_segments.remove(segment)
                
                if count_reversed_segment > 0: #if the reversed (same cableline) appears as well, delete this one aswell
                    all_segments.remove(segment)
    
            amount_unique_segments = len(all_segments)
            print(all_segments)
            print(amount_unique_segments)
            total_segments += amount_unique_segments

        print(total_segments)"""

        """copy_current_segment = copy.deepcopy(current_segment)


                    tempory_list.append(self.cables[cable].segments)
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
                    print(mini_deepcopy)
                    #print(mini_list_cables)
                    list_cables.append(mini_deepcopy)
                    mini_list_cables.pop(0)


            #print(list_cables)

            length_list_cables = len(list_cables)
            for k in range(length_list_cables):
                a = list_cables.count(list_cables[k]) #alleen kabels in dezelfde richting deelt nu
                kopie = copy.deepcopy(list_cables[k])
                new_kopie = [kopie[1], kopie[0]]
                b = list_cables.count(new_kopie) # nu beide richtingen
                totaal = a + b
                #print(totaal)
                if totaal > 1:
                    overlay = True
                #print(totaal)


    
"""