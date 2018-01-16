#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab

data0 = genfromtxt(sys.argv[1], delimiter=' ')
data1 = genfromtxt(sys.argv[2], delimiter=' ')
data2 = genfromtxt(sys.argv[3], delimiter=' ')
data3 = genfromtxt(sys.argv[4], delimiter=' ')

nonlinear_iterations0 = data0[:,1]
nonlinear_iterations1 = data1[:,1]
nonlinear_iterations2 = data2[:,1]
nonlinear_iterations3 = data3[:,1]
assembly_time0 = data0[:,2]
assembly_time1 = data1[:,2]
assembly_time2 = data2[:,2]
solver_time0 = data0[:,3]
solver_time1 = data1[:,3]
solver_time2 = data2[:,3]

print('--- summary for ' + sys.argv[1] + ' ---')
print('assembly time: ' + str(assembly_time0.sum()))
print('solver time: ' + str(solver_time0.sum()))
print('nonlinear iterations: ' + str(nonlinear_iterations0.sum()))
print('time per nonlinear iterations: ' + str((assembly_time1.sum() + solver_time1.sum()) / nonlinear_iterations1.sum()))
print('--- summary for ' + sys.argv[2] + ' ---')
print('assembly time: ' + str(assembly_time1.sum()))
print('solver time: ' + str(solver_time1.sum()))
print('nonlinear iterations: ' + str(nonlinear_iterations1.sum()))
print('time per nonlinear iterations: ' + str((assembly_time0.sum() + solver_time0.sum()) / nonlinear_iterations2.sum()))
print('--- summary for ' + sys.argv[3] + ' ---')
print('assembly time: ' + str(assembly_time2.sum()))
print('solver time: ' + str(solver_time2.sum()))
print('nonlinear iterations: ' + str(nonlinear_iterations2.sum()))
print('time per nonlinear iterations: ' + str((assembly_time2.sum() + solver_time2.sum()) / nonlinear_iterations2.sum()))


fig, ax = plt.subplots()
ax.grid(True, linestyle='-.')

pylab.plot(np.cumsum(nonlinear_iterations0), label=sys.argv[1])
pylab.plot(np.cumsum(nonlinear_iterations1), label=sys.argv[2])
pylab.plot(np.cumsum(nonlinear_iterations2), label=sys.argv[3])
#pylab.plot(np.cumsum(nonlinear_iterations3), label=sys.argv[4])
#pylab.plot(assembly_time, label='assembly time')
#pylab.plot(solver_time, label='solver time')
#pylab.plot((assembly_time0 + solver_time0)/nonlinear_iterations0, label=sys.argv[1])
#pylab.plot((assembly_time1 + solver_time1)/nonlinear_iterations1, label=sys.argv[2])
#pylab.plot((assembly_time2 + solver_time2)/nonlinear_iterations2, label=sys.argv[3])

pylab.legend()
pylab.xlabel("time step number")
pylab.ylabel("cumulative nonlinear steps")
plt.show()

