from math import sqrt
from .house import House
from .battery import Battery
import copy


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
        # Cable drawn from house to battery
        start_x, start_y, end_x, end_y = self.house.x, self.house.y, self.battery.x, self.battery.y

        delta_x = (end_x - start_x)
        delta_y = (end_y - start_y)

        x_coordinates_segments = []
        y_coordinates_segments = []

        current_x = start_x
        current_y = start_y
        # Battery to the right of the house 
        if delta_x > 0: 
            while current_x != end_x + 1:
                x_coordinates_segments.append(current_x)
                current_x += 1
        elif delta_x < 0:
            while current_x != end_x - 1:
                x_coordinates_segments.append(current_x)
                current_x -= 1
        # Battery above the hosue
        if delta_y > 0: 
            while current_y != end_y + 1:
                y_coordinates_segments.append(current_y)
                current_y += 1      
        elif delta_y < 0: #under the house
            while current_y != end_y - 1:
                y_coordinates_segments.append(current_y)
                current_y -= 1
        # List for all the coordinates of the cable [(),(),()]
        coordinates_cables = [] 
        # First move the x value
        for i in x_coordinates_segments:
            coordinates_cables.append((i, start_y))

        # Then move y
        for i in y_coordinates_segments:
            if i != start_y:
                coordinates_cables.append((end_x, i))

        coordinates_cables_real = []
        mini_segments = []
        length = len(coordinates_cables)
        for i in range(length):
            mini_segments.append(coordinates_cables[i])
            if len(mini_segments) == 2:
                #print(mini_segments)
                mini_deepcopy = copy.deepcopy(mini_segments)
                coordinates_cables_real.append(mini_deepcopy)
                mini_segments.pop(0)

        self.segments = coordinates_cables_real
        #self.segments = coordinates_cables
        
        return self.segments

    def calculate_distance(self):
        segments = len(self.segments)
        self.distance = segments
        return self.distance

    def calculate_cost(self): #moet nog rekening houden met check_overlay
        self.cost = self.distance * 9
        return self.cost
