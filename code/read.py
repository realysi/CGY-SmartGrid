import csv
from .classes.battery import Battery
from .classes.house import House
from sys import argv

"""

This file is used to read the data from the csv files and to store this data
inside of objects. 

"""
def select_district():
    if len(argv) < 2:
        print("Usage: --district (filenumber)")
        quit()
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

def read_houses(relative_path_houses: str):
    # Dictionary containing data of houses
    # Indexing of dictionary: [0]connection, [1]to_bat, [2]x, [3]y, [4]max_output
    houses = {}

    with open(relative_path_houses, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        id_house = 0
        for row in csv_reader:
            if id_house != 0: # Skip first line of file
                house = House(int(row[0]), int(row[1]), float(row[2]), id_house)
                houses[house.id] = house
            id_house += 1
    return houses

def read_batteries(relative_path_batteries: str):  
    # Dictionary containing data of batteries
    batteries = {}

    with open(relative_path_batteries, mode='r') as csv_file:
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
    battery_link = select_district()[1]
    houses = read_houses(house_link)
    batteries = read_batteries(battery_link)
    dictionaries = [houses, batteries]
    return dictionaries
