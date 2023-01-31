from matplotlib import pyplot as plt

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
    
    plt.hist(scores, bins=20)
    plt.xlabel("Score/Costs")
    plt.ylabel("Appearance")
    plt.title("Scores of restart hill climber")
    plt.show()

    plt.hist(depth, bins=20)
    plt.xlabel("Depth of algorithm")
    plt.ylabel("Appearance")
    plt.title("Depths of hill climber runs")
    plt.show()