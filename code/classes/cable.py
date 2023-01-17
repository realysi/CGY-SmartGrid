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
        self.segments = 0
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
        pass
    def check_overlay(self):
        pass

    def calculate_price(self): #moet nog rekening houden met check_overlay
        self.cost = self.distance * 9
        return self.cost

    
