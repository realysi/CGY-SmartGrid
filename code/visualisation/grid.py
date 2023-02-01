import matplotlib.pyplot as plt
from ..classes.cable import Cable

def empty_grid():
    plt.xlim(-0.2,51)   # Limit x-axis
    plt.ylim(-0.2,51)   # Limit y-axis

    plt.grid(which='major')
    plt.grid(which='minor')

#Data of houses
#indexing of dictionary: [0]connection, [1]to_bat, [2]x, [3]y, [4]max_output
def plot_houses(houses):
    for house_id in houses:
        x = houses[house_id].x
        y = houses[house_id].y
        color = color_house(houses[house_id])
        plt.plot(int(x), int(y), marker=".", color=color)
        
# Removes labels from axes
def axes_labels():
    plt.xlabel("")
    plt.ylabel("")

# Gives color to houses on the grid
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
    for battery_id in batteries:
        x = batteries[battery_id].x
        y = batteries[battery_id].y
        color = color_battery(batteries[battery_id])
        plt.plot(int(x), int(y), marker="D", color=color, label=f"Battery {batteries[battery_id].id}")

        plt.legend()

#  Gives color to batteries on the grid
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

def draw_cables(cables):
    for cable in cables:
        coordinates = cables[cable].segments
        battery_id = cables[cable].start.to_battery

        x_coordinates = []
        y_coordinates = []

        length = len(coordinates)
        j = 0
        for i in coordinates:
            x_coordinates.append(i[0][0])
            y_coordinates.append(i[0][1])
            x_coordinates.append(i[1][0])
            y_coordinates.append(i[1][1])
        
        color = color_cables(battery_id)

        plt.plot(x_coordinates, y_coordinates, color=color, ls = "-")

def color_cables(battery_id):
        if battery_id == 1:
            return f"black"
        elif battery_id == 2:
            return f"green"
        elif battery_id == 3:
            return f"blue"
        elif battery_id == 4:
            return f"red"
        elif battery_id == 5:
            return f"purple"    

def render_grid():
    plt.minorticks_on() #toon minor gridlines (kan ticks nog uitschakelen -> zie links)
    plt.tight_layout()
    plt.title("Smart Grid")

def plot_grid(houses, batteries, cables):
    plt.clf() #to empyty the plot when wanting to run it more times for the same algorithm
    empty_grid()
    plot_houses(houses)
    plot_batteries(batteries)
    axes_numbers()
    axes_labels()
    draw_cables(cables)
    ax = plt.subplot()
    box = ax.get_position()
    # Schrinks grid so that a legend box can be added.
    ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    render_grid()
    plt.savefig('grid.png', bbox_inches='tight')
    plt.show()

"""
Links:
https://www.tutorialspoint.com/how-can-i-plot-a-single-point-in-matplotlib-python
https://www.pythoncharts.com/matplotlib/customizing-grid-matplotlib/
https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot
https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot

"""