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
from code.visualisation.hillclimber_views import sketch
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


def select_house_two(data: Data, house_one_id: int) -> House:
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

    #Add all houses (in this case house_id's) in the chosen first_battery to a list and pick a random house id
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

#This function will likely be removed since it won't be neccesary much longer
def runs(tries: int) -> bool:
    """
    returns True if amount of tries is under the given limit.
    """
    if tries < 10:
        return True
    else: 
        return False


def switch_batteries(house_one: House, house_two: House):
    """
    Switches the batteries of the houses
    """
    copy_house_one_battery: int = copy.deepcopy(house_one.to_battery) #make a deepcopy of house_one battery as buffer
    house_one.to_battery = house_two.to_battery #switch batteries of house_one and house_two
    house_two.to_battery = copy_house_one_battery


def clear_segments(data: Data, house_one: House, house_two: House):
    """
    Clears the segments of the houses that will be switched from batteries
    """
    data.cables[house_one.id].segments.clear()
    data.cables[house_two.id].segments.clear()


def switch(data: Data) -> Data:
    """
    Returns data object 
    Edits data object and if valid_switch() and beter_score_after_switch() return true
    it returns the edited data object, otherwise the old object.
    """
    #-- if edited data is valid and has a better score within x tries, then return edited data type --
    while True:
        if runs(data.depth):
            data.depth += 1
            #total tries now stored in data.depth which copy_data will copy
            copy_data: Data = copy.deepcopy(data)
            house_one: House = select_house_one(copy_data)
            house_two: House = select_house_two(copy_data, house_one.id)

            switch_max_outputs(copy_data, house_one, house_two)
            switch_to_houses(copy_data, house_one, house_two)

            switch_batteries(house_one, house_two)
            clear_segments(copy_data, house_one, house_two)

            copy_data.add_cables() #only should have to do this for two switched houses

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


def random_solution(houses: dict[int, House], batteries: dict[int, Battery]) -> Data:
    """
    Returns data object which has been solved by the random algorithm and alreay has the segments and costs calculated.
    """
    data: Data = random_algorithm(houses, batteries)
    data.add_cables()
    data.cost_with_overlay()

    return data


def restart_hillclimber(houses, batteries) -> dict[int, Data]:
    """"
    Returns dictionary that contains data object of all hill climber runs (key = number of run, value = data object).
    Hill climber algorithm that restarts for x amount of times if after n-runs no beter solution has been found.
    """
    results = {}
    total_hillclimbers: int = 0
    while total_hillclimbers < 1:
        data: Data = random_solution(houses, batteries)

        while data.depth < 10:
            data = switch(data)
            
        data.algorithm_used = "hill climber"
        data.base = "random"

        print(f"run: {total_hillclimbers}\t| cost: {data.cost}\t| depth : {data.depth}")
        results[total_hillclimbers + 1] = data
        total_hillclimbers += 1

            
    save_data(results)
    print(results)
    sketch(results)
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

    

