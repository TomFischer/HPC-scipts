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

idealy = np.arange(1, len(assembly_times[len(assembly_times)-1])+1)
idealx = [x * 24 for x in idealy]
fig, ax = plt.subplots(figsize=(5,3.5))
ax.grid(True, linestyle='-.')

fname='scaling_jureca'
ax.plot(idealx, idealy, 'k--', label='ideal')

sublabels = ['MPI (jureca node)', 'MPI (booster)', 'MPI (booster_opt)']
linestyles = ['-', '-.', ':']

for i in np.arange(0, len(assembly_times)):
    assembly_time = assembly_times[i]
    s = assembly_time[0]
    ax.plot(number_of_cores[i], [s / x for x in assembly_time], label='assembly ('+sublabels[i]+')', linestyle=linestyles[i])

    #linear_solver_time = linear_solver_times[i]
    #s = linear_solver_time[0]
    #ax.plot(number_of_cores[i], [s / x for x in linear_solver_time], label='linear solver ('+sublabels[i]+')', linestyle=linestyles[i])

pylab.legend()
ax.set_xlabel("number of processes")
ax.set_ylabel("scaling $\\frac{t(N)}{t(24)}$")

fig.savefig(fname + '.pdf')

plt.show()

