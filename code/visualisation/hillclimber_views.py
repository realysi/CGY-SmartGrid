from matplotlib import pyplot as plt
import csv

def read_data(file, swaps, algorithm, base):
    with open(file) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        depth = []
        cost = []
        for row in csv_reader:
            depth.append(int(row[0]))
            cost.append(int(row[1]))

    a = plt.hist(cost)
    plt.xlim(0, 25000)
    plt.xticks(ticks=[0, 5000, 10000, 15000, 20000], labels=axes_numbers) 
    plt.xlabel("Score/Costs")
    plt.ylabel("Appearance")
    plt.title(f"Scores of {algorithm}, swaps = {swaps}, base = {base}")
    plt.savefig("plaatje.png", bbox_inches='tight')

    plt.hist(depth, bins = 50)
    plt.xlabel("Score/Costs")
    plt.ylabel("Appearance")
    plt.title(f"Depth of {algorithm}, swaps = {swaps}, base = {base}")
    plt.savefig("plaatje.png", bbox_inches='tight')


def sketch(results: dict):
    """
    Return dataset of the best score.
    Saves figures that display the data of the restart hill climber algorithm. Shows histogram of score and depth.
    """
    scores = []
    depth = []
    for hillclimber in results:
        scores.append(results[hillclimber].cost)
        depth.append(results[hillclimber].depth)

    best_score = min(scores)

    for i in results:
        if results[i].cost == best_score:
            data_best_score = results[i]

    average_depth = sum(scores) / len(scores)
    
    plt.hist(scores, bins=50)
    plt.xlabel("Score/Costs")
    plt.ylabel("Appearance")
    plt.title("Scores of restart hill climber")
    plt.savefig('Scores/Costs', bbox_inches='tight')
    plt.show()

    plt.hist(depth, bins=50)
    plt.xlabel("Depth of algorithm")
    plt.ylabel("Appearance")
    plt.title("Depths of hill climber runs")
    plt.savefig('Depth', bbox_inches='tight')
    plt.show()