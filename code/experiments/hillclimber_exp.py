import csv
from matplotlib import pyplot as plt
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.hillclimber import * #dit moet nog netter worden gemaakt ofc
from code.classes.data import Data
from code.classes.house import House
from code.classes.battery import Battery
from code.visualisation.hillclimber_views import sketch
import random
import copy

def hillclimber(houses, batteries):
    """"
    Returns dictionary that contains data object of all hill climber runs (key = number of run, value = data object).
    Hill climber algorithm that restarts for x amount of times if after n-runs no beter solution has been found.
    """
    data: Data = random_solution(houses, batteries)

    while data.depth < 10:
        data = switch(data)
        
    data.algorithm_used = "hill climber"
    data.base = "random"

    fields = ["Depth", "Cost", "Algorithm", "Base"]
    filename = "hillclimber.csv"

    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        fields = ["Depth", "Cost", "Algorithm", "Base"]
        row = [data.depth, data.cost, data.algorithm_used, data.base]
        csv_writer.writerow(fields)
        csv_writer.writerow(row)


    return data
    

def restart_hillclimber(houses, batteries) -> dict[int, Data]:
    """"
    Returns dictionary that contains data object of all hill climber runs (key = number of run, value = data object).
    Hill climber algorithm that restarts for x amount of times if after n-runs no beter solution has been found.
    """
    results = {}
    total_hillclimbers: int = 0
    while total_hillclimbers < 1:
        data: Data = random_solution(houses, batteries)

        while data.depth < 10:
            data = switch(data)
            
        data.algorithm_used = "hill climber"
        data.base = "random"

        print(f"run: {total_hillclimbers}\t| cost: {data.cost}\t| depth : {data.depth}")
        results[total_hillclimbers + 1] = data
        total_hillclimbers += 1

            
    save_data(results)
    print(results)
    sketch(results)
    return results






def save_data(dictionary: dict[int, Data]):
    fields = ["Run", "Depth", "Cost", "Algorithm", "Base"]
    filename = "hillclimber.csv"

    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(fields)
        for i in dictionary:
            run = i
            depth = dictionary[i].depth
            cost = dictionary[i].cost
            algo = dictionary[i].algorithm_used
            algo_base = dictionary[i].base
            row = [run, depth, cost, algo, algo_base]
            csv_writer.writerows([row])