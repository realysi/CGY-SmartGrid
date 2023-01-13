"""
Info:
Name algorithm: random_algorithm
Case: Smartgrid (Teamname: CGY-SmartGrid)

Summary: 
This algorithm solves this smartgrid problem by looking at it as a knapsack problem.
In this case there are 5 knapsacks, which together have to contain 150 objects (houses).
This is solved by randomly selecting a battery and fill this with random houses untill there are no more houses 
left that can fit inside the current battery. Then it moves on to the next battery and does the same thing, etc.
When the last battery has run out of capacity, a check will be performed to see whether all houses are connected to a battery
In that case the algorithm yields a result. Otherwise the algorithm will start again untill the check is passed.

Example:
->begin<-
normal battery order [1,2,3,4,5] -> random order [3,5,2,4,1]
normal house order [1,2,3,4,5] -> random order [4,1,5,3,2]
Fill battery 4 untill full -> fill battery 3 untill full -> etc
Check if all houses are connectec to a battery? Yes --> results | No --> start again at begin
"""

import random
from battery import Battery
from house import House
import copy

def random_battery_order(batteries):
    id_keys = []
    for i in batteries:
        id_keys.append(batteries[i].id)
    random.shuffle(id_keys)
    return id_keys

def random_house_order(houses):
    id_keys = []
    for i in houses:
        id_keys.append(houses[i].id)
    random.shuffle(id_keys)
    return id_keys

def fits(battery: Battery, house: House):
    if battery.capacity - house.max_output > 0.0:
        return True

def subtract(battery: Battery, house: House):
    if house.to_battery == False:
        battery.capacity -= house.max_output
        battery.to_houses.append(house.id)
        battery.connections += 1
        house.to_battery = battery.id

def move_on():
    pass

def mistakes(houses) -> bool:
    mistakes = False

    for i in houses:
        if houses[i].to_battery == False:
            mistakes = True

    if mistakes == False:
        return False
    else:
        return True

        
def random_algorithm(houses, batteries):
    while True:
        copy_houses = copy.deepcopy(houses) #make a deepcopy of the houses dictionary
        copy_batteries = copy.deepcopy(batteries) #make a deepcopy of the batteries dictionary
        battery_order = random_battery_order(copy_batteries) #list of battery id's which are randomly shuffeled. 
        house_order = random_house_order(copy_houses) #list of house id's which are randomly shuffeled. 

        for i in battery_order:
            battery = copy_batteries[i]  #battery class

            for j in house_order:
                house = copy_houses[j]   #house class
                if fits(battery, house):
                    subtract(battery, house) 
                else:
                    continue

        #repeat
        if mistakes(copy_houses):
            #print(house_order)
            continue
        else:
            break    

    dictionaries = [copy_houses, copy_batteries]

    return dictionaries
