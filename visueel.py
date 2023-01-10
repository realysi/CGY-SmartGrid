import csv
import numpy
from matplotlib import pyplot

"""
Functie om de data van de csv files in te lezen
"""
with open('/Users/yanickidsinga/Documents/GitHub/CGY-SmartGrid/Huizen&Batterijen/district_1/district-1_houses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    pyplot.xlim(0,50)
    pyplot.ylim(0,50)
    gridlines = []
    for i in range(50):
        if i % 1 == 0 and i % 10 != 0:
            gridlines.append(i)
    print(gridlines)
    pyplot.grid(which='major')
    pyplot.grid(which='minor')
    x = []
    y = []
    line_count = 0
    for row in csv_reader:
        if line_count != 0:
            x.append(row[0])
            y.append(row[1])
            pyplot.plot(int(x[-1]), int(y[-1]), marker="p", color="black")
        line_count += 1
    pyplot.minorticks_on()
    for i in gridlines:
        pyplot.axhline(i, linestyle="-", color="black", linewidth=0.5)
        pyplot.axvline(i, linestyle="-", color="black", linewidth=0.5)
    pyplot.show()

"""
Links:
https://www.tutorialspoint.com/how-can-i-plot-a-single-point-in-matplotlib-python
https://www.pythoncharts.com/matplotlib/customizing-grid-matplotlib/
https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot
"""