from code.algorithms.distance_related_algorithm import start_distance
import csv
from sys import argv


def test_distance_district(houses, batteries):

    scores = start_distance(houses, batteries)

    filename = "results/distance/distance_district_3.csv"

    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        for score in range(len(scores.all_scores)):
            row = [scores.switch_per_run[score],scores.all_scores[score]]
            csv_writer.writerow(row)
    return scores