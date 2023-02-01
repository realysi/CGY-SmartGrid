"""
Name algorithm: Hillclimber
by: Yanick
"""
from matplotlib import pyplot as plt
from .random_algorithm import random_algorithm
from code.classes.data import Data
from code.classes.cable import Cable
from code.classes.house import House
from code.classes.battery import Battery
import random
import copy

def select_house_one(data: Data) -> House:
    """
    Returns a house object.
    Selects a random house from a random battery.
    """

    #Select a random battery
    id_first_battery: int = random.randint(1,5)
    first_battery: Battery = data.batteries[id_first_battery]

    #Add all houses (in this case house_id's) in the chosen first_battery to a list and pick a random house id
    houses_in_first_battery: list = []
    for house in first_battery.to_houses:
        houses_in_first_battery.append(house)
    id_randomhouse: int = random.choice(houses_in_first_battery)
    first_house: House = data.houses[id_randomhouse] #first house

    return first_house

def select_house_two(data: Data, house_one_id) -> House:
    """
    Returns a house object.
    Selects a random house from a random battery, which is different than the battery of select_house_one()
    """

    #Select a random battery (except the one already chosen in function above)
    while True: #this excludes already chosen battery
        id_second_battery: int = random.randint(1,5)
        id_first_battery: int = data.houses[house_one_id].to_battery
        if id_second_battery == id_first_battery:
            continue
        else:
            break
    second_battery: Battery = data.batteries[id_second_battery]

    # - add all houses (in this case house_id's) in the chosen first_battery to a list and pick a random house id
    houses_in_second_battery: list = []
    for house in second_battery.to_houses:
        houses_in_second_battery.append(house)
    id_second_randomhouse: int = random.choice(houses_in_second_battery)
    second_house: House = data.houses[id_second_randomhouse] #first house

    return second_house


def valid_switch(data: Data) -> bool:
    """
    Returns a bool.
    Returns True if none of the batteries have a negative capacity (< 0). Else returns False.
    """

    for battery in data.batteries:
        if data.batteries[battery].capacity < 0:
            return False
    return True

def better_score_after_switch(data_before_switch: Data, data_after_switch: Data) -> bool:
    """
    Returns a bool.
    Returns True if the costs of the edited data object are lower than that of the unedited data object. Else False.
    """

    data_before_switch.cost_with_overlay()
    data_after_switch.cost_with_overlay()
    if data_after_switch.cost < data_before_switch.cost: #return true if after switch cost(score) is better (smaller) than before the switch, so it is equal is still returns false
        return True
    else:
        return False

def switch_max_outputs(data: Data, house_one: House, house_two: House):
    """
    Returns nothing
    Switches the max_outputs of the two houses on the two batteries.
    """
    #removes max_output from the capacity of the batteries
    data.batteries[house_one.to_battery].capacity += house_one.max_output  #remove output from current house from the capacity
    data.batteries[house_two.to_battery].capacity += house_two.max_output  #"same as above"

    #adds max_output from the houses to the capacity of the batteries
    data.batteries[house_one.to_battery].capacity -= house_two.max_output  #switch the outputs from the houses to the capacity of the batteries
    data.batteries[house_two.to_battery].capacity -= house_one.max_output  #"same as above"

def switch_to_houses(data: Data, house_one: House, house_two: House):
    """
    Returns nothing
    Switches the house_id's of the two houses on the to_houses of the two batteries.
    """
    #remove house from to_house of battery
    data.batteries[house_one.to_battery].to_houses.remove(house_one.id)
    data.batteries[house_two.to_battery].to_houses.remove(house_two.id)

    #add house to to_house of battery
    data.batteries[house_one.to_battery].to_houses.append(house_two.id)
    data.batteries[house_two.to_battery].to_houses.append(house_one.id)

def runs(tries):
    if tries < 10:
        return True
    else: 
        return False

def sketch(results: dict):
    scores = []
    depth = []
    for hillclimber in results:
        scores.append(results[hillclimber].cost)
        depth.append(results[hillclimber].depth)

    best_score = min(scores)

    for i in results:
        if results[i].cost == best_score:
            data_best_score = results[i]

    average_depth = sum(scores) / len(scores)


#makes it well enough to a depth of 60 in an okay time (10 min)
#further than 100 steps can take up to an hour and a half

        
    plt.hist(scores)
    plt.show()
    plt.hist(depth)
    plt.show()

def switch(data: Data) -> Data:
    """
    Returns data object 
    Edits data object and if valid_switch() and beter_score_after_switch() return true
    it returns the edited data object, otherwise the old object.
    """
    tries = 0
    while True:
        if runs(tries):
            copy_data: Data = copy.deepcopy(data)
            house_one: House = select_house_one(copy_data)
            house_two: House = select_house_two(copy_data, house_one.id)

            switch_max_outputs(copy_data, house_one, house_two)
            switch_to_houses(copy_data, house_one, house_two)

            copy_house_one_battery: int = copy.deepcopy(house_one.to_battery) #make a deepcopy of house_one battery as buffer
            house_one.to_battery = house_two.to_battery #switch batteries of house_one and house_two
            house_two.to_battery = copy_house_one_battery

            copy_data.cables[house_one.id].segments.clear()
            copy_data.cables[house_two.id].segments.clear()

            copy_data.add_cables() #only should have to do this for two switched houses

            if valid_switch(copy_data):
                if better_score_after_switch(data, copy_data):
                    #print(data.cost_with_overlay(), copy_data.cost_with_overlay())
                    #print(copy_data.cables[house_one.id].segments, copy_data.cables[house_two.id].segments)
                    #print(tries)
                    return copy_data
                else:
                    tries += 1
                    continue         
            else:
                tries += 1
                continue

        else:
            return data
            break

        #fout zit hem erin dat als de huizen en batterijen worden geswitched, de kabels en dus segmenten dat nog niet doen --> nog oplossen

def hillclimber(houses, batteries) -> Data:
    data: Data = random_algorithm(houses, batteries)
    data.add_cables()
    data.cost_with_overlay() #calculates cost of grid
    for i in range(20):
        copy_data = data
        data = switch(data)
        if copy_data == data:
            print("JA")
        
        print(f"\n{i}\n")

    return data

def restart_hillclimber(houses, batteries):
    results = {}
    total_hillclimbers = 1
    while total_hillclimbers < 6:
        data: Data = random_algorithm(houses, batteries)
        data.add_cables()
        data.cost_with_overlay()
        for i in range(100):
            #print(f"TRY: {total_hillclimbers}")
            copy_data = data
            data = switch(data)
            data.depth += 1
            if copy_data == data:
                print(f"cost: {data.cost} | depth : {data.depth}")
                #print("TRY TERMINDATED:")
                results[total_hillclimbers] = data
                total_hillclimbers += 1
                break
            else:
                continue

    print(results)
    sketch(results)
    return results


    

