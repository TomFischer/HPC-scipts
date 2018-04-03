#!/bin/python

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from numpy import genfromtxt
import sys
import pylab

dfs = []
number_of_mpi = []
number_of_openmp = []
assembly_times = []
linear_solver_times = []

for i in np.arange(1, len(sys.argv)):
    dfs.append(pd.read_csv(sys.argv[i], delimiter=' '))
    data = genfromtxt(sys.argv[i], delimiter=' ')
    number_of_mpi.append(data[:,1])
    number_of_openmp.append(data[:,2])
    assembly_times.append(data[:,3])
    linear_solver_times.append(data[:,4])

fig, ax = plt.subplots(figsize=(8,6))
ax.grid(True, linestyle='-.')

fname='run_times'

sublabels = ['MPI/OpenMP']
linestyles = ['-', '-.', ':']

for i in np.arange(0, len(assembly_times)):
    ax.plot(number_of_mpi[i], assembly_times[i], '*', label='assembly ('+sublabels[i]+')') #linestyle=linestyles[i])
    #ax.plot(number_of_mpi[i], linear_solver_times[i], label='linear solver ('+sublabels[i]+')', linestyle=linestyles[i])

pylab.legend()
ax.set_xlabel("number of MPI processes")
second_y_axis = ax.twiny()
ax.set_ylabel("run times in $s$")
second_y_axis.set_xlabel("number of OpenMP threads")
second_axis_ticks = number_of_openmp
print(second_axis_ticks)
second_y_axis.xaxis.set_major_locator(ticker.FixedLocator([12,8,6,4,3,1]))
#second_y_axis.xaxis.set_ticklabels([i[0] for i in second_axis_ticks])

fig.savefig(fname + '.pdf')

plt.show()

