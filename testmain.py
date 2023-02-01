from code.read import read_data
from code.classes.data import Data
from code.classes.score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.visualisation.histogram import plot_histogram
from code.algorithms.cluster_algorithm import cluster_algorithm
from sys import argv
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.distance_related_algorithm import start_distance
from code.experiments.distance_related_exp import test_distance_district_1
import time

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""
start_time = time.time()


if __name__ == "__main__":    
    # Read in the raw data
    raw_data: Data = read_data()

    # Run algorithm
    scores = test_distance_district_1(raw_data.houses, raw_data.batteries)