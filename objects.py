class House:
    """
    
    """
    def __init__(self, x, y, max_output, id):
        self.x = x
        self.y = y
        self.max_output = max_output
        self.id = id
        self.to_bat = False

    def __repr__(self) -> str:
        return f"ID= {self.id}, x={self.x}, y={self.y}, output={self.max_output}, battery={self.to_bat}"

class Battery:
    """
    
    """
    def __init__(self, x, y, capacity, id):
        self.x = x
        self.y = y
        self.capacity = capacity
        self.to_houses = []
        self.id = id
    
    def __repr__(self) -> str:
        return f"ID= {self.id}, x={self.x}, y={self.y}, capacity={self.capacity}, to houses={self.to_houses}"

