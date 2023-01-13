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
