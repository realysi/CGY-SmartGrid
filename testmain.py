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
from code.experiments.distance_related_exp import test_distance_district_1
from code.experiments.hillclimber_exp import hillclimber_random, hillclimber_greedy, restart_hillclimber_random, restart_hillclimber_greedy
import time

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""
start_time = time.time()


if _name_ == "_main_":    
    # Read in the raw data
    raw_data: Data = read_data()

    # Runs the chosen algorithm
    if argv[3] == "random":
        if len(argv) == 5:
            scores = start_random(raw_data.houses, raw_data.batteries)
            data_best_score: Data = scores.best_data
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs'")
            raise SystemExit
    if argv[3] == "distance":
        if len(argv) == 7:
            scores = start_distance(raw_data.houses, raw_data.batteries)
            data_best_score: Data = scores.best_data
        else:
            print("Usage: --district (filenumber) 'algorithm' 'amount of runs' 'amount_of_houses_to_remove' 'capacity_border'")
            raise SystemExit
    if argv[3] == "hillclimber":
        #3 = name, 4 = base, 5 = houses, 6 = depth
        if argv[4] == "random":
            data = hillclimber_random(raw_data.houses, raw_data.batteries, int(argv[5]), int(argv[6]))
        elif argv[4] == "greedy":
            data = hillclimber_greedy(raw_data.houses, raw_data.batteries, int(argv[5]), int(argv[6]))
    if argv[3] == "restart_hillclimber":
        #3 = name, 4 = base, 5 = houses, 6 = depth, 7=restarts
        if argv[4] == "random":
            data = restart_hillclimber_random(raw_data.houses, raw_data.batteries, int(argv[5]), int(argv[6]), int(argv[7]))
        elif argv[4] == "greedy":
            data = restart_hillclimber_greedy(raw_data.houses, raw_data.batteries, int(argv[5]), int(argv[6]), int(argv[7]))

    if argv[3] == "cluster":
        pass