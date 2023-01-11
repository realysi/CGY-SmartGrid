import csv
from objects import House, Battery
from functions import total_output
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


#Data van huizen
output_houses = []  #array of all max-outputs from all the houses

with open(house_link, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count != 0: #skip eerste line 
            house = House(int(row[0]), int(row[1]), float(row[2]), line_count)
            output_houses.append(house.max_output)
            x = row[0]
            y = row[1]
            print(x, y)
        line_count += 1
    
#Data van batterijen
with open(battery_link, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0: #skip eerste line 
            x1 = row[0]
            y1 = row[1]
        line_count += 1

# Data outputs
sum_output = total_output(output_houses)
with open('data.txt', 'w') as a:
    a.write(f"Total output of houses: {sum_output}")



"""
Links:
https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3

https://www.tutorialspoint.com/how-can-i-plot-a-single-point-in-matplotlib-python
https://www.pythoncharts.com/matplotlib/customizing-grid-matplotlib/
https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot

"""

