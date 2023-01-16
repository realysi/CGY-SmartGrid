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
    
    def __repr__(self) -> str:
        return f"\tcoordinates = ({self.x}, {self.y})\t| capacity = {self.capacity}\t| connections = {self.connections}\n\tto houses = {self.to_houses}\n"
