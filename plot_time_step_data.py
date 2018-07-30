#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab

time_step_number = []
number_of_nonlinear_iterations = []
time_for_nonlinear_iterations = []

for i in np.arange(1, len(sys.argv)):
    data = genfromtxt(sys.argv[i], delimiter=' ')
    time_step_number.append(data[:,0])
    number_of_nonlinear_iterations.append(data[:,1])
    time_for_nonlinear_iterations.append(data[:,4])

sublabels = ['bcgs+jacobi', 'gmres+jacobi', 'bcgs+hypre (boomeramg)', 'gmres+hypre (boomeramg)']
linestyles = ['-', '-.', ':','--']

# number of non-linear iterations
fname='nonlinear_iterations_per_time_step_jureca'

fig, ax = plt.subplots()
ax.grid(True, linestyle='-.')

for i in np.arange(0, len(time_step_number)):
    ax.plot(time_step_number[i], number_of_nonlinear_iterations[i],
    label=sublabels[i], linestyle=linestyles[i])

pylab.legend()
ax.set_xlabel("time step")
ax.set_ylabel("number of non-linear iterations")

fig.savefig(fname + '.pdf')

# time for non-linear iterations
fname1='time_for_nonlinear_iterations_per_time_step_jureca'

fig1, ax1 = plt.subplots()
ax1.grid(True, linestyle='-.')

for i in np.arange(0, len(time_step_number)):
    ax1.plot(time_step_number[i], time_for_nonlinear_iterations[i], label=sublabels[i], linestyle=linestyles[i])

pylab.legend()
ax1.set_xlabel("time step")
ax1.set_ylabel("time for non-linear iterations")

fig1.savefig(fname1 + '.pdf')

# cumulative time for non-linear iterations
fname2='cumulative_time_for_nonlinear_iterations_per_time_step_jureca'

fig2, ax2 = plt.subplots()
ax2.grid(True, linestyle='-.')

for i in np.arange(0, len(time_step_number)):
    ax2.plot(time_step_number[i], np.cumsum(time_for_nonlinear_iterations[i]),
    label=sublabels[i], linestyle=linestyles[i])

pylab.legend()
ax2.set_xlabel("time step")
ax2.set_ylabel("cumulative time for non-linear iterations")

fig2.savefig(fname2 + '.pdf')

###
plt.show()
