import csv
from code.classes.battery import Battery
from code.classes.house import House
from sys import argv

"""
This file is used to read the data from the csv files and to store this data
inside of objects. 

Usage: --district {number of district the user would like to select}.

"""
def select_district():
    if argv[1] != "--district":
        print("Usage: --district (filenumber)")
        quit()
    else:
        file_number = int(argv[2])
        if file_number > 4:
            quit()

    districts = {} # Dictonary to save the relative paths (both houses & batteries) for each district
    for i in range(1, 5):
        districts[i] = [f"data/district_{str(i)}/district-{str(i)}_houses.csv", 
        f"data/district_{str(i)}/district-{str(i)}_batteries.csv"]

    house_link = districts[file_number][0]
    battery_link = districts[file_number][1]

    links_data = [house_link, battery_link]
    return links_data

def read_houses(relative_link_houses):
    # Dictionary containing data of houses
    # Indexing of dictionary: [0]connection, [1]to_bat, [2]x, [3]y, [4]max_output
    houses = {}

    with open(relative_link_houses, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        id_house = 0
        for row in csv_reader:
            if id_house != 0: # Skip first line of file
                house = House(int(row[0]), int(row[1]), float(row[2]), id_house)
                houses[house.id] = house
            id_house += 1
    
    return houses

def read_batteries(relative_link_batteries):  
    # Dictionary containing data of batteries
    batteries = {}

    with open(relative_link_batteries, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        id_battery = 0
        for row in csv_reader:
            if id_battery != 0: #skip eerste line 
                battery = Battery(int(row[0]), int(row[1]), float(row[2]), id_battery)
                batteries[battery.id] = battery
            id_battery += 1

    return batteries

def read_data():
    house_link = select_district()[0]
    return house_link

# Data outputs
"""
Om de data te visualizeren, zal wat data worden gegenereerd in data.txt. 
Elke keer wanneer data.py zal worden gerund, zal data.txt worden overgeschreven.
"""
def output_file():
    with open('output.txt', 'w') as data:
        total_output = 0
        for i in houses:
            total_output += houses[i].max_output
        data.write(f"Sum max_outputs:\t {total_output} \n\n")
        for i in batteries:
            data.write(f"ID:{i} \t {batteries[i]} \n")
        for i in houses:
            data.write(f"ID:{i} \t {houses[i]} \n")
    return "Output generated"

