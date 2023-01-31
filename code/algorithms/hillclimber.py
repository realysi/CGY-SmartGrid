"""
Name algorithm: Restart hill climber
by: Yanick
Description:
This is a restart hill climber algorithm. It starts with a solution from the random algorithm and tries to improve
the given dataset by trying to switch 2 houses of 2 different batteries with eachother. It checks if in n-tries none of the
batteries capacities are exceeded due to the switch and wether the switch results in lower costs. If these 3 
requirements are met, then the switch is made permanent. 
"""
import csv
from matplotlib import pyplot as plt
from .random_algorithm import random_algorithm
from code.classes.data import Data
from code.classes.house import House
from code.classes.battery import Battery
#from code.visualisation.hillclimber_views import sketch
import random
import copy

def swaps(amount_of_houses):
    pass

#--- no bugs ---
def select_houses(data: Data, amount_of_houses):
    house_choices = []
    batteries_left = [1,2,3,4,5]
    while len(house_choices) != amount_of_houses:
        id_battery = random.choice(batteries_left)
        batteries_left.remove(id_battery)
        battery = data.batteries[id_battery]
        houses_in_battery = []
        for house in battery.to_houses:
            houses_in_battery.append(house)
        id_house = random.choice(houses_in_battery)
        house = data.houses[id_house]
        house_choices.append(house)

    return house_choices


#--- 
def switch_max(data: Data, chosen_houses:list[House]):
    length_houses = len(chosen_houses)
    copy_house_one_output = 0
    #--- loop through houses in list
    for i in range(length_houses):
        house = chosen_houses[i]
        data.batteries[house.to_battery].capacity += house.max_output #remove output from current house from the capacity
        if i == 0:
            copy_house_one_output = copy.deepcopy(house.max_output) #make copy since you gonna change this
        elif i == length_houses - 1 and length_houses > 1: #last house in list
            data.batteries[house.to_battery].capacity -= copy_house_one_output #subtract the buffer of houses[0]
            break
        
        house_after = chosen_houses[i + 1]
        data.batteries[house.to_battery].capacity -= house_after.max_output #--- remove output from battery and add output from next house
    
    """for i in chosen_houses:
        battery = data.batteries[i.to_battery]
        print(f"switch_max: {i.id}\t| {battery.capacity}")"""
        
def switch_bat(data: Data, chosen_houses:list[House]):
    length_houses = len(chosen_houses)
    copy_house_one_battery = 0
    #--- loop through houses in list
    for i in range(length_houses):
        house = chosen_houses[i]
        if i == 0:
            copy_house_one_battery = copy.deepcopy(house.to_battery) #make copy since you gonna change this
        elif i == length_houses - 1 and length_houses > 1: #last house in list
            house.to_battery = copy_house_one_battery #switch batteries of house_one and house_two
            break
        
        house_after = chosen_houses[i + 1]
        house.to_battery = house_after.to_battery

    """for i in chosen_houses:
        print(f"switch_bat: {i.id}\t| {i.to_battery}")"""



def switch_houses(data: Data, chosen_houses: list[House]):
    length_houses = len(chosen_houses)
    copy_house_one_id = 0
    #--- loop through houses in list
    for i in range(length_houses):
        house = chosen_houses[i]
        battery_house_id = data.houses[house.id].to_battery
        battery_house = data.batteries[battery_house_id]
        battery_house.to_houses.remove(house.id)
        if i == 0:
            copy_house_one_id = copy.deepcopy(house.id) #make copy since you gonna change this
        elif i == length_houses - 1 and length_houses > 1: #last house in list
            data.batteries[house.to_battery].to_houses.append(copy_house_one_id)
            break
        
        house_after = chosen_houses[i + 1]
        data.batteries[house.to_battery].to_houses.append(house_after.id)
        house.to_battery = house_after.to_battery


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


def clear_segments(data: Data, choice_houses:list[House]):
    """
    Clears the segments of the houses that will be switched from batteries
    """
    for i in choice_houses:
        data.cables[i.id].segments.clear()


def runs(tries: int) -> bool:
    """
    returns True if amount of tries is under the given limit.
    """
    if tries < 100:
        return True
    else: 
        return False


def bitch(data: Data, amount_of_houses):
    while True:
        if runs(data.depth):
            data.depth += 1
            copy_data: Data = copy.deepcopy(data)

            houses = select_houses(copy_data, amount_of_houses)
            #switch_houses(data, houses)
            switch_max(copy_data, houses)

            switch_bat(copy_data, houses)

            clear_segments(copy_data, houses)
            copy_data.add_cables()

            if valid_switch(copy_data):
                if better_score_after_switch(data, copy_data):
                    print(f"cost: {copy_data.cost}\t| depth : {data.depth}")
                    return copy_data
                    
                else:
                    #print(f"cost: {data.cost}\t| depth : {data.depth}")
                    continue         
            else:
                #print(f"cost: {data.cost}\t| depth : {data.depth}")
                continue
        else:
            return data
            break

    pass


def random_solution(houses: dict[int, House], batteries: dict[int, Battery]) -> Data:
    """
    Returns data object which has been solved by the random algorithm and alreay has the segments and costs calculated.
    """
    data: Data = random_algorithm(houses, batteries)
    data.add_cables()
    data.cost_with_overlay()

    return data


def restart_hillclimber(houses, batteries, amount_of_houses) -> dict[int, Data]:
    """"
    Returns dictionary that contains data object of all hill climber runs (key = number of run, value = data object).
    Hill climber algorithm that restarts for x amount of times if after n-runs no beter solution has been found.
    """
    results = {}
    total_hillclimbers: int = 0
    while total_hillclimbers < 1:
        data: Data = random_solution(houses, batteries)

        while data.depth < 100:
            data = bitch(data, amount_of_houses)
            
        data.algorithm_used = "hill climber"
        data.base = "random"

        print(f"run: {total_hillclimbers}\t| cost: {data.cost}\t| depth : {data.depth}")
        results[total_hillclimbers + 1] = data
        total_hillclimbers += 1

            
    save_data(results)
    print(results)
    #sketch(results)
    return results

def save_data(dictionary: dict[int, Data]):
    fields = ["Run", "Depth", "Cost", "Algorithm", "Base"]
    filename = "hillclimber.csv"

    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(fields)
        for i in dictionary:
            run = i
            depth = dictionary[i].depth
            cost = dictionary[i].cost
            algo = dictionary[i].algorithm_used
            algo_base = dictionary[i].base
            row = [run, depth, cost, algo, algo_base]
            csv_writer.writerows([row])

    

