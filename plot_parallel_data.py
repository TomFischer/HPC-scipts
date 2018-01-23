#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab

data0 = genfromtxt(sys.argv[1], delimiter=' ')
time_steps0 = data0[:,0]
nonlinear_iterations0 = data0[:,1]
assembly_time0 = data0[:,2]
number_of_linear_iterations0 = data0[:,3]
linear_solver_time0 = data0[:,4]

data1 = genfromtxt(sys.argv[2], delimiter=' ')
time_steps1 = data1[:,0]
nonlinear_iterations1 = data1[:,1]
assembly_time1 = data1[:,2]
number_of_linear_iterations1 = data1[:,3]
linear_solver_time1 = data1[:,4]

data2 = genfromtxt(sys.argv[3], delimiter=' ')
time_steps2 = data2[:,0]
nonlinear_iterations2 = data2[:,1]
assembly_time2 = data2[:,2]
number_of_linear_iterations2 = data2[:,3]
linear_solver_time2 = data2[:,4]

fig, ax = plt.subplots()
ax.grid(True, linestyle='-.')

#pylab.plot(np.cumsum(nonlinear_iterations0), label=sys.argv[1])
#pylab.plot(np.cumsum(nonlinear_iterations1), label=sys.argv[2])
#pylab.plot(np.cumsum(nonlinear_iterations2), label=sys.argv[3])
#pylab.ylabel("cumulative nonlinear steps")
pylab.plot(np.cumsum(assembly_time0 + linear_solver_time0), label=sys.argv[1])
pylab.plot(np.cumsum(assembly_time1 + linear_solver_time1), label=sys.argv[2])
pylab.plot(np.cumsum(assembly_time2 + linear_solver_time2), label=sys.argv[3])
pylab.ylabel("cumulative time assembly + solver")

pylab.legend()
pylab.xlabel("time step number")
plt.show()

