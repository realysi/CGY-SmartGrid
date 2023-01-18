from code.read import read_data
from code.classes.data import Data
from code.classes.best_score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from sys import argv
from code.algorithms.random_algorithm import random_algorithm

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""


if __name__ == "__main__":    
    # Read in the data
    info: Data = read_data()

    # Algorithm of choice
    final_score = Score() 
    for i in range(100):
        data: Data = random_algorithm(info.houses, info.batteries) # Returns dictionaries = [copy_houses, copy_batteries]
        # calculate distance (for now) -> later do this by path
        data.add_cables()
        for j in data.cables:
            data.cables[j].calculate_distance()
        score = data.costs()
        final_score.add_score(score, data)
    final_score.calculate_average_score()
    data_best_score = final_score.best_data
    print(final_score)
    
    #output file
    output_file(data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    #plot the grid with all its data:
    plot_grid(data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    