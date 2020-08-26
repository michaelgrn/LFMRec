# Creates a plot of some statistics about LFM-1b.
# Author: Markus Schedl

import numpy as np
import matplotlib.pyplot as plt


STATISTICS_OUTPUT_FILE = 'LFM-1b_stats_users.txt'         # output file for statistics (from LFM-1b_stats.py)

# Main program
if __name__ == '__main__':
    # Load figures from file
    data = np.loadtxt(STATISTICS_OUTPUT_FILE)

    handle_tpc, = plt.loglog(range(data[:,0].__len__()), sorted(data[:,0], reverse=True), 'r-')
    handle_uqa, = plt.loglog(range(data[:,1].__len__()), sorted(data[:,1], reverse=True), 'b-')
    plt.legend([handle_tpc, handle_uqa], ['Playcounts', 'Unique artists'])
#    plt.title('Artist-based statistics', fontsize=18)
    plt.xlabel('Users', fontsize=14)
    plt.ylabel('Playcounts / Unique artists', fontsize=14)
    plt.grid(True)
    plt.savefig('LFM-1b_user_plot.eps', format='eps', dpi=1000)
    plt.show()

