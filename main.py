from code.read import read_data
from code.classes.data import Data
from code.classes.cable import Cable
from code.classes.battery import Battery
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from sys import argv
from code.algorithms.random_algorithm import random_algorithm

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""

def cables(data: Data):    #nog even ergens anders plakken en aanpassen
        cables = {}
        for i in data.houses:
            designated_battery_id = data.houses[i].to_battery
            designated_battery = data.batteries[designated_battery_id]
            cable = Cable(data.houses[i], designated_battery)
            cables[data.houses[i].id] = cable #Key = house.id: Value = Cable
        new_data = Data(data.houses, data.batteries, cables)
        return new_data

if __name__ == "__main__":    
    # Read in the data
    info: Data = read_data()

    # Algorithm of choice
    data: Data = random_algorithm(info.houses, info.batteries) # Returns dictionaries = [copy_houses, copy_batteries]

    # calculate distance (for now) -> later do this by path
    new_data = cables(data)
    for i in new_data.cables:
        new_data.cables[i].calculate_distance()
    cost = new_data.costs()

    print(f"House: {new_data.cables[i].house.id} to Battery: {new_data.cables[i].battery.id} | distance = {new_data.cables[i].distance}")
    print(f"total cost: {new_data.costs()}")

    #output file
    output_file(data.houses, data.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    #plot the grid with all its data:
    plot_grid(data.houses, data.batteries)
    

    

