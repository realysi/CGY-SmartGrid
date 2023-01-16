from code.read import read_data
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
    data = read_data()

    # Algorithm of choice
    data_handeld = random_algorithm(data.houses, data.batteries) # Returns dictionaries = [copy_houses, copy_batteries]
    output_file(data_handeld.houses, data_handeld.batteries) #creates outputfile which contains data of both dictionaries -> see output.txt



    # calculate paths 

    #plot the grid with all its data:
    plot_grid(data_handeld.houses, data_handeld.batteries)
    

    

