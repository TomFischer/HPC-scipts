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

data3 = genfromtxt(sys.argv[4], delimiter=' ')
time_steps3 = data3[:,0]
nonlinear_iterations3 = data3[:,1]
assembly_time3 = data3[:,2]
number_of_linear_iterations3 = data3[:,3]
linear_solver_time3 = data3[:,4]

data4 = genfromtxt(sys.argv[5], delimiter=' ')
time_steps4 = data4[:,0]
nonlinear_iterations4 = data4[:,1]
assembly_time4 = data4[:,2]
number_of_linear_iterations4 = data4[:,3]
linear_solver_time4 = data4[:,4]

data5 = genfromtxt(sys.argv[6], delimiter=' ')
time_steps5 = data5[:,0]
nonlinear_iterations5 = data5[:,1]
assembly_time5 = data5[:,2]
number_of_linear_iterations5 = data5[:,3]
linear_solver_time5 = data5[:,4]

data6 = genfromtxt(sys.argv[7], delimiter=' ')
time_steps6 = data6[:,0]
nonlinear_iterations6 = data6[:,1]
assembly_time6 = data6[:,2]
number_of_linear_iterations6 = data6[:,3]
linear_solver_time6 = data6[:,4]

data7 = genfromtxt(sys.argv[8], delimiter=' ')
time_steps7 = data7[:,0]
nonlinear_iterations7 = data7[:,1]
assembly_time7 = data7[:,2]
number_of_linear_iterations7 = data7[:,3]
linear_solver_time7 = data7[:,4]

fig, ax = plt.subplots(figsize=(8,6))
ax.grid(True, linestyle='-.')

fname=''
plot_nonlinear_iterations=True
if plot_nonlinear_iterations:
    pylab.plot(np.cumsum(nonlinear_iterations0), label=sys.argv[1])
    pylab.plot(np.cumsum(nonlinear_iterations1), label=sys.argv[2])
    pylab.plot(np.cumsum(nonlinear_iterations2), label=sys.argv[3])
    pylab.plot(np.cumsum(nonlinear_iterations3), label=sys.argv[4])
    pylab.plot(np.cumsum(nonlinear_iterations4), label=sys.argv[5], linestyle="--")
    pylab.plot(np.cumsum(nonlinear_iterations5), label=sys.argv[6], linestyle="--")
    pylab.plot(np.cumsum(nonlinear_iterations6), label=sys.argv[7], linestyle="--")
    pylab.plot(np.cumsum(nonlinear_iterations7), label=sys.argv[8], linestyle="--")
    pylab.ylabel("cumulative nonlinear steps")
    fname='cumulative_nonlinear_steps'
else:
    plot_assembly_linear_solver=True
    if plot_assembly_linear_solver:
        pylab.plot(np.cumsum(assembly_time0 + linear_solver_time0), label=sys.argv[1])
        pylab.plot(np.cumsum(assembly_time1 + linear_solver_time1), label=sys.argv[2])
        pylab.plot(np.cumsum(assembly_time2 + linear_solver_time2), label=sys.argv[3])
        pylab.plot(np.cumsum(assembly_time3 + linear_solver_time3), label=sys.argv[4])
        pylab.plot(np.cumsum(assembly_time4 + linear_solver_time4), label=sys.argv[5], linestyle="--")
        pylab.plot(np.cumsum(assembly_time5 + linear_solver_time5), label=sys.argv[6], linestyle="--")
        pylab.plot(np.cumsum(assembly_time6 + linear_solver_time6), label=sys.argv[7], linestyle="--")
        pylab.plot(np.cumsum(assembly_time7 + linear_solver_time7), label=sys.argv[8], linestyle="--")
        pylab.ylabel("cumulative time assembly + solver")
        fname='cumulative_time_assembly_solver'
    else:
        plot_assembly=True
        if plot_assembly:
            pylab.plot(np.cumsum(linear_solver_time0), label=sys.argv[1])
            pylab.plot(np.cumsum(linear_solver_time1), label=sys.argv[2])
            pylab.plot(np.cumsum(linear_solver_time2), label=sys.argv[3])
            pylab.plot(np.cumsum(linear_solver_time3), label=sys.argv[4])
            pylab.plot(np.cumsum(linear_solver_time4), label=sys.argv[5], linestyle="--")
            pylab.plot(np.cumsum(linear_solver_time5), label=sys.argv[6], linestyle="--")
            pylab.plot(np.cumsum(linear_solver_time6), label=sys.argv[7], linestyle="--")
            pylab.plot(np.cumsum(linear_solver_time7), label=sys.argv[8], linestyle="--")
            pylab.ylabel("cumulative linear solver time")
            fname='cumulative_linear_solver_time'
        else:
            pylab.plot(np.cumsum(assembly_time0), label=sys.argv[1])
            pylab.plot(np.cumsum(assembly_time1), label=sys.argv[2])
            pylab.plot(np.cumsum(assembly_time2), label=sys.argv[3])
            pylab.plot(np.cumsum(assembly_time3), label=sys.argv[4])
            pylab.plot(np.cumsum(assembly_time4), label=sys.argv[5], linestyle="--")
            pylab.plot(np.cumsum(assembly_time5), label=sys.argv[6], linestyle="--")
            pylab.plot(np.cumsum(assembly_time6), label=sys.argv[7], linestyle="--")
            pylab.plot(np.cumsum(assembly_time7), label=sys.argv[8], linestyle="--")
            pylab.ylabel("cumulative assembly time")
            fname='cumulative_assembly_time'

pylab.legend()
pylab.xlabel("time step number")

fig.savefig(fname + '.pdf')

plt.show()

