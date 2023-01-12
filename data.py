import csv
from objects import House, Battery
import argparse

"""
argparse uitgelegd:
voeg na de gebruikelijke "python3 filename" de vlag --disctrict toe met daarachter 1 2 of 3 om aan te geven
welke dataset van de drie districten je wil verwerken. Met een getal groter dan 3 kom je hier ook door, maarrr
dan wordt er geen data verwerkt.

pip3 install argparse
"""

parser = argparse.ArgumentParser()
parser.add_argument('--district', type=int, required=True, help="Select district 1, 2 or 3")
args = parser.parse_args()

districten = {} #dictonary to save the relative paths (both house & battery) for each district
for i in range(1, 4):
    districten[i] = [f"Huizen&Batterijen/district_{str(i)}/district-{str(i)}_houses.csv", 
    f"Huizen&Batterijen/district_{str(i)}/district-{str(i)}_batteries.csv"]

house_link = districten[args.district][0]
battery_link = districten[args.district][1]

#Data of houses
#indexing of dictionary: [0]connection, [1]to_bat, [2]x, [3]y, [4]max_output
houses = {}

with open(house_link, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    id_house = 0
    for row in csv_reader:
        if id_house != 0: #skip eerste line 
            house = House(int(row[0]), int(row[1]), float(row[2]), id_house)
            houses[id_house] = [house.connection, house.to_bat, house.x, house.y, house.max_output]
        id_house += 1
    
#Data van batterijen
#indexing of dictionary: [0]to_houses, [1]capacity, [2]x, [3]y
batteries = {}

with open(battery_link, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    id_battery = 0
    for row in csv_reader:
        if id_battery != 0: #skip eerste line 
            battery = Battery(int(row[0]), int(row[1]), float(row[2]), id_battery)
            batteries[id_battery] = [battery.to_houses, battery.capacity, battery.x, battery.y]
        id_battery += 1


# Data outputs
"""
Om de data te visualizeren, zal wat data worden gegenereerd in data.txt. 
Elke keer wanneer data_pro.py zal worden gerund, zal data.txt worden overgeschreven.
"""
with open('data.txt', 'w') as data:
    total_output = 0
    for i in houses:
        total_output += houses[i][4]
    data.write(f"Sum max_outputs:\t {total_output} \n\n")
    for i in houses:
        data.write(f"ID:{i} \t {houses[i]} \n")



"""
Links:
https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
"""
