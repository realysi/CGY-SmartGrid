from code.read import read_data
from code.classes.data import Data
from code.classes.cluster import make_clusters
from code.classes.score import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.visualisation.histogram import plot_histogram
from sys import argv
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.distance_relatable_algorithm import distance_algorithm
import time

if __name__ == "__main__":    
    # Read in the raw data
    raw_data: Data = read_data()

    make_clusters(raw_data.houses)