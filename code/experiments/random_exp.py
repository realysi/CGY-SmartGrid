from code.algorithms.random_algorithm import start_random
import csv
from sys import argv

def test_random(houses, batteries):

    scores = start_random(houses, batteries)

    filename = "results/random/random_district_1.csv"

    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        for score in range(len(scores.all_scores)):
            row = [scores.all_scores[score]]
            csv_writer.writerow(row)
    return scores