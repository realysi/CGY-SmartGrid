from math import sqrt
class Cable:
    
    def __init__(self, house, battery) -> None:
        self.battery = battery
        self.house = house
        self.x = []
        self.y = []
        self.segments = 0
        self.cost = 0
    
    def add_x(self):
        pass
    
    def add_y(self):
        pass

    def distance(self, x_battery, y_battery, x_house, y_house):
        #distance = sqrt((x_battery - x_house)^2 + (y_battery - y_house)^2) #a^2 + b^2 = c^2
        x_battery = self.battery.x
        y_battery = self.battery.y
        x_house = self.house.x
        y_house = self.house.y
        x_difference = abs(x_battery - x_house)
        y_difference = abs(y_battery - y_house)
        distance = x_difference + y_difference
        return distance
        # we hebben a, b

    def calculate_segments(self):
        x_battery = self.battery.x
        y_battery = self.battery.y
        x_house = self.house.x
        y_house = self.house.y
        distance()


        

        length_x = len(self.x)
        length_y = len(self.y)
        if length_x == length_y:
            segments = len(self.x)
            return segments
        else:
            raise(ValueError:"Not the same amount of x and y points!")

    def check_overlay(self):
        pass

    def calculate_price(self): #moet nog rekening houden met check_overlay
        cost = self.segments * 9
        return cost

    
