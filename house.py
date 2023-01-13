class House:
    """
    
    """
    def __init__(self, x, y, max_output, id):
        self.x = x
        self.y = y
        self.max_output = max_output
        self.id = id
        self.to_battery = False

    def __repr__(self) -> str:
        return f"ID= {self.id}, x={self.x}, y={self.y}, output={self.max_output}, battery={self.to_battery}\n"