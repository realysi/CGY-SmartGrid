from math import sqrt
from typing import List, Tuple
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

        # If end object is to the right of start object
        if delta_x > 0: 
            while current_x != end_x + 1:
                self.x.append(current_x)
                current_x += 1
        # If end object is to the left of start object
        elif delta_x < 0:
            while current_x != end_x - 1:
                self.x.append(current_x)
                current_x -= 1
        # If end object is above start object
        if delta_y > 0: 
            while current_y != end_y + 1:
                self.y.append(current_y)
                current_y += 1   
        # If end object is below start object   
        elif delta_y < 0:
            while current_y != end_y - 1:
                self.y.append(current_y)
                current_y -= 1
        # List containing pairs of coordinates
        coordinates = []

        # Move in the x-direction
        for x in self.x:
            coordinates.append((x, start_y))
        # Move in the y-direction
        for y in self.y:
            if y != start_y:
                coordinates.append((end_x, y))

        coordinates_cables: List[List[Tuple[int, int]]] = []
        mini_segments = []

        for tuple in coordinates:
            # Append one pair of coordinates
            mini_segments.append(tuple)

            if len(mini_segments) == 2:
                mini_deepcopy = copy.deepcopy(mini_segments)
                coordinates_cables.append(mini_deepcopy)
                # Pop the first set of coordinates from the list
                mini_segments.pop(0)
        self.segments = coordinates_cables
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