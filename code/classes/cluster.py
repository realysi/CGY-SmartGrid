from typing import List, Dict, Tuple

class Cluster:

    def __init__(self, id):
        self.output = 0
        self.houses = []
        self.id = id

    def output(self):
        pass

    def add_houses(self, house_id):
        self.houses.append(house_id)