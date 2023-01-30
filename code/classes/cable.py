from math import sqrt
import copy


class Cable:
    
    # Class takes two arguments, start object and end object
    # Draws cable from x,y of start object to x,y of end object
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.x = []
        self.y = []
        self.distance = 0
        self.segments = []
        self.cost = 0
    
    def calculate_segments(self):
        start_x, start_y, end_x, end_y = self.start.x, self.start.y, self.end.x, self.end.y
        delta_x = (end_x - start_x)
        delta_y = (end_y - start_y)
        current_x, current_y = start_x, start_y

        # If end object is to the right of the start object
        if delta_x > 0: 
            while current_x != end_x + 1:
                self.x.append(current_x)
                current_x += 1
        elif delta_x < 0:
            while current_x != end_x - 1:
                self.x.append(current_x)
                current_x -= 1
        # If end object is above the start object
        if delta_y > 0: 
            while current_y != end_y + 1:
                self.y.append(current_y)
                current_y += 1   
        # If end object is below the start object   
        elif delta_y < 0:
            while current_y != end_y - 1:
                self.y.append(current_y)
                current_y -= 1
        # List for all the coordinates of the cable [(),(),()]
        coordinates_cables = [] 
        # First move the x value
        for i in self.x:
            coordinates_cables.append((i, start_y))

        # Then move y
        for i in self.y:
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
        
        return self.segments

    def calculate_distance(self):
        self.distance = len(self.segments)
        return self.distance

    def calculate_cost(self):
        self.cost = self.distance * 9
        return self.cost

    def add_cables(self):
        self.calculate_segments()
        self.calculate_distance()
        self.calculate_cost()