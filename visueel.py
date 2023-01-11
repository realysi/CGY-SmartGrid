import csv
import numpy
from matplotlib import pyplot


"""
Functie om de data van de csv files in te lezen
Toekomstige problemen: Lijnen tekenen (vragen begeleider of matplotlib hier wel ideaal voor is)
Note! Heb veel enters in de code om het zo overzichtelijk mogelijk te houden voor de rest

Wat nog te doen:
- Classes voor huizen, batterijen en verbindingen?
- 
"""

pyplot.xlim(-0.2,51)   #limiet x-as
pyplot.ylim(-0.2,51)   #limiet y-as

pyplot.grid(which='major')  #toont major grid
pyplot.grid(which='minor')  #toont minor grid

#Data van huizen
with open('Huizen&Batterijen/district_1/district-1_houses.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')


    line_count = 0
    for row in csv_reader:
        if line_count != 0: #skip eerste line 
            x = row[0]
            y = row[1]
            pyplot.plot(int(x), int(y), marker="p", color="black")
        line_count += 1

#Data van batterijen
with open('Huizen&Batterijen/district_1/district-1_batteries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count != 0: #skip eerste line 
            x1 = row[0]
            y1 = row[1]
            pyplot.plot(int(x1), int(y1), marker="P", color="red")
        line_count += 1

axes_nummers = []
for i in range(51):
    if i % 5 == 0:
        axes_nummers.append(i)
        
for i in axes_nummers:
    pyplot.axhline(i, linestyle="-", color="black", linewidth=0.5)
    pyplot.axvline(i, linestyle="-", color="black", linewidth=0.5)

pyplot.xticks(ticks=axes_nummers, labels=axes_nummers) 
pyplot.yticks(ticks=axes_nummers, labels=axes_nummers)

#tonen grid 
pyplot.minorticks_on() #toon minor gridlines (kan ticks nog uitschakelen -> zie links)
pyplot.tight_layout()
pyplot.title("Smart Grid")
pyplot.show()




"""
Links:
https://www.tutorialspoint.com/how-can-i-plot-a-single-point-in-matplotlib-python
https://www.pythoncharts.com/matplotlib/customizing-grid-matplotlib/
https://stackoverflow.com/questions/14608483/how-to-add-a-grid-line-at-a-specific-location-in-matplotlib-plot

"""