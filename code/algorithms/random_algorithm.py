"""
Info:
Name algorithm: random_algorithm
Door: Yanick
Case: Smartgrid (Teamname: CGY-SmartGrid)


Summary: 
This algorithm solves this smartgrid problem by looking at it as a knapsack problem.
In this case there are 5 knapsacks, which together have to contain 150 objects (houses).
This is solved by randomly selecting a battery and filling this battery with random houses untill there is not more capacity.
Then the algorithm continues to the next battery and repeats the process.
When the last battery has run out of capacity, a check will be performed to see whether all houses are connected to a battery.
In case this is true, the algorithm yields a result. Otherwise the algorithm will restart untill the check is passed.

Example:
->begin<-
normal battery order [1,2,3,4,5] -> random order [3,5,2,4,1]
normal house order [1,2,3,4,5] -> random order [4,1,5,3,2]
Fill battery 4 untill full -> fill battery 3 untill full -> etc
Check if all houses are connected to a battery? Yes --> results | No --> start over
"""
from typing import List, Dict
import random
from ..classes.battery import Battery
from ..classes.house import House
from ..classes.data import Data
from ..classes.score import Score
from copy import deepcopy
from sys import argv

# Makes list with random ints, same amount as battery objects
def random_battery_order(batteries: Dict[int, Battery]) -> List[int]:
    id_keys: List[int] = []
    for battery_id in batteries:
        id_keys.append(battery_id)
    random.shuffle(id_keys)
    return id_keys

# Makes list with random ints, same amount as house objects
def random_house_order(houses):
    id_keys: List[int] = []
    for house_id in houses:
        id_keys.append(house_id)
    random.shuffle(id_keys)
    return id_keys

# Checks if house fits inside battery
def fits(battery: Battery, house: House) -> bool:
    return battery.capacity - house.max_output > 0.0

# Subtracts house output from battery capacity in case house in not connected yet
def subtract(battery: Battery, house: House) -> None:
    if house.to_battery == None: # If house is not yet connected to battery
        battery.capacity -= house.max_output
        battery.to_houses.append(house.id)
        battery.connections += 1
        house.to_battery = battery.id

# Returns True if a house has no battery connection
def mistakes(houses) -> bool:
    for house_id in houses:
        if houses[house_id].to_battery == None:
            return True
    return False

# Returns Data object containing a copy of the houses and batteries dicts.
# Calls all other functions in this file.
def random_algorithm(houses: Dict[int, House], batteries: Dict[int, Battery]):

    while True:
        copy_houses: Dict[int, House] = deepcopy(houses) # Make a deepcopy of the houses dictionary
        copy_batteries: Dict[int, Battery] = deepcopy(batteries) # Make a deepcopy of the batteries dictionary
        battery_order = random_battery_order(copy_batteries) # Randomizes battery id order 
        house_order = random_house_order(copy_houses) # Randomizes house id order 

        for battery_id in battery_order:
            battery: Battery = copy_batteries[battery_id]
            for house_id in house_order:
                house: House = copy_houses[house_id]
                if fits(battery, house):
                    subtract(battery, house)

        # Check if there are houses without battery
        if mistakes(copy_houses):
            continue
        else:
            return Data(copy_houses, copy_batteries)


def start_random(houses, batteries):

    final_score = Score()

    runs = int(argv[4])

    # Runs the algorithm
    for run in range(runs):
        data = random_algorithm(houses, batteries)
        data.add_cables()
        score = data.cost_with_overlay()
        final_score.all_scores.append(score)
        final_score.add_score(score, data)

    # Calculate average score, save dataset of best score
    final_score.calculate_average_score()
    print(final_score.all_scores)
    print(final_score)

    return final_score
    

            
