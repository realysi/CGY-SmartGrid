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
    
    def add_x(self):
        pass
    
    def add_y(self):
        pass

    def calculate_distance(self):
        x_battery = self.battery.x
        y_battery = self.battery.y
        x_house = self.house.x
        y_house = self.house.y
        #distance = sqrt((x_battery - x_house)^2 + (y_battery - y_house)^2) #a^2 + b^2 = c^2
        x_difference = abs(x_battery - x_house)
        y_difference = abs(y_battery - y_house)
        self.distance = x_difference + y_difference
        return self.distance

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
        length = len(self.segments)
        print(length)
        
        for i in range(length):
            print(self.segments[i], self.segments[i][0], self.segments[i][1])
        return self.segments

    def check_overlay(self):
        pass

    def calculate_price(self): #moet nog rekening houden met check_overlay
        self.cost = self.distance * 9
        return self.cost

    
    """def route(houses):
    x = []
    y = []
    start_x = houses[2].x
    start_y = houses[2].y
    delta_x = 7
    delta_y = -18
    end_x = start_x + delta_x
    # To the same value of the x-axis of the battery (if delta_x is positive, moves from battery to the right).
    if delta_x >= 0:
        for i in range(start_x, (start_x + delta_x + 1), 1):
            x.append(i)
            y.append(start_y)
            plt.plot(x, y, color = 'deepskyblue')
    if delta_x < 0:
        for i in range(start_x, (start_x + delta_x + 1), -1):
            x.append(i)
            y.append(start_y)
            plt.plot(x, y, color = 'deepskyblue')
    if delta_y >= 0:
        for i in range(start_y, (start_y + delta_y + 1), 1):
            x.append(end_x)
            y.append(i)
            plt.plot(x, y, color = 'deepskyblue')
    if delta_y < 0:
        for i in range(start_y, (start_y + delta_y + 1), -1):
            x.append(end_x)
            y.append(i)
            plt.plot(x, y, color = 'deepskyblue')"""

