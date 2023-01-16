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
<<<<<<< Updated upstream
    houses: dict = data[0] #create houses dictionary, which contains data of all the houses
    batteries: dict = data[1] #create batteries dictionary, which contains data of all the houses
    
=======
    houses: dict = data[0] # Create houses dictionary, which contains data of all the houses
    batteries: dict = data[1] # Create batteries dictionary, which contains data of all the houses
    output_file(houses, batteries) # Creates outputfile which contains data of both dictionaries -> see output.txt
>>>>>>> Stashed changes

    # Algorithm of choice
    data_2 = random_algorithm(houses, batteries) # Returns dictionaries = [copy_houses, copy_batteries]
    houses: dict = data_2[0]
    batteries: dict = data_2[1]
    output_file(houses, batteries) #creates outputfile which contains data of both dictionaries -> see output.txt


<<<<<<< Updated upstream
    # calculate paths 

    #plot the grid with all its data:
=======
    # Calculate paths 

    ##plot the grid with all its data:
>>>>>>> Stashed changes
    plot_grid(houses, batteries)
    

    

