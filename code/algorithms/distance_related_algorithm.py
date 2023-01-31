import math
import random
from ..classes.data import Data
from copy import deepcopy

"""
First calculate the distances between each house and battery.
Then we make a list of tuples containing the house_id and the distance to the battery. (doing this for each battery)
After making the lists we are going to add the houses to the battery
"""

# Checks if there are houses without a battery
def mistakes(houses) -> bool:
    for house_id in houses:
        if houses[house_id].to_battery == None:
            return True
    return False
        
# For now returns distance
def calculate_score(house, distance):
    mean_distance = 34
    mean_capacity = 50
    return distance   

# Add scores to the houses
def add_scores(houses, batteries):
    for battery_id in batteries:
        unsorted_list = []
        for house_id in houses:
            # Manhatten distance
            distance_between_bat_house = calculate_distance(houses[house_id], batteries[battery_id])

            # Calculate score considering output and distance from house
            score_between_bat_house = calculate_score(houses[house_id], distance_between_bat_house)

            # Add houses and their score to the battery to the list in battery class
            unsorted_list.append((houses[house_id].id, score_between_bat_house)) 
        sorted_list = sort_list_distance(unsorted_list)
        batteries[battery_id].best_score_houses = sorted_list   

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

# Adds first house in closest_house to battery and then goes to next battery.
def add_houses_bat(houses, batteries):
    # Counter goes to the amount of houses in each list for eacht battery
    for counter in range(len(houses)):
        for battery_id in batteries:
            battery = batteries[battery_id]
            # House gives tuple (house_id , distance), we need house_id
            house_id = battery.best_score_houses[counter][0] 
            house = houses[house_id]
            if fits(battery, house):
                        subtract(battery, house)

# Hill_climber function to shuffle houses.
def shuffle(houses, batteries, change):
    # Get houses without a connected battery
    houses_without_battery = []
    for house_id in houses:
        if houses[house_id].to_battery is None:
            houses_without_battery.append((house_id, houses[house_id].max_output))

    # Get a battery to remove a house from
    batteries_with_space = []
    for battery_id in batteries:
        if batteries[battery_id].capacity > 1:
            batteries_with_space.append(battery_id)
    battery_id_to_shuffle = random.choice(batteries_with_space)
    # Finds house to remove
    house_to_remove = random.choice(batteries[battery_id_to_shuffle].to_houses)
    batteries[battery_id_to_shuffle].remove_house(houses[house_to_remove])
    houses_without_battery.append((houses[house_to_remove].id, houses[house_to_remove].max_output))
    fit_houses(houses, batteries, houses_without_battery, change)

# Tries to fit all the houses without a battery
def fit_houses(houses, batteries, houses_without_battery, change):
    # Sort the houses on their output
    houses_without_battery.sort(key = lambda x: x[1])

    # If we tried to fit the first house in the list for 20 times and no solution came 
    # we switch the order of houses we want to fit first
    if change is False:
        houses_without_battery.reverse()

    for battery_id in batteries:
        for house in houses_without_battery:
            house_to_fit = house[0]
            if houses[house_to_fit].max_output < batteries[battery_id].capacity:
                batteries[battery_id].add_house(houses[house_to_fit])
                houses_without_battery.remove(house)
                continue
    return houses_without_battery

# Counter for when we change the house_order for fitting houses
def change_algorithm(counter):
    if counter < 20:
        return False
    else:
        return True

        
def distance_algorithm(houses, batteries):
    add_scores(houses, batteries)
    add_houses_bat(houses, batteries)
    copy_houses = deepcopy(houses)
    copy_batteries = deepcopy(batteries)
    counter = 0
    runs = 0
    while mistakes(copy_houses):
        change = change_algorithm(counter)
        counter += 1
        if counter > 40:
            counter = 0
        shuffle(copy_houses, copy_batteries, change)
        runs += 1
    print(runs)
    return Data(copy_houses, copy_batteries)


#Had dit even nodig ~ Yanick
def exp_greedy_algorithm(houses, batteries):
    data = distance_algorithm(houses, batteries)
    data.add_cables
    data.cost_with_overlay

    return data