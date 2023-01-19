from code.read import read_data
from code.classes.data import Data
from code.classes.score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from sys import argv
from code.algorithms.random_algorithm import random_algorithm

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""


if __name__ == "__main__":    
    # Read in the raw data
    raw_data: Data = read_data()

    # Create score object for all runs
    final_score: Score = Score() 
    for run in range(2):
        # Applies algorithm to data set, makes connections between houses and batteries
        data: Data = random_algorithm(raw_data.houses, raw_data.batteries)
        data.add_cables()
        for j in data.cables:
            data.cables[j].calculate_distance()
        score = data.cables_cost()
        final_score.add_score(score, data)

    final_score.calculate_average_score()
    data_best_score: Data = final_score.best_data
    print(final_score)
    
    for i in data_best_score.cables:
        data_best_score.cables[i].calculate_segments()

    #output file
    output_file(data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    #plot the grid with all its data:
    plot_grid(data_best_score.houses, data_best_score.batteries, data_best_score.cables) #creates outputfile which contains data of both dictionaries -> see output.txt

    