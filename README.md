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

Later on in the assignment, cables are allowed to be shared by houses to decrease the amount of cable used.
In practise, a house would now be able to connect to a cable which was already connected to a battery.
Said house would then also be connected to the battery, without having to draw its own cable.

### Costs

A cable segment spans between two adjacent points on the grid. The cost of one segment is 9.
The cost per battery is 5000. Without cables, this would already give each district a minimum cost of 25000.

###### Score

Total cost can be used as a scoring system. If we take into consideration the fact that each district
has a standard cost of 25000 and the remaining cost can only be influenced by drawing cables, we can measure 
our programs performance in cable drawing, by total cost. The better solution will have a score which is 
as close to 25000 as possible.

## Running the program

### Requirements

The requirements to run the software can be found in:

**CGY-Smartgrid/requirements.txt**

## Usage


### Main

Program is started when main.py file is called.
This can be done by calling the following:

```
python3 main.py --district #
```

'#' can be either numbers one, two or three, depending on the district that is to be used.

### Algorithms

### Structure

Program is structured as such:

## Authors

- Christos 
- Gabriel Veder
- Yanick Idsinga
