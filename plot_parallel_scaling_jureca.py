#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab

data = genfromtxt(sys.argv[1], delimiter=' ')
number_of_cores = data[:,1]
assembly_time = data[:,2]
linear_solver_time = data[:,3]

idealy = np.arange(1,5)
idealx = [x * 24 for x in idealy]

fig, ax = plt.subplots(figsize=(8,6))
ax.grid(True, linestyle='-.')

fname='scaling_jureca_booster'
ax.plot(idealx, idealy, 'k--', label='ideal')
s = assembly_time[0]
ax.plot(number_of_cores, [s / x for x in assembly_time], label='assembly')
s = linear_solver_time[0]
ax.plot(number_of_cores, [s / x for x in linear_solver_time], label='linear solver')

pylab.legend()
ax.set_xlabel("number of processes")
ax.set_ylabel("scaling $\\frac{t(N)}{t(24)}$")

fig.savefig(fname + '.pdf')

plt.show()

