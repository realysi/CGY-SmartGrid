from code.read import read_data
from code.classes.data import Data
from code.classes.cable import Cable
from code.classes.battery import Battery
from code.classes.scores import Score
from code.visualisation.output import output_file
from code.visualisation.grid import plot_grid
from sys import argv
from code.algorithms.random_algorithm import random_algorithm

"""

Main file which is used to call all other functions in other files.

Usage: --district {number of district the user would like to select}.

"""



if __name__ == "__main__":    
    # Read in the data
    info: Data = read_data()

    # Algorithm of choice
    scores = {} # dict to compare the results of an algorithm that runs n times
    score = Score()
    for i in range(1,101):
        data: Data = random_algorithm(info.houses, info.batteries) # Returns dictionaries = [copy_houses, copy_batteries]
        # calculate distance (for now) -> later do this by path
        data.add_cables()
        for i in data.cables:
            data.cables[i].calculate_distance()
        data.costs()

        #cost = data.costs()
        score.score_append(i, data)
        score.score_data()
    print(score)

    #output file
    output_file(score.scores[score.best_score_id].houses, score.scores[score.best_score_id].batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    #plot the grid with all its data:
    plot_grid(score.scores[score.best_score_id].houses, score.scores[score.best_score_id].batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    #plot_grid(data_best_score.houses, data_best_score.batteries)
    

    #data_best_score.houses, data_best_score.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

