from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

class Grid:
    """
    Creates a grid with all houses and batteries on the grid. 
    """

    def __init__(self) -> None:
        self.x_limit = 51
        self.y_limit = 51


    def empty_grid(self, ):
        plt.xlim(-0.2,51)   # Limit x-axis
        plt.ylim(-0.2,51)   # Limit y-axis

        plt.grid(which='major')
        plt.grid(which='minor')

    def plot_houses(self, houses):
        for i in houses:
            x = houses[i].x
            y = houses[i].y
            plt.plot(int(x), int(y), marker="p", color="black")
    
    def plot_batteries(self, batteries):
        for i in batteries:
            x = batteries[i].x
            y = batteries[i].y
            plt.plot(int(x), int(y), marker="P", color="red")
        
    def axes_numbers(self):
        axes_numbers = []
        for number in range(51):
            if number % 5 == 0:
                axes_numbers.append(number)

        for number in axes_numbers:
            plt.axhline(number, linestyle="-", color="black", linewidth=0.5)
            plt.axvline(number, linestyle="-", color="black", linewidth=0.5)

        plt.xticks(ticks=axes_numbers, labels=axes_numbers) 
        plt.yticks(ticks=axes_numbers, labels=axes_numbers)