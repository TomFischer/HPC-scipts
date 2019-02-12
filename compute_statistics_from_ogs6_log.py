#!/bin/python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pylab
import pandas as pd

df = pd.read_csv(sys.argv[1], sep=' ')

time_step_start = 0
time_step_end = 0
current_time_step = 1
i = 0

# print header
ts = 'time_step_number'
asm = 'assembly_time'
asm_min = asm + '_min'
asm_max = asm + '_max'
asm_mean = asm + '_mean'
asm_var = asm + '_var'
asm_all = asm_min + ' ' + asm_max + ' ' + asm_mean + ' ' + asm_var
ls = 'linear_solver'
lst = ls + '_time'
ls_min = lst + '_min'
ls_max = lst + '_max'
ls_mean = lst + '_mean'
ls_var = lst + '_var'
lsn = ls + '_iterations'
ls_all = ls_min + ' ' + ls_max + ' ' + ls_mean + ' ' + ls_var + ' ' + lsn
non_lin_iter = 'nonlinear_iteration_time'
non_lin_iter_min = non_lin_iter + '_min'
non_lin_iter_max = non_lin_iter + '_max'
non_lin_iter_mean = non_lin_iter + '_mean'
non_lin_iter_var = non_lin_iter + '_var'
non_lin_itern = non_lin_iter + '_iterations'
non_lin_iter_all = non_lin_iter_min + ' ' + non_lin_iter_max + ' ' + non_lin_iter_mean + ' ' + non_lin_iter_var + ' ' + non_lin_itern

print(ts + ' ' + asm_all + ' ' + ls_all + ' ' + non_lin_iter_all)

while i < len(df.index):
    if current_time_step != df.iloc[i,0]:
        time_step_start = time_step_end
        time_step_end = i
        act_time_step_frame = df.truncate(before=time_step_start, after=time_step_end-1, axis=0)
        print(str(current_time_step) + ' ' + str(act_time_step_frame['assembly_time'].min()) + ' ' + str(act_time_step_frame['assembly_time'].max()) + ' ' + str(act_time_step_frame['assembly_time'].mean()) + ' ' + str(act_time_step_frame['assembly_time'].var()) + ' ' + str(act_time_step_frame['linear_iterations_time'].min()) + ' ' + str(act_time_step_frame['linear_iterations_time'].max()) + ' ' + str(act_time_step_frame['linear_iterations_time'].mean()) + ' ' + str(act_time_step_frame['linear_iterations_time'].var()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].min()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].max()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].mean()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].var()))
        current_time_step = df.iloc[i,0]
    i = i + 1

time_step_start = time_step_end
time_step_end = i
act_time_step_frame = df.truncate(before=time_step_start, after=time_step_end-1, axis=0)
print(str(current_time_step) + ' ' + str(act_time_step_frame['assembly_time'].min()) + ' ' + str(act_time_step_frame['assembly_time'].max()) + ' ' + str(act_time_step_frame['assembly_time'].mean()) + ' ' + str(act_time_step_frame['assembly_time'].var()) + ' ' + str(act_time_step_frame['linear_iterations_time'].min()) + ' ' + str(act_time_step_frame['linear_iterations_time'].max()) + ' ' + str(act_time_step_frame['linear_iterations_time'].mean()) + ' ' + str(act_time_step_frame['linear_iterations_time'].var()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].min()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].max()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].mean()) + ' ' + str(act_time_step_frame['nonlinear_iteration_time'].var()))

