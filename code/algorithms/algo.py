from ..read import houses
from ..read import batteries
import random
from ..classes.house import House
from ..classes.battery import Battery

"""
This algorithm works with the basis of the knapsack problem.
It wil first select a random battery, fill this untill its capacity can't add another house
Then it will move on to the next battery. The houses will be chosen randomly.

Aantekening: Werkt soms in 1 keer, maar andere keren met een miljoen repetities niet??
"""
def order_houses():
    id_keys = []
    for i in houses:
        id_keys.append(houses[i].id)
    return id_keys

def order_batteries():
    id_keys = []
    for i in batteries:
        id_keys.append(batteries[i].id)
    return id_keys

def random_battery_order():
    id_keys = order_batteries()
    random.shuffle(id_keys)
    return id_keys

def random_house_order():
    id_keys = order_houses()
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

def mistakes():
    mistakes = False
    for i in houses:
        if houses[i].to_battery == False:
            mistakes = True
    return mistakes

#echt helemaal random:
def main():
    battery_order = random_battery_order()  #random
    house_order = order_houses()
    for i in house_order:
        house = houses[i]   #house class
        if house.max_output > house_order[0]:
            buffer = house_order[0]
            house.id = house_order[0]
            buffer = house_order[i]
    print(house_order)

    """
    for i in battery_order:
        battery = batteries[i]  #battery class
        for j in house_order:
            house = houses[j]   #house class
            if fits(battery, house):
                subtract(battery, house)
    print(batteries)
    """
      

print(main())


"""
#echt helemaal random:
def main():
    battery_order = random_battery_order()
    house_order = random_house_order()

    for i in battery_order:
        battery = batteries[i]  #battery class
        for j in house_order:
            house = houses[j]   #house class
            print(battery.id, battery.capacity)
            if fits(battery, house):
                subtract(battery, house)
            else:
                continue
"""