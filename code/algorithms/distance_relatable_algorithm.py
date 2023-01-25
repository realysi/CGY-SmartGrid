import math
from ..classes.data import Data
"""
First calculate the distances between each house and battery.
Then we make a list of tuples containing the house_id and the distance to the battery. (doing this for each battery)
After making the lists we are gonna add the houses to the battery (starting with battery 1 -> 5)
"""

# We need to calculate the distance between each house and each battery
def add_distances(houses, batteries):
    for battery_id in batteries:
        unsorted_list = []
        for house_id in houses:
            distance_between_bat_house = calculate_distance(houses[house_id], batteries[battery_id]) #manhatten distance
            #add houses and their distance to the battery to the list in battery class
            unsorted_list.append((houses[house_id].id, distance_between_bat_house)) 
        sorted_list = sort_list_distance(unsorted_list)
        batteries[battery_id].closest_houses = sorted_list

# Sorts the unsorted list to the second element of the tuple (house_id , distance)
def sort_list_distance(unsorted_list):
    unsorted_list.sort(key=lambda a: a[1])
    return unsorted_list    

# Calculate the distance between each battery and house
def calculate_distance(house, battery):
    bat_x = battery.x
    bat_y = battery.y
    house_x = house.x
    house_y = house.y
    distance_x = int(math.dist((bat_x,), (house_x,)))
    distance_y = int(math.dist((bat_y,), (house_y,)))
    tot_distance = distance_x + distance_y
    return tot_distance

# Checks if house fits inside battery
def fits(battery, house):
    return battery.capacity > house.max_output

# Subtracts house output from battery capacity in case house in not connected yet
def subtract(battery, house):
    if house.to_battery == None: # If house is not yet connected to battery
        battery.capacity -= house.max_output
        battery.to_houses.append(house.id)
        battery.connections += 1
        house.to_battery = battery.id

# Adds houses to battery
def add_houses_bat(houses, batteries):
    for battery_id in batteries:
        battery = batteries[battery_id]
        for house_and_distance in battery.closest_houses:  
            house_id = house_and_distance[0] # House gives tuple (house_id , distance), we need house_id
            house = houses[house_id]
            if fits(battery, house):
                    subtract(battery, house)
    return Data(houses, batteries)
            

def distance_algorithm(houses, batteries):
    add_distances(houses, batteries)
    add_houses_bat(houses, batteries)
    #print(batteries)
    #print(houses)
