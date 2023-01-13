from ..read import houses
from ..read import batteries
import random
from .code.classes.house import House
from .code.classes.battery import Battery

"""
This algorithm works with the basis of the knapsack problem.
It wil first select a random battery, fill this untill its capacity can't add another house
Then it will move on to the next battery. The houses will be chosen randomly.
"""

def random_battery_order():
    id_keys = []
    for i in batteries:
        id_keys.append(batteries[i].id)
    random.shuffle(id_keys)
    return id_keys

def random_house_order():
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
        house.to_battery = battery.id

def move_on():
    pass

def mistakes() -> bool:
    mistakes = False

    for i in houses:
        if houses[i].to_battery == False:
            mistakes = True

    if mistakes == False:
        return False
    else:
        return True
        
def main():
    while True:
        battery_order = random_battery_order()
        house_order = random_house_order()

        for i in battery_order:
            battery = batteries[i]  #battery class

            for j in house_order:
                house = houses[j]   #house class
                if fits(battery, house):
                    subtract(battery, house) 
                    
                else:
                    continue

        #repeat
        if mistakes():
            continue
        else:
            for i in batteries:
                print(batteries[i].id, batteries[i].capacity, sorted(batteries[i].to_houses))
            print(houses)
            break    
    return "yesss"




print(main())