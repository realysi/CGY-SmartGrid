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

def hillclimber_random_2opt(houses, batteries):
    #--- Experiment algorithm ---
    data: Data = random_solution(houses, batteries)

    while data.depth < 10:
        data = switch(data)
        
    data.algorithm_used, data.base = "hillclimber", "random"

    #--- Data output --- 
    fields = ["Depth", "Cost", "Algorithm", "Base"]
    filename = "hillclimber_random.csv"
    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        fields = ["Depth", "Cost", "Algorithm", "Base"]
        row = [data.depth, data.cost, data.algorithm_used, data.base]
        csv_writer.writerow(fields)
        csv_writer.writerow(row)

    return data
    

def restart_hillclimber_random_2opt(houses, batteries) -> dict[int, Data]:
    #--- Experiment algorithm --- 
    results = {}
    total_hillclimbers: int = 0
    while total_hillclimbers < 1:
        data: Data = random_solution(houses, batteries)

        while data.depth < 10:
            data = switch(data)
            
        data.algorithm_used, data.base = "restart_hillclimber", "random"

        print(f"run: {total_hillclimbers}\t| cost: {data.cost}\t| depth : {data.depth}")
        results[total_hillclimbers + 1] = data
        total_hillclimbers += 1

        #--- Data output ----
        fields = ["Run", "Depth", "Cost", "Algorithm", "Base"]
        filename = "restart_hillclimber_random.csv"

        with open(filename, "w") as csvfile:
            csv_writer = csv.writer(csvfile)

            csv_writer.writerow(fields)
            for i in results:
                run, depth, cost, algo, algo_base = i, results[i].depth, results[i].cost, results[i].algorithm_used, results[i].base
                row = [run, depth, cost, algo, algo_base]
                csv_writer.writerows([row])
            
    return results






def save_data(results: dict[int, Data]):
    fields = ["Run", "Depth", "Cost", "Algorithm", "Base"]
    filename = "hillclimber.csv"

    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(fields)
        for i in results:
            run = i
            depth = results[i].depth
            cost = results[i].cost
            algo = results[i].algorithm_used
            algo_base = results[i].base
            row = [run, depth, cost, algo, algo_base]
            csv_writer.writerows([row])