from math import sqrt
from .house import House
from .battery import Battery


class Cable:
    
    def __init__(self, house: House, battery: Battery) -> None:
        self.battery = battery
        self.house = house
        self.x = []
        self.y = []
        self.distance = 0
        self.segments = []
        self.cost = 0
    
    def calculate_segments(self):
        #Cable drawn from house to battery
        start_x, start_y, end_x, end_y = self.house.x, self.house.y, self.battery.x, self.battery.y

        delta_x = (end_x - start_x)
        delta_y = (end_y - start_y)

        x_coordinates_segments = []
        y_coordinates_segments = []

        current_x = start_x #trying to avoid a softcopy
        current_y = start_y # "

        if delta_x > 0: #battery to the right of the house
            while current_x != end_x + 1:
                x_coordinates_segments.append(current_x)
                current_x += 1
        elif delta_x < 0: #To the left of the house
            while current_x != end_x - 1:
                x_coordinates_segments.append(current_x)
                current_x -= 1

        if delta_y > 0: #Battery above the hosue
            while current_y != end_y + 1:
                y_coordinates_segments.append(current_y)
                current_y += 1      
        elif delta_y < 0: #under the house
            while current_y != end_y - 1:
                y_coordinates_segments.append(current_y)
                current_y -= 1
        
        coordinates_cables = [] #list for all the coordinates of the cable [(),(),()]
        #first move the x value
        for i in x_coordinates_segments:
            coordinates_cables.append((i, start_y))

        #then move y
        for i in y_coordinates_segments:
            if i != start_y:
                coordinates_cables.append((end_x, i))

        self.segments = coordinates_cables
        
        return self.segments

    def calculate_distance(self):
        segments = self.segments 
        length_segments = len(segments)
        length_route = length_segments - 1 #3 points = 2 lines etc
        self.distance = length_route
        return self.distance

    def check_overlay(self):
        pass

    def calculate_cost(self): #moet nog rekening houden met check_overlay
        self.cost = self.distance * 9
        return self.cost
