from typing import List, Dict, Tuple, Any

class House:
    """
    
    """
    def __init__(self, x, y, max_output, id):
        self.x = x
        self.y = y
        self.max_output = max_output
        self.id = id
        self.to_battery: int = None
        self.incluster: bool = False

    def __repr__(self) -> str:
        return f" id: {self.id}\tcoordinates = ({self.x}, {self.y})\t| output = {self.max_output}\t| battery:{self.to_battery}\n"