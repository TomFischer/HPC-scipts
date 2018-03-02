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
total_assembly_time0 = np.sum(assembly_time0)
number_of_linear_iterations0 = data0[:,3]
linear_solver_time0 = data0[:,4]
total_linear_solver_time0 = np.sum(linear_solver_time0)

data1 = genfromtxt(sys.argv[2], delimiter=' ')
time_steps1 = data1[:,0]
nonlinear_iterations1 = data1[:,1]
assembly_time1 = data1[:,2]
total_assembly_time1 = np.sum(assembly_time1)
number_of_linear_iterations1 = data1[:,3]
linear_solver_time1 = data1[:,4]
total_linear_solver_time1 = np.sum(linear_solver_time1)

data2 = genfromtxt(sys.argv[3], delimiter=' ')
time_steps2 = data2[:,0]
nonlinear_iterations2 = data2[:,1]
assembly_time2 = data2[:,2]
total_assembly_time2 = np.sum(assembly_time2)
number_of_linear_iterations2 = data2[:,3]
linear_solver_time2 = data2[:,4]
total_linear_solver_time2 = np.sum(linear_solver_time2)

data3 = genfromtxt(sys.argv[4], delimiter=' ')
time_steps3 = data3[:,0]
nonlinear_iterations3 = data3[:,1]
assembly_time3 = data3[:,2]
total_assembly_time3 = np.sum(assembly_time3)
number_of_linear_iterations3 = data3[:,3]
linear_solver_time3 = data3[:,4]
total_linear_solver_time3 = np.sum(linear_solver_time3)

print(sys.argv[1] + ' ' + str(total_assembly_time0) + ' ' + str(total_linear_solver_time0))
print(sys.argv[2] + ' ' + str(total_assembly_time1) + ' ' + str(total_linear_solver_time1))
print(sys.argv[3] + ' ' + str(total_assembly_time2) + ' ' + str(total_linear_solver_time2))
print(sys.argv[4] + ' ' + str(total_assembly_time3) + ' ' + str(total_linear_solver_time3))
