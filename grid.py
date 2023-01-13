import matplotlib.pyplot as plt
from ..read import houses
from ..read import batteries

"""
argparse uitgelegd:
voeg na de gebruikelijke "python3 filename" de vlag --disctrict toe met daarachter 1 2 of 3 om aan te geven
welke dataset van de drie districten je wil verwerken. Met een getal groter dan 3 kom je hier ook door, maar
dan wordt er geen data verwerkt.
"""

plt.xlim(-0.2,51)   #limiet x-as
plt.ylim(-0.2,51)   #limiet y-as

plt.grid(which='major')  #toont major grid
plt.grid(which='minor')  #toont minor grid

#Data of houses
#indexing of dictionary: [0]connection, [1]to_bat, [2]x, [3]y, [4]max_output
for i in houses:
    x = houses[i].x
    y = houses[i].y
    plt.plot(int(x), int(y), marker="p", color="black")

#Data van batterijen
#indexing of dictionary: [0]to_houses, [1]capacity, [2]x, [3]y
for i in batteries:
    x = batteries[i].x
    y = batteries[i].y
    plt.plot(int(x), int(y), marker="P", color="red")

axes_nummers = []
for i in range(51):
    if i % 5 == 0:
        axes_nummers.append(i)

for i in axes_nummers:
    plt.axhline(i, linestyle="-", color="black", linewidth=0.5)
    plt.axvline(i, linestyle="-", color="black", linewidth=0.5)

plt.xticks(ticks=axes_nummers, labels=axes_nummers) 
plt.yticks(ticks=axes_nummers, labels=axes_nummers)

#tonen grid 
plt.minorticks_on() #toon minor gridlines (kan ticks nog uitschakelen -> zie links)
plt.tight_layout()
plt.title("Smart Grid")
plt.show()


"""
Links:
https://www.tutorialspoint.com/how-can-i-plot-a-single-point-in-matplotlib-python
https://www.pythoncharts.com/matplotlib/customizing-grid-matplotlib/
https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot
https://stackoverflow.com/questions/7908636/how-to-add-hovering-annotations-to-a-plot

"""