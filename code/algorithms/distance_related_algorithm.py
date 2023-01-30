import math
import random
from ..classes.data import Data
"""
First calculate the distances between each house and battery.
Then we make a list of tuples containing the house_id and the distance to the battery. (doing this for each battery)
After making the lists we are going to add the houses to the battery
"""

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
    # Counter goes to 150 because there are 150 houses in each list for eacht battery
    for counter in range(150):
        for battery_id in batteries:
            battery = batteries[battery_id]
            # House gives tuple (house_id , distance), we need house_id
            house_id = battery.best_score_houses[counter][0] 
            house = houses[house_id]
            if fits(battery, house):
                        subtract(battery, house)
    #print(houses)
    #print(batteries)

    while mistakes(houses):
        shuffle_houses(houses, batteries)
        fill_batteries(houses, batteries)
    return Data(houses, batteries)

# Checks which houses have no battery and shuffles them randomly with a house in a battery
def shuffle_houses(houses, batteries):

    houses_without_battery = []

    house_id_to_shuffle = 0
    output_house_to_shuffle = 0


    # Checks which houses have no battery
    for house_id in houses:
        if houses[house_id].to_battery is None:
            houses_without_battery.append((house_id, houses[house_id].max_output))

    # Check which house without a battery has the most output 
    for house in houses_without_battery:
        if house[1] > output_house_to_shuffle:
            output_house_to_shuffle = house[1]
            house_id_to_shuffle = house[0]

    # Check which batteries have capacity > 1 and choses random battery to switch with.
    batteries_with_space = []
    bat_id_to_shuffle = 0
    for battery_id in batteries:
        if batteries[battery_id].capacity > 1:
            batteries_with_space.append(battery_id)
    if len(batteries_with_space) > 0:
        bat_id_to_shuffle = random.choice(batteries_with_space)

    # Random choice of house to remove
    house_id_to_remove = random.choice(batteries[bat_id_to_shuffle].to_houses)

    # Shuffling takes place here
    battery_to_shuffle = batteries[bat_id_to_shuffle]    
    battery_to_shuffle.remove_house(houses[house_id_to_remove])
    battery_to_shuffle.add_house(houses[house_id_to_shuffle])    

# Function that finds the houses without battery and tries to fit these
def fill_batteries(houses, batteries):
    # List with house_id's and their output that dont have a battery yet
    houses_without_battery = []

    # List with battery_id's and their capacity
    batteries_id_capacity = []

    # Checks which houses have no battery
    for house_id in houses:
        if houses[house_id].to_battery is None:
            houses_without_battery.append((house_id, houses[house_id].max_output))
    
    # Sorts houses on biggest output
    houses_without_battery.sort(key = lambda x: x[1])
    houses_without_battery.reverse()

    for battery_id in batteries:
        batteries_id_capacity.append((battery_id, batteries[battery_id].capacity))

    # Sorts batteries on most capacity left
    batteries_id_capacity.sort(key = lambda x: x[1])
    batteries_id_capacity.reverse()

    # Tries to add all houses without battery to the batteries
    for house_tuple in houses_without_battery:
        for battery_tuple in batteries_id_capacity:
            if house_tuple[1] < battery_tuple[1]:
                batteries[battery_tuple[0]].add_house(houses[house_tuple[0]])

        
def distance_algorithm(houses, batteries):
    add_scores(houses, batteries)
    return add_houses_bat(houses, batteries)
    #return add_houses_bat_alternative(houses, batteries)
