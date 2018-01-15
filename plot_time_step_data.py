#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import pandas as pd
import sys
import pylab
import csv

# reading and parsing functions

#def readData(filename):
#    time_step_number = []
#    iterations = []
#    assembly_time = []
#    solver_time = []
#
#    for line in open(filename):
#        temperature.append(line)

data = genfromtxt(sys.argv[1], delimiter=' ')

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

