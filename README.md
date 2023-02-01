# SmartGrid

The future is here already. Homes all across the world are producing energy using the power of solar rays.
Most of this energy can be used within the home, but on very sunny days a surplus will mount.
Batteries will be installed throughout cities to collect this surplus of electrical energy.

In the SmartGrid case it is our job as programmers to find a solution to the problem of connecting the homes and batteries.
Cables will have to be drawn between the homes and the batteries, while using as little cable as possible.
Three cities/districts were made available to study and practise on. All districts contain 150 homes and 5 batteries.
The homes and batteries are situated on a 50 by 50 grid. The distance between two points one the grid
is measured using Manhattan geometry.

### Constraints

The assignments has a few hard-constraints, these are:

- Batteries may not be connected to one another
- One house may only be connected to one battery
- Each house needs a unique cable to be connected to a battery

Later on in the assignment, cables are allowed to be shared by houses to decrease the amount of cables used.
In practise, a house would now be able to connect to a cable which was already connected to a battery.
Said house would then also be connected to the battery, without having to draw its own cable.

### Costs

A cable segment spans between two adjacent points on the grid. The cost of one segment is 9.
The cost per battery is 5000. Without cables, this would already give each district a minimum cost of 25000.

##### Score

Total cost can be used as a scoring system. If we take into consideration the fact that each district
has a standard cost of 25000 and the remaining cost can only be influenced by drawing cables, we can measure 
our programs performance in cable drawing, by total cost. The better solution will have a score which is 
as close to 25000 as possible.

## Algorithms

In this sections all implemented algorithms will be discussed and the steps each algorithm takes will be explained.

#### Random

This algorithm solves this problem by approaching it as a knapsack problem.
In this case there are 5 batteries, which together have to contain 150 houses.
It works as follows:

- Randomly select a battery and fill this battery with random houses untill there is no more capacity.
- Continue to the next battery and repeat the process.
- When the last battery has run out of capacity, a check will be performed to see whether all houses are connected to a battery. 
- In case this is true, the algorithm yields a result. Otherwise the algorithm will restart untill the check is passed.

#### Distance Related

The distance algorithm first calculates the distance to all houses for each battery. All these distances are stored in lists for each battery. The first house in the list of battery one gets added to the battery, the same is done for the second battery and so on. After this proccess has continued for all houses, one house is left without a battery. To connect this remaining house to a battery, the following happens:

- Checks which houses have no battery.
- Finds the batteries from which the algorithm is potentially going to remove a house.
    - The capacity border parameter determines the maxmimum remaining capacity a battery may have, for a house to be removed from it.
- From the potential batteries a random battery is chosen from which a house will be removed.
    - The parameter 'amount of houses to be removed' is given. This parameter will remove the given amount of houses from the battery. A value of 1 or 2 is necessary for the code to work.
- For each selected house, it will be checked whether it fits inside a battery. If it fits, the house is added to the battery. 
    - To prevent a house from not being added to a battery, the list of houses without a battery is randomized after 10 shuffles.
- After fitting all the houses, the algorithm yields a result.

#### Hillclimber

The hill climber algorithm tries to achieve lower costs by continously switching a set amount of houses. It switches the batteries of the given amount of houses with each other. If the capacity of one of the batteries is exceeded, the algorithm starts again. If none of the capacities is exceeded, the scores of the edited data set by the hill climber will be compared to that of the data before the changes of the algorithm. If the cost is lower after the algorithm, this dataset will be returned. Otherwise the algorithm starts again. 

The following arguments/parameters can be given to this algorithm:
- district
- depth (amount of total tries)
- restart or no restart
- if restarts --> amount of restarts
- base algorithm

In this project there are 2 types of hillclimber algorithms:
- hillclimber random (functions):
    uses a random solution as base to imporve the cost.
- restart_hillclimber random (functions): 
    restarts if no improvement can be found within x-tries. Uses a random solution as base.


#### Clustering

The clustering algorithm makes clusters of houses which are relatively close to one another. All houses in a cluster will
be connected to eachother via a 'main' house. It then connects the main house to the closest battery. Houses that are not part of a cluster (because they are too far away) will be connected to batteries at the end. As of now, it does not produce a valid solution since not all houses will be connected in the end. It works as follows:

- Make clusters of houses. Each house can be in only one cluster.
- Draw cables between houses in cluster and main house. Connect houses to nearest battery.
- Draw cables from main house to battery. Connect main house to nearest battery.
- If nearest battery does not have enough capacity, try next battery in the sequence.
- Connect all houses which did not belong to a cluster.

## Usage

### Requirements

All code is written in python 3.8.10. The **CGY-Smartgrid/requirements.txt** file includes all packages which are required to run the code.
This can be installed automatically by running:

```
pip install -r requirements.txt
```

### To run the program

**Instructions on how to run the program with different algorithms will follow:**

The main.py file will have to be called with a number of arguments, depending on the algorithm.

Example:

```
python3 main.py --district 2 random 100
```

This command would run the random algorithm 100 times on district number two.

First, the --district flag followed by either number one, two or three, should be typed 
to choose which district will be used to solve for a solution.

Then, the name of the algorithm has to be entered followed by the number of runs the user
wants to complete. The best score out of this number of runs will be saved.

The different algorithms to be entered are:

- random (followed by number of runs)
- distance (followed by: number of runs | amount of houses deleted per shuffle | capacity border)
- hillclimber (followed by: base algorithm (random/greedy) | amount of houses to switch | depth)
- restart_hillclimber (followed by: base algorithm (random/greedy) | amount of houses to switch | depth | restarts)
- cluster (followed by number of runs)

hillclimber greedy, restart_hillclimber greedy and cluster algorithm will not produce valid outputs.

### Structure

The files are structured as such:

- **/code**: contains all the code written during this project and code that does not belong to other folders
    - **/code/algorithms**: contains the code for the four algorithms
    - **/code/classes**: contains the code for all classes
    - **/code/experiments**: contains the code for the experiments
    - **/code/visualisation**: contains the code for the visualisation
- **/data**: contains the data from the problemset

## Authors

- Christos Anagnostou
- Gabriel Veder
- Yanick Idsinga
