import matplotlib.pyplot as plt

def empty_grid():
    plt.xlim(-0.2,51)   # Limit x-axis
    plt.ylim(-0.2,51)   # Limit y-axis

    plt.grid(which='major')
    plt.grid(which='minor')

#Data of houses
#indexing of dictionary: [0]connection, [1]to_bat, [2]x, [3]y, [4]max_output
def plot_houses(houses):
    for i in houses:
        x = houses[i].x
        y = houses[i].y
        color = color_house(houses[i])
        plt.plot(int(x), int(y), marker=".", color=color, label="house")

# Gives color to the house on the grid
def color_house(house):
    if house.to_battery == 1:
        return f"black"
    elif house.to_battery == 2:
        return f"green"
    elif house.to_battery == 3:
        return f"blue"
    elif house.to_battery == 4:
        return f"red"
    elif house.to_battery == 5:
        return f"purple"

#Data of batteries
#indexing of dictionary: [0]to_houses, [1]capacity, [2]x, [3]y
def plot_batteries(batteries):
    for i in batteries:
        x = batteries[i].x
        y = batteries[i].y
        color = color_battery(batteries[i])
        plt.plot(int(x), int(y), marker="D", color=color, label="battery")
    

#  Gives color to the battery on the grid
def color_battery(battery):
    if battery.id == 1:
        return f"black"
    elif battery.id == 2:
        return f"green"
    elif battery.id == 3:
        return f"blue"
    elif battery.id == 4:
        return f"red"
    elif battery.id == 5:
        return f"purple"

def axes_numbers():
    axes_numbers = []
    for number in range(51):
        if number % 5 == 0:
            axes_numbers.append(number)

    for number in axes_numbers:
        plt.axhline(number, linestyle="-", color="black", linewidth=0.5)
        plt.axvline(number, linestyle="-", color="black", linewidth=0.5)

    plt.xticks(ticks=axes_numbers, labels=axes_numbers) 
    plt.yticks(ticks=axes_numbers, labels=axes_numbers)

#Show grid
def render_grid():
    plt.minorticks_on() #toon minor gridlines (kan ticks nog uitschakelen -> zie links)
    plt.tight_layout()
    plt.title("Smart Grid")
    plt.show()


def plot_grid(houses, batteries):
    empty_grid()
    plot_houses(houses)
    plot_batteries(batteries)
    axes_numbers()
    render_grid()


"""
Links:
https://www.tutorialspoint.com/how-can-i-plot-a-single-point-in-matplotlib-python
https://www.pythoncharts.com/matplotlib/customizing-grid-matplotlib/
https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot
https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot

"""