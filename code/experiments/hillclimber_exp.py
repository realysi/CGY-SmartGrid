import csv
from matplotlib import pyplot as plt
from code.algorithms.random_algorithm import random_algorithm
from code.algorithms.hillclimber import * #dit moet nog netter worden gemaakt ofc
from code.classes.data import Data
from code.classes.house import House
from code.classes.battery import Battery
from code.visualisation.hillclimber_views import sketch
from code.algorithms.distance_related_algorithm import distance_algorithm #, exp_greedy_algorithm
import random
import copy


def open_temporary_data(filename: str):
    """
    Data output
    Opens/creates the file to write all data from a specific algorithm to
    """
    with open(filename, "w") as csvfile:
        pass


def append_temporary_data(filename: str, depth: int, cost: int):
    """
    Data output
    For each iteration appends the depth and cost to the file opened by open_temporary_data()
    """
    with open(filename, "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        row: list[int] = [depth, cost]
        csv_writer.writerow(row)
        csvfile.close()


def data_hillclimber(data: Data, filename: str):
    """
    Data output
    Creates a .csv file with the end results of a single hillclimber run
    """
    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        fields= ["Depth", "Cost", "Swaps at a time", "Algorithm", "Base"]
        row = [data.depth, data.cost, data.swaps, data.algorithm_used, data.base]
        csv_writer.writerow(fields)
        csv_writer.writerow(row)


def data_restart_hillclimber(results: dict[int, Data], filename: str):
    """
    Data output
    Creates a .csv file with the end results of a multiple hillclimber runs
    """
    with open(filename, "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        fields = ["Run", "Depth", "Cost", "Swaps at a time", "Algorithm", "Base"]
        csv_writer.writerow(fields)
        for i in results:
            run, depth, cost, swaps, algo, algo_base = i, results[i].depth, results[i].cost, results[i].swaps, results[i].algorithm_used, results[i].base
            row = [run, depth, swaps, cost, algo, algo_base]
            csv_writer.writerows([row])


def hillclimber_random(houses: dict[int, House], batteries: dict[int, Battery], amount_of_houses: int, depth: int):
    """
    Returns a data object which is run through a hillclimber algorithm which starts with a random solution.
    Change limit if you want the algorithm to run deeper or less deep.
    """
    data: Data = random_solution(houses, batteries)
    limit = depth

    open_temporary_data("hillclimber_random_data.csv")

    while data.depth < limit:
        append_temporary_data("hillclimber_random_data.csv",data.depth, data.cost)
        data = switch(data, amount_of_houses, limit)

    append_temporary_data("hillclimber_random_data.csv",data.depth, data.cost)

    data.algorithm_used, data.base, data.swaps = "hillclimber", "random", amount_of_houses

    data_hillclimber(data, "hillclimber_random.csv")

    return data


def hillclimber_greedy(houses: dict[int, House], batteries: dict[int, Battery], amount_of_houses: int, depth: int):
    """
    Returns a data object which is run through a hillclimber algorithm which starts with a greedy solution
    Change limit if you want the algorithm to run deeper or less deep.
    """
    data: Data = exp_greedy_algorithm(houses, batteries)
    limit = depth

    open_temporary_data("hillclimber_greedy_data.csv")

    while data.depth < limit:
        append_temporary_data("hillclimber_greedy_data.csv",data.depth, data.cost)
        data = switch(data, amount_of_houses, limit)

    append_temporary_data("hillclimber_greedy_data.csv",data.depth, data.cost)
        
    data.algorithm_used, data.base, data.swaps = "hillclimber", "random", amount_of_houses

    data_hillclimber(data, "hillclimber_greedy.csv")

    return data


def restart_hillclimber_random(houses: dict[int, House], batteries: dict[int, Battery], amount_of_houses: int, depth: int, restarts: int) -> dict[int, Data]:
    """
    Algorithm
    Returns data objects which are run through a hillclimber algorithm which starts with a random solution
    Change limit if you want the algorithm to run deeper or less deep. Change < after total hillclimbers if you
    want more restarts.
    """
    results = {}
    total_hillclimbers: int = 0
    limit = depth

    while total_hillclimbers < restarts:
        data: Data = random_solution(houses, batteries)

        while data.depth < limit:
            data = switch(data, amount_of_houses, limit)
            
        data.algorithm_used, data.base, data.swaps = "restart_hillclimber", "random", amount_of_houses

        print(f"run: {total_hillclimbers}\t| cost: {data.cost}\t| depth : {data.depth}")
        results[total_hillclimbers + 1] = data
        total_hillclimbers += 1

    data_restart_hillclimber(results, "restart_hillclimber_random.csv")
            
    return results


def restart_hillclimber_greedy(houses: dict[int, House], batteries: dict[int, Battery], amount_of_houses: int, depth: int, restarts: int) -> dict[int, Data]:
    """
    Returns data objects which are run through a hillclimber algorithm which starts with a greedy solution.
    Change limit if you want the algorithm to run deeper or less deep. Change < after total hillclimbers if you
    want more restarts.
    """
    #--- Experiment algorithm --- 
    results = {}
    total_hillclimbers: int = 0
    limit = depth
    while total_hillclimbers < restarts:
        data: Data = exp_greedy_algorithm(houses, batteries)

        while data.depth < limit:
            data = switch(data, amount_of_houses, limit)
            
        data.algorithm_used, data.base, data.swaps = "restart_hillclimber", "random", amount_of_houses

        print(f"run: {total_hillclimbers}\t| cost: {data.cost}\t| depth : {data.depth}")
        results[total_hillclimbers + 1] = data
        total_hillclimbers += 1

    data_restart_hillclimber(results, "restart_hillclimber_greedy.csv")
            
    return results

def data_restart(data: dict[int, Data]):
    best_score = 1000000
    data_object_best_score = 0
    for data_object in data.values():
        current_score =  data_object.cost
        current_data_object = data_object
        if current_score < best_score:
            best_score = current_score
            data_object_best_score: Data = current_data_object
    return data_object_best_score