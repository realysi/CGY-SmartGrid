from typing import List, Dict, Tuple, Any
from ..classes.house import House
from ..classes.battery import Battery
from ..classes.cable import Cable
from ..clusters import make_clusters
from ..classes.data import Data
from ..read import read_data
from .distance_related_algorithm import shuffle, change_algorithm, mistakes
from copy import deepcopy
import random

"""

This algorithm works by making clusters of houses which are 'close'to one another.
The clusters of houses are made in code/clusters.py.
Clusters contain at least two houses and each house can only belong to one cluster.
House in the cluster which is closest to the battery is called the main house.
All other houses in the cluster connect to the main house and from there,
every house connects to the nearest battery.

"""

def cluster_output(cluster, houses) -> int:
    """
    Returns total output of cluster.
    """
    output: int = 0
    for house in cluster:
        output += houses[house].max_output
    return output

def calc_middle(cluster, houses) -> Tuple[int, int]:
    """
    Returns a tuple containing the coordinates which correspond to the middle of a given cluster.
    Does this by dividing the total x and y coordinates by the amount of houses in a cluster.
    """
    # Keeps track of how many houses there are in a cluster
    cluster_size = 0
    x = 0
    y = 0
    for house_id in cluster:
        cluster_size += 1
        x += houses[house_id].x
        y += houses[house_id].y
    x_avg = round(x / cluster_size)
    y_avg = round(y / cluster_size)
    return (x_avg, y_avg)


def closest_house_to_battery(cluster, closest_battery, batteries, houses) -> int:
    battery = batteries[closest_battery]
    smallest_distance = 50
    closest_house_id = 0
    for house_id in cluster:
        # Calculate distance between centre of cluster and battery
        delta_x = abs(houses[house_id].x - battery.x)
        delta_y = abs(houses[house_id].y - battery.y)
        distance = delta_x + delta_y
        if distance < smallest_distance:
            smallest_distance = distance
            main_house = house_id
    return main_house


def closest_battery_to_cluster(middle: Tuple[int, int], batteries) -> int:
    """
    Returns the battery id of the battery
    which is closest to the centre of a given cluster.
    """
    # Distance between center of cluster and battery cannot exceed 50
    smallest_distance = 50
    closest_battery_id = 0
    for battery_id in batteries:
        # Calculate distance between centre of cluster and battery
        delta_x = abs(batteries[battery_id].x - middle[0])
        delta_y = abs(batteries[battery_id].y - middle[1])
        distance = delta_x + delta_y
        if distance < smallest_distance:
            smallest_distance = distance
            closest_battery_id = battery_id
    return closest_battery_id


def houses_to_house(cluster, houses, main_house, closest_battery, batteries, data) -> None:
    """
    Connects all houses in the cluster to the one house in the cluster which is
    closest to the battery. Adds the closest battery to all houses but the main
    house in the cluster.
    """
    for house_id in cluster:
        if house_id != main_house:
            houses[house_id].to_house = main_house
            houses[house_id].to_battery = closest_battery
            batteries[closest_battery].add_house(houses[house_id])
            cable = Cable(houses[house_id], houses[main_house])
            cable.add_cables()
            data.cables[house_id] = cable


def main_house_to_battery(houses, main_house, closest_battery, batteries, data) -> None:
    """
    Connects the main house to the closest battery. 
    """
    cable = Cable(houses[main_house], batteries[closest_battery])
    cable.add_cables()
    # Adds cable to data dictionary
    data.cables[main_house] = cable
    # Connects main house to battery
    houses[main_house].to_battery = closest_battery
    batteries[closest_battery].add_house(houses[main_house])

def connect_cluster(cluster, houses, main_house, closest_battery, batteries, data) -> None:
    houses_to_house(cluster, houses, main_house, closest_battery, batteries, data)
    main_house_to_battery(houses, main_house, closest_battery, batteries, data)


def left_over_houses(houses, batteries, data) -> None:
    """
    Adds left over houses to random batteries.
    """
    bat = random.randint(1, 5)
    for house in houses:
        if houses[house].to_battery == None:
            if houses[house].max_output < batteries[bat].capacity:
                cable = Cable(houses[house], batteries[bat])
                cable.add_cables()
                data.cables[house] = cable
                houses[house].to_battery = bat
                batteries[bat].add_house(houses[house])


def cluster_algorithm(houses, batteries) -> Data:
    data = Data(houses, batteries)
    clusters = make_clusters(houses)
    for cluster in clusters:
        middle = calc_middle(cluster, houses)
        closest_battery = closest_battery_to_cluster(middle, batteries)
        output = cluster_output(cluster, houses)
        main_house = closest_house_to_battery(cluster, closest_battery, batteries, houses)
        
        if batteries[closest_battery].capacity > output:
            connect_cluster(cluster, houses, main_house, closest_battery, batteries, data)
        else:
            if closest_battery < 5:
                closest_battery += 1
            elif closest_battery == 1:
                closest_battery += 1
            connect_cluster(cluster, houses, main_house, closest_battery, batteries, data)
        left_over_houses(houses, batteries, data)
    if mistakes(houses):
        shuffle(houses, batteries, True, 1, 1)
    return data