from code.read import read_data
from code.classes.data import Data
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from code.visualisation.histogram import plot_histogram
from code.algorithms.cluster_algorithm import cluster_algorithm
from sys import argv
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.distance_related_algorithm import start_distance
import time
import csv


def test_distance_district_1(houses, batteries):

    parameters = []

    #parameters
    switch_sorting = 20
    amount_of_houses_to_remove = 1
    capacity_border = 1
    amount_of_runs = 5

    #add the parameters
    parameters.append(switch_sorting)
    parameters.append(amount_of_houses_to_remove)
    parameters.append(capacity_border)
    parameters.append(amount_of_runs)

    scores = start_distance(houses, batteries, parameters)

    print(scores.all_scores)

    filename = "results/distance.csv"

    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        fields = ["Switches", "Score", "Amount switch_sorting", "Amount of houses to remove", "Amount of capacity border", "Amount of runs"]
        csv_writer.writerow(fields)
        for score in range(len(scores.all_scores)):
            row = [scores.switch_per_run[score],scores.all_scores[score], switch_sorting, amount_of_houses_to_remove, capacity_border, amount_of_runs ]
            csv_writer.writerow(row)

    # new parameters
    parameters_1 = []

    #parameters
    switch_sorting = 5
    amount_of_houses_to_remove = 1
    capacity_border = 1
    amount_of_runs = 1

    #add the parameters
    parameters_1.append(switch_sorting)
    parameters_1.append(amount_of_houses_to_remove)
    parameters_1.append(capacity_border)
    parameters_1.append(amount_of_runs)

    scores_1 = start_distance(houses, batteries, parameters_1)

    filename = "results/distance.csv"

    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        fields = ["Switches", "Score", "Amount switch_sorting", "Amount of houses to remove", "Amount of capacity border", "Amount of runs"]
        csv_writer.writerow(fields)
        for score in range(len(scores.all_scores)):
            row = [scores.switch_per_run[score],scores.all_scores[score], switch_sorting, amount_of_houses_to_remove, capacity_border, amount_of_runs ]
            csv_writer.writerow(row)



       