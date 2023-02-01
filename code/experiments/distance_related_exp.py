from code.algorithms.distance_related_algorithm import start_distance
import time
import csv


def test_distance_district_1(houses, batteries):

    parameters = []

    #parameters
    switch_sorting = 20 # Switch_sorting after amount of runs otherwise the same house gets shuffled over and over
    amount_of_houses_to_remove = 1  # Amount of houses to remove per shuffle
    capacity_border = 1 # Capacity border for battery, so only shuffle battery with available space > x
    amount_of_runs = 5 # Amount of runs to run the algorithm

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
        for score in range(len(scores.all_scores)):
            row = [scores.switch_per_run[score],scores.all_scores[score], switch_sorting, amount_of_houses_to_remove, capacity_border, amount_of_runs ]
            csv_writer.writerow(row)

    # new parameters
    parameters_1 = []

    #parameters
    switch_sorting = 5
    amount_of_houses_to_remove = 2
    capacity_border = 1
    amount_of_runs = 5

    #add the parameters
    parameters_1.append(switch_sorting)
    parameters_1.append(amount_of_houses_to_remove)
    parameters_1.append(capacity_border)
    parameters_1.append(amount_of_runs)

    scores_1 = start_distance(houses, batteries, parameters_1)

    print(scores_1.all_scores)

    filename = "results/distance.csv"

    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        for score in range(len(scores_1.all_scores)):
            row = [scores.switch_per_run[score],scores.all_scores[score], switch_sorting, amount_of_houses_to_remove, capacity_border, amount_of_runs ]
            csv_writer.writerow(row)



       