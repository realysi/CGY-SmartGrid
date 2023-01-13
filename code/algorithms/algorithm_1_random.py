from data import houses, batteries
import random
from random import randint, shuffle

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

def fits(capacity, max_output):
    if capacity - max_output > 0:
        return True
    else:
        return False

"""
def naam(order_batteries, order_houses): 
    amount = 0
    for i in order_batteries:
        id_current_battery = i
        current_battery = batteries[id_current_battery] #current_battery is class of type Battery


        for i in order_houses:
            id_current_house = i
            current_house = houses[id_current_house] #current_battery is class of type Battery
            current_battery.capacity -= current_battery.max_output 
            print(current_house)
            amount += 1
    print(amount)
    return "iets"
"""

print(fits(100, 100))