from code.read import read_data
from code.classes.data import Data
from code.classes.score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.visualisation.histogram import plot_histogram
from sys import argv
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.cluster_algorithm import cluster_algorithm

from code.algorithms.distance_related_algorithm import distance_algorithm
from code.algorithms.hillclimber import restart_hillclimber

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
    # cluster_algorithm(raw_data.houses, raw_data.batteries)
    data = random_algorithm(raw_data.houses, raw_data.batteries)
    data.add_cables()
    plot_grid(data.houses, data.batteries, data.cables)


    # List for histogram
    all_scores = []

    # Create score object for all runs
    final_score: Score = Score() 

    #stukje van Yanick voor testen hillclimber algoritme
    data = restart_hillclimber(raw_data.houses, raw_data.batteries)
    #data: Data = hillclimber(raw_data.houses, raw_data.batteries)
    #plot_grid(data.houses, data.batteries, data.cables) #creates outputfile which contains data of both dictionaries -> see output.txt
    #for i in data.cables:
        #print(f"ID: {data.cables[i].house.id}")
        #print(f"BAT ID: {data.cables[i].battery.id} | Capacity: {data.cables[i].battery.capacity} | {data.cables[i].battery.to_houses}")
        #print(f"{data.cables[i].segments}")

    print(f"SCORE: {data.cost}")

    #- van Christos # Run distance algorithm (Need to check how it works with data object)

    houses = raw_data.houses
    batteries = raw_data.batteries
    data = distance_algorithm(houses, batteries)

    #run a certain algorithm for a specified number of times
    data.add_cables()
    #score = data.cables_cost_no_overlap()
    score = data.cost_with_overlay()
    all_scores.append(score)
    final_score.add_score(score, data)


    
    #calculate average score, save dataset of best score

    average_score = final_score.calculate_average_score()
    data_best_score: Data = final_score.best_data

    #data_best_score.overlay() --> DIT IS CODE VOOR DE OVERLAY UPDATE
    print(final_score)


    print("--- %s seconds ---" % (time.time() - start_time))

    output_file(data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt
    
    # Plot the dat  a
    plot_histogram(all_scores, average_score)
    plot_grid(data_best_score.houses, data_best_score.batteries, data_best_score.cables) #creates outputfile which contains data of both dictionaries -> see output.txt
