from read import read_data
from output import output_file
from grid import plot_grid
from sys import argv
from random_algorithm import random_algorithm

"""

Main file which is used to call all other functions in other files.

"""
   

if __name__ == "__main__":    
    # read in the data
    data = read_data()
    houses: dict = data[0] #create houses dictionary, which contains data of all the houses
    batteries: dict = data[1] #create batteries dictionary, which contains data of all the houses
    output_file(houses, batteries) #creates outputfile which contains data of both dictionaries -> see output.txt

    # algorithm of choice
    data_2 = random_algorithm(houses, batteries) # returns dictionaries = [copy_houses, copy_batteries]
    houses: dict = data_2[0]
    batteries: dict = data_2[1]

    print(houses)
    print(batteries)
    # calculate paths 

    ##plot the grid with all its data:
    #plot_grid(houses, batteries)
    

    

