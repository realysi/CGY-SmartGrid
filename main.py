from code.classes.data import Data
from code.read import read_data
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.algorithms.cluster_algorithm import cluster_algorithm
from code.algorithms.random_algorithm import start_random
from code.algorithms.distance_related_algorithm import start_distance
from code.experiments.hillclimber_exp import hillclimber_random, restart_hillclimber_random, data_restart
import time
from sys import argv

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select} {Parameters}.

"""
start_time = time.time()


if __name__ == "__main__":    
    # Read in the raw data
    raw_data: Data = read_data()

    # Runs the chosen algorithm
    if argv[3] == "random":
        #4 = runs
        if len(argv) == 5:
            scores = start_random(raw_data.houses, raw_data.batteries)
            data_best_score: Data = scores.best_data
            output_file(data_best_score.houses, data_best_score.batteries)
            plot_grid(data_best_score.houses, data_best_score.batteries, data_best_score.cables)
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs'")
            raise SystemExit
    elif argv[3] == "distance":
        #4 = runs, 5 = houses to remove per shuffle, 6 = capacity border for the battery
        if len(argv) == 7:
            scores = start_distance(raw_data.houses, raw_data.batteries)
            data_best_score: Data = scores.best_data
            output_file(data_best_score.houses, data_best_score.batteries)
            plot_grid(data_best_score.houses, data_best_score.batteries, data_best_score.cables)
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs' 'amount_of_houses_to_remove' 'capacity_border'")
            raise SystemExit
    elif argv[3] == "hillclimber":
        #argv[3] = hillclimber, argv[4] = base (random or greedy), argv[5] = houses to switch, argv[6] = depth
        if argv[4] == "random":
            data = hillclimber_random(raw_data.houses, raw_data.batteries, int(argv[5]), int(argv[6]))
            output_file(data.houses, data.batteries)
            plot_grid(data.houses, data.batteries, data.cables)         
    elif argv[3] == "restart_hillclimber":
        #argv[3] = hillclimber, argv[4] = base (random or greedy), argv[5] = houses to switch, argv[6] = depth, argv[7] = restarts
        if argv[4] == "random":
            data_dictionary = restart_hillclimber_random(raw_data.houses, raw_data.batteries, int(argv[5]), int(argv[6]), int(argv[7]))
            data = data_restart(data_dictionary)
            output_file(data.houses, data.batteries)
            plot_grid(data.houses, data.batteries, data.cables)
    elif argv[3] == "cluster":
         #3 = name, 4 = runs
        if len(argv) == 5:
            for run in range(int(argv[4])):
                data = cluster_algorithm(raw_data.houses, raw_data.batteries)
                output_file(data.houses, data.batteries)
                plot_grid(data.houses, data.batteries, data.cables)
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs'")
            raise SystemExit
        pass
    else:
        print("Usage: --district (filenumber) 'algorithm' 'parameters'")
        raise SystemExit