import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def plot_histogram(scores, average_score):
    num_bins = 10
    # the histogram of the data
    bins = plt.hist(scores, num_bins, facecolor='blue', alpha=0.5)

    # add a 'best fit' line
    plt.xlabel('Costs')
    plt.ylabel('Amount of runs')
    plt.title(r'Histogram of 1000 runs')

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    plt.show()
