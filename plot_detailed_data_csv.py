#!/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd

df = pd.read_csv(sys.argv[1], sep=' ')

#fig, ax = plt.subplots(figsize=(8, 5))

#print(df)

time_step_start = 0
time_step_end = 0
current_time_step = 1
i = 0

while i < len(df.index):
    if current_time_step != df.iloc[i,0]:
        time_step_start = time_step_end
        time_step_end = i
        act_time_step_frame = df.truncate(before=time_step_start, after=time_step_end-1, axis=0)
        #print('time step #' + str(current_time_step) + ': assembly_time: ' + str(act_time_step_frame['assembly_time'].min()) + ', ' + str(act_time_step_frame['assembly_time'].max()) + ', ' + str(act_time_step_frame['assembly_time'].mean()) + ', ' + str(act_time_step_frame['assembly_time'].var()))
        #print('time step #' + str(current_time_step) + ': linear solver time: ' + str(act_time_step_frame['linear_iterations_time'].min()) + ', ' + str(act_time_step_frame['linear_iterations_time'].max()) + ', ' + str(act_time_step_frame['linear_iterations_time'].mean()) + ', ' + str(act_time_step_frame['linear_iterations_time'].var()))
        print('time step #' + str(current_time_step) + ': non-linear iteration time: ' + str(act_time_step_frame['nonlinear_iteration_time'].min()) + ', ' + str(act_time_step_frame['nonlinear_iteration_time'].max()) + ', ' + str(act_time_step_frame['nonlinear_iteration_time'].mean()) + ', ' + str(act_time_step_frame['nonlinear_iteration_time'].var()))
        current_time_step = df.iloc[i,0]
    i = i + 1

time_step_start = time_step_end
time_step_end = i
act_time_step_frame = df.truncate(before=time_step_start, after=time_step_end-1, axis=0)
#print('time step #' + str(current_time_step) + ': assembly_time: ' + str(act_time_step_frame['assembly_time'].min()) + ', ' + str(act_time_step_frame['assembly_time'].max()) + ', ' + str(act_time_step_frame['assembly_time'].mean()) + ', ' + str(act_time_step_frame['assembly_time'].var()))
#print('time step #' + str(current_time_step) + ': linear solver time: ' + str(act_time_step_frame['linear_iterations_time'].min()) + ', ' + str(act_time_step_frame['linear_iterations_time'].max()) + ', ' + str(act_time_step_frame['linear_iterations_time'].mean()) + ', ' + str(act_time_step_frame['linear_iterations_time'].var()))
print('time step #' + str(current_time_step) + ': non-linear iteration time: ' + str(act_time_step_frame['nonlinear_iteration_time'].min()) + ', ' + str(act_time_step_frame['nonlinear_iteration_time'].max()) + ', ' + str(act_time_step_frame['nonlinear_iteration_time'].mean()) + ', ' + str(act_time_step_frame['nonlinear_iteration_time'].var()))
#print('current time step ' + str(current_time_step) + ' [' + str(time_step_start) + ', ' + str(time_step_end) + ')')

#print(df.iloc[lambda x: x.index < 10])
#first_time_step = df.truncate(0, 1535)
#print(first_time_step)

#ax.plot(df.iloc[:,0], np.cumsum(df.iloc[:,9]), marker='o')
#ax.plot(df.iloc[:,0], df.iloc[:,9], marker='o')

#ax.legend()
#ax.set_title('Runtime for Fractured Cube Example (ref2)')
#ax.set_xlabel(df.columns.values[0])
#ax.set_ylabel(df.columns.values[9] + ' in s')
#ax.grid() #True, linestyle='-.')
#ax.set_yscale('log')
#plt.show()

