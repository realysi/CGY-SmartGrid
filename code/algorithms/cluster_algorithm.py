from typing import List, Dict, Tuple, Any
from ..classes.house import House
from ..classes.battery import Battery
from ..classes.cable import Cable
from ..clusters import make_clusters
from ..classes.data import Data
from ..read import read_data

raw_data: Data = read_data()

def calc_middle(cluster, houses) -> Tuple[int, int]:
    """
    Returns a tuple containing the coordinates which correspond to the middle of a given cluster.
    Does this by dividing the total x and y coordinates by the amount of houses in a cluster.
    """
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
        

def closest_battery_to_cluster(middle: Tuple[int, int], batteries) -> Battery:
    """
    Returns the battery object which is closest to the centre of a given cluster.
    """
    # Distance between center of cluster and battery cannot exceed 100 
    smallest_distance = 100
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


def closest_house_to_battery(cluster, houses, batteries) -> House:
    """
    Returns house from cluster which is closest to the nearest battery.
    """
    for house_id in houses:


def cluster_algorithm(houses, batteries):
    clusters = make_clusters(houses)
    for cluster in clusters:
        middle = calc_middle(cluster, houses)
        closest_battery = closest_battery_to_cluster(middle, batteries)
    pass