from typing import List, Dict, Tuple, Any

class House:
    def __init__(self, x, y, max_output, id):
        self.x = x
        self.y = y
        self.max_output = max_output
        self.id = id
        self.to_battery: int = None #int hinttype is neccesary here for my code ~ Yanick
        self.incluster: bool = False
        self.to_house: int = None

    def __repr__(self) -> str:
        return f" id: {self.id}\tcoordinates = ({self.x}, {self.y})\t| output = {self.max_output}\t| battery:{self.to_battery} | to house: {self.to_house}\n"

    