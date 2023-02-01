import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv
import numpy as np



def plot_histogram():

    scores_1 = []
    with open("results/distance/distance_district_1.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            scores_1.append(float(row[1]))
    scores_1 = sorted(scores_1)
    num_bins = 15
    # the histogram of the data
    plt.hist(scores_1, num_bins, facecolor='blue', alpha=0.85, label="Distance")

    scores_2 = []
    with open("results/random/random_district_1.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            scores_2.append(float(row[1]))
    scores_2 = sorted(scores_2)
    num_bins = 15
    # the histogram of the data
    plt.hist(scores_2, num_bins, facecolor='green', alpha=0.85, label="Random")


    # add a 'best fit' line
    plt.xlabel('Scores/Costs')
    plt.ylabel('Appearances')
    plt.title('500 runs')
    plt.xticks(np.arange(5000, 20000, 1000))
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc="upper right")

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.savefig('histogram.png', bbox_inches='tight')
    plt.show()
