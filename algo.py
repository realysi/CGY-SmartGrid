#Yanick
import random
from battery import Battery
from house import House
import copy

"""
This algorithm works with the basis of the knapsack problem.
It wil first select a random battery, fill this untill its capacity can't add another house
Then it will move on to the next battery. The houses will be chosen randomly.
"""

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

        
def algo(houses, batteries):
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
            for i in copy_batteries:
                print(copy_batteries[i].id, copy_batteries[i].capacity, sorted(copy_batteries[i].to_houses))
            print(copy_houses)
            
            break    

    dictionaries = [copy_houses, copy_batteries]
    print("gelukt babyyyyy")
    return dictionaries
