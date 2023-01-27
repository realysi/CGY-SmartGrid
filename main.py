from code.read import read_data
from code.classes.data import Data
from code.classes.score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.visualisation.histogram import plot_histogram
from sys import argv
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.distance_related_algorithm import distance_algorithm
import time

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""
start_time = time.time()


if __name__ == "__main__":    
    # Read in the raw data
    raw_data: Data = read_data()

    # List for histogram
    all_scores = []

    # Create score object for all runs
    final_score: Score = Score() 

    #run a certain algorithm for a specified number of times
    for run in range(100):
        # Applies algorithm to data set, makes connections between houses and batteries
        data: Data = random_algorithm(raw_data.houses, raw_data.batteries) #algorithm of choice
        data.add_cables()
        score = data.cables_cost()
        all_scores.append(score)
        final_score.add_score(score, data)

    #calculate average score, save dataset of best score

    average_score = final_score.calculate_average_score()
    data_best_score: Data = final_score.best_data

    #data_best_score.overlay() --> DIT IS CODE VOOR DE OVERLAY UPDATE
    print(final_score)


    print("--- %s seconds ---" % (time.time() - start_time))

    #plot the histogram
    #plot_histogram(all_scores, average_score)

    #output file
    output_file(data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt
    
    #plot the data
    plot_histogram(all_scores, average_score)
    plot_grid(data_best_score.houses, data_best_score.batteries, data_best_score.cables) #creates outputfile which contains data of both dictionaries -> see output.txt
