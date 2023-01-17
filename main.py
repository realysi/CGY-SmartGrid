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


# function to calculate the avg of the scores
def average(dict):
    scores = 0
    for score in dict.values():
        scores += score
    average_score = scores / len(dict)
    return average_score


if __name__ == "__main__":    
    # Read in the data
    info: Data = read_data()

    # Algorithm of choice
    scores = {} # dict to compare the results of an algorithm that runs n times
    for i in range(10):
        data: Data = random_algorithm(info.houses, info.batteries) # Returns dictionaries = [copy_houses, copy_batteries]
        # calculate distance (for now) -> later do this by path
        new_data = cables(data)
        for i in new_data.cables:
            new_data.cables[i].calculate_distance()
        cost = new_data.costs()
        scores[data] = cost # track all scores in a dictionary 

    print(f"Average:", average(scores)) # prints the average
    best_score =  min(scores.items(), key=lambda x: x[1]) # gets the best score by comparing the values in the dictionary
    data_best_score = best_score[0] # gives back the key of the best score which contains the data of that score
    print(f"Best score:", best_score[1]) # prints the best costs

    #output file
    output_file(data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    #plot the grid with all its data:
    plot_grid(data_best_score.houses, data_best_score.batteries)
    

    

