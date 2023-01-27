from sys import argv
from .house import House
from typing import Dict, List, Tuple, Set, Any

"""
# Appends to self.distances list of tuples containing: 
# (home_house_id, away_house_id)
# List only contains tuples with a distance of < 5 between houses.
"""
def neighbours(houses: Dict[int, House]) -> Any:
    neighbours: Dict[int, list] = {}
    for home in houses:
        x_home = (houses[home].x)
        y_home = (houses[home].y)
        for away in houses:
            x_away = (houses[away].x)
            y_away = (houses[away].y)
            # Skips if home house is same as away house
            if x_home == x_away and y_home == y_away:
                continue
            # Calculates total (dx + dy) distance
            distance = abs(x_home - x_away) + abs(y_home - y_away)
            if distance < 5 and (away not in neighbours or home not in neighbours[away]):
                # If key is not yet in Dict, make empty list for key
                if home not in neighbours.keys():
                    neighbours[home] = []
                neighbours[home] += [away]
    return print(neighbours)


# Adds Tuples containing clusters of houses to the self.clusters Set
def make_clusters(houses: Dict[int, House]) -> None:
    neighbours(houses)
    visited = set()
    clusters: List[List[Any]] = []
    for key in neighbours.keys():
        cluster = []
        if key not in visited:
            visited.add(key)
            cluster += [key]
        for value in neighbours[key]:
            if value not in visited:
                visited.add(value)
                cluster.append(value)

        if cluster != [] and len(cluster) > 1:
            print(cluster)
            clusters.append(cluster)