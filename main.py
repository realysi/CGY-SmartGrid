from read import *
from sys import argv

"""

Main file which is used to call all other functions in other files.

"""

if __name__ == "__main__":

    if argv[1] != "--district":
        print("Usage: --district (filenumber)")
        quit()
    else:
        file_number = int(argv[2])
        if file_number > 4:
            quit()
    
    # call functions