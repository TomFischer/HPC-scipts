#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab



nonlinear_iterations = data[:,1]
assembly_time = data[:,2]
solver_time = data[:,3]

fig, ax = plt.subplots()
ax.grid(True, linestyle='-.')

pylab.plot(nonlinear_iterations, label='number of nonlinear iterations')
#pylab.plot(assembly_time, label='assembly time')
#pylab.plot(solver_time, label='solver time')

pylab.legend()
pylab.xlabel("time step number")
pylab.ylabel("#iterations")
plt.show()

