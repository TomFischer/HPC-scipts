#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab

number_of_cores = []
assembly_times = []
linear_solver_times = []

for i in np.arange(1, len(sys.argv)):
    data = genfromtxt(sys.argv[i], delimiter=' ')
    number_of_cores.append(data[:,1])
    assembly_times.append(data[:,2])
    linear_solver_times.append(data[:,3])

fig, ax = plt.subplots(figsize=(5,3.5))
ax.grid(True, linestyle='-.')

fname='run_times'

sublabels = ['MPI (jureca node)', 'MPI (booster)', 'MPI (booster_opt)']
linestyles = ['-', '-.', ':']

for i in np.arange(0, len(assembly_times)):
    ax.plot(number_of_cores[i], assembly_times[i], label='assembly ('+sublabels[i]+')', linestyle=linestyles[i])
    #ax.plot(number_of_cores[i], linear_solver_times[i], label='linear solver ('+sublabels[i]+')', linestyle=linestyles[i])

pylab.legend()
ax.set_xlabel("number of mpi processes")
ax.set_ylabel("run times in $s$")

fig.savefig(fname + '.pdf')

plt.show()

