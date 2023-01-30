class Battery:
    """
    
    """
    def __init__(self, x, y, capacity, id):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.to_houses = []
        self.connections = 0
        self.id = id
        self.closest_houses = []
        self.best_score_houses = []

    def remove_house(self, house):
        if house.id in self.to_houses:
            self.to_houses.remove(house.id)
            self.capacity += house.max_output
            self.connections -= 1
            house.to_battery = None


    def add_house(self, house):
        if house.max_output < self.capacity:
            self.to_houses.append(house.id)
            self.capacity -= house.max_output
            self.connections += 1
            house.to_battery = self.id

    
    def __repr__(self) -> str:
        return f"id: {self.id}\tcoordinates = ({self.x}, {self.y})\t| capacity = {self.capacity}\t| connections = {self.connections}\n\tto houses = {self.to_houses}\n"
