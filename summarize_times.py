#!/bin/python

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt
import sys
import pylab

assembly_times = []
linear_solver_times = []

for i in np.arange(1, len(sys.argv)):
    data = genfromtxt(sys.argv[i], delimiter=' ')
    assembly_times.append(data[:,2])
    linear_solver_times.append(data[:,4])

for i in np.arange(0, len(assembly_times)):
    print(sys.argv[i+1] + ' ' + str(np.sum(assembly_times[i])) + ' ' + str(np.sum(linear_solver_times[i])))
