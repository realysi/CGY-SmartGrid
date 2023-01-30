from .classes.house import House
from typing import Dict, List

"""
Cluster.py contains two function which together make clusters of houses which
are relatively close to one another. A house cannot be part of multiple`clusters
at the same time. These cluster can be used in an algorithm to efficiently
connect houses to batteries by sharing cables. 
"""


def make_neighbours(houses: Dict[int, House]) -> Dict[int, list]:
    """
    Returns a dict containing a houses (keys) and their neighbouring houses (values).
    Manhattan distance is calculated between all houses.
    Only adds neighbouring houses with a distance smaller than 5 units to dict.
    """
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
            # Will not create a new key for a house if that house wat already part of a value
            # Maximum distance is also determined here
            if distance < 5 and (away not in neighbours or home not in neighbours[away]):
                if home not in neighbours:
                    # If key not yet in dict, make empty list for the key
                    neighbours[home] = []
                neighbours[home] += [away]
    return(neighbours)
                

def make_clusters(houses) -> List[list]:
    """
    Returns a list of clusters whith every cluster containing unique houses.
    The clusters themselves are also lists.
    """
    neighbours = make_neighbours(houses)
    visited = set()
    clusters: List[list] = []
    for key in neighbours:
        cluster = []
        if key not in visited:
            visited.add(key)
            cluster += [key]
        for value in neighbours[key]:
            if value not in visited:
                visited.add(value)
                cluster.append(value)
        if cluster != [] and len(cluster) > 1:
            clusters.append(cluster)
    return(clusters)
