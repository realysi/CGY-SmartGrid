from read import read_data
from output import output_file
from grid import plot_grid
from sys import argv
from algo import algo

"""

Main file which is used to call all other functions in other files.

"""
   

if __name__ == "__main__":    
    # call functions
    data = read_data()
    houses: dict = data[0]
    batteries: dict = data[1]
    output_file(houses, batteries)

    plot_grid(houses, batteries)
    algo(houses, batteries)

