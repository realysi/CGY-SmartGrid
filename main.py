from code.read import read_data
from code.classes.data import Data
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
    data: Data = random_algorithm(info.houses, info.batteries) # Returns dictionaries = [copy_houses, copy_batteries]
    output_file(data.houses, data.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt



    # calculate paths 

    #plot the grid with all its data:
    plot_grid(data.houses, data.batteries)
    

    

