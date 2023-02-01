from code.read import read_data
from code.classes.data import Data
from code.classes.score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.visualisation.histogram import plot_histogram
from code.algorithms.cluster_algorithm import cluster_algorithm
from sys import argv
from code.algorithms.random_algorithm import start_random
from code.algorithms.distance_related_algorithm import start_distance
from code.experiments.distance_related_exp import test_distance_district
from code.experiments.random_exp import test_random
import time

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""
start_time = time.time()


if __name__ == "__main__":    
    # Read in the raw data
    raw_data: Data = read_data()

    # Runs the chosen algorithm
    if argv[3] == "random":
        if len(argv) == 5:
            scores = test_random(raw_data.houses, raw_data.batteries)
            data_best_score: Data = scores.best_data
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs'")
            raise SystemExit
    elif argv[3] == "distance":
        if len(argv) == 7:
            #scores = start_distance(raw_data.houses, raw_data.batteries)
            scores = test_distance_district(raw_data.houses, raw_data.batteries)
            data_best_score: Data = scores.best_data
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs' 'amount_of_houses_to_remove' 'capacity_border'")
            raise SystemExit
    elif argv[3] == "hillclimber":
        pass
    elif argv[3] == "cluster":
        if len(argv) == 5:
            for run in range(int(argv[4])):
                data = cluster_algorithm(raw_data.houses, raw_data.batteries)
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs'")
            raise SystemExit
        pass
    

    # Plot histogram
    #output_file(data_best_score.houses, data_best_score.batteries)
    plot_histogram()
    #plot_grid(data_best_score.houses, data_best_score.batteries, data_best_score.cables)

