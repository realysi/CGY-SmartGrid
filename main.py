from read import read_data
from sys import argv

"""

Main file which is used to call all other functions in other files.

"""
   

if __name__ == "__main__":    
    # call functions
    data = read_data()
    houses = data[0]
    print(houses)
    batteries = data[1]
    print(batteries)