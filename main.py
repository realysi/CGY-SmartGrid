from read import read_data
from sys import argv

"""

Main file which is used to call all other functions in other files.

"""
def main():
    data = read_data()[0]
    print(data)

if __name__ == "__main__":    
    # call functions
    print(main())