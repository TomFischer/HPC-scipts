#!/bin/python

import numpy as np
import pandas as pd
import re # regular expressions
import sys
import glob

class TimeStepItem:
    """Class to store information about one linear step"""
    def __init__(self, number_processes):
        self.assembly_time = np.zeros((number_processes))
        self.number_of_linear_iterations = -1
        self.run_time_linear_solver = np.zeros((number_processes))


class TimeStep:
    """Class to store information about a time step"""
    def __init__(self):
        self.time_step_items = []

    def addTimeStepItem(self, item):
        self.time_step_items.append(item)

# reading and parsing functions
def tryMatch(line, regex):
    match = re.search(regex, line)
    if match:
        return float(match.group(1))
    else:
        return -1

def tryMatchInt(line, regex):
    match = re.search(regex, line)
    if match:
        return int(match.group(1))
    else:
        return -1

def tryMatchValue(line, regex):
    match = re.search(regex, line)
    if match:
        return int(match.group(1)), float(match.group(2))
    else:
        return -1, 0.0

def parseTimeStepItem(lines, begin, end, time_step_item, number_processes):
    for i in range(begin, end):
        line = lines[i]
        float_value = 0.0
        pos, float_value = tryMatchValue(line, '\[(.*)\] .*time.* Assembly took (.*) s.')
        if pos != -1:
            time_step_item.assembly_time[pos] = float_value
        number_of_linear_iterations = tryMatchInt(line, '.*converged in (.*) iterations.*')
        if number_of_linear_iterations != -1:
            time_step_item.number_of_linear_iterations = number_of_linear_iterations
        pos, float_value = tryMatchValue(line, '\[(.*)\] .*time.* Linear solver took (.*) s')
        if pos != -1:
            time_step_item.run_time_linear_solver[pos] = float_value

def parseTimeStepItems(iss, time_step, number_processes):
    cnt_time_step_items = 0
    for line in iss:
        match = re.search('.*time.* Time step #.* took .*', line)
        if match:
            cnt_time_step_items += 1
            if cnt_time_step_items == number_processes-1:
                return
            continue
        match = re.search('.*time.* Solver step #.* took .*', line)
        if match:
            cnt_time_step_items += 1
            if cnt_time_step_items == number_processes-1:
                return
            continue
        time_step_item = TimeStepItem(number_processes)
        parseTimeStepItem(iss, time_step_item, number_processes)
        time_step.addTimeStepItem(time_step_item)

# returns the first and the last line of the time step item
def parseTimeStepItemRange(lines, time_step_begin, time_step_end, time_step_item_number, number_of_ranks):
    begin_expression = '.* Assemble .*Process *.'
    end_expression = '.* Iteration #' + str(time_step_item_number) + ' *.'
    time_step_item_begin = -1
    time_step_item_end = -1
    time_step_item_end_cnt = 0
    first_time_step_item_end = -1
    for i in range(time_step_begin, time_step_end):
        line = lines[i]
        match = re.search(begin_expression, line)
        if match and time_step_item_begin == -1:
            time_step_item_begin = i+1
            continue
        match = re.search(end_expression, line)
        if match:
            time_step_item_end_cnt += 1
            if time_step_item_end_cnt == 1:
                first_time_step_item_end = i
        else:
            continue
        if time_step_item_end_cnt == number_of_ranks:
            time_step_item_end = i+1
            return time_step_item_begin, time_step_item_end, first_time_step_item_end
    return time_step_item_begin, time_step_item_end, first_time_step_item_end

# returns the first and the last line of the time step
def parseTimeStep(lines, time_step_begins, time_step_ends, time_step_number, number_of_ranks):
    time_step_item_number = 1
    time_step_item_begins = []
    time_step_item_ends = []
    time_step_item_begin, time_step_item_end, first_time_step_item_end = parseTimeStepItemRange(lines, time_step_begins[time_step_number-1], time_step_ends[time_step_number-1], time_step_item_number, number_of_ranks)
    time_step_item_begins.append(time_step_item_begin)
    time_step_item_ends.append(time_step_item_end)
    time_step_item_number += 1
    while time_step_item_end > -1:
        time_step_item_begin, time_step_item_end, first_time_step_item_end = parseTimeStepItemRange(lines, first_time_step_item_end, time_step_ends[time_step_number-1], time_step_item_number, number_of_ranks)
        if time_step_item_end > -1:
            time_step_item_begins.append(time_step_item_begin)
            time_step_item_ends.append(time_step_item_end)
        time_step_item_number += 1
    return time_step_item_begins, time_step_item_ends

def getTimeStepRange(lines, line_number_begin, number_of_ranks, time_step_number):
    begin_expression = '.* === Time stepping at step #' + str(time_step_number) + ' *.'
    end_expression = '.* \[time\] Time step #' + str(time_step_number) + ' *.'
    time_step_begin = -1
    time_step_end = -1
    time_step_end_cnt = 0
    for i in range(line_number_begin, len(lines)):
        line = lines[i]
        match = re.search(begin_expression, line)
        if match and time_step_begin == -1:
            time_step_begin = i+1
        match = re.search(end_expression, line)
        if match:
            time_step_end_cnt += 1
        if time_step_end_cnt == number_of_ranks:
            time_step_end = i+1
            return time_step_begin, time_step_end



time_steps = []
lines = open(sys.argv[1]).readlines()
number_of_ranks = int(sys.argv[2])
number_of_time_steps = int(sys.argv[3])+1
time_step_begins = []
time_step_ends = []

# determine the range for each time step
line_number_begin = 1
for time_step_number in range(1, number_of_time_steps):
    time_step_begin, time_step_end = getTimeStepRange(lines, line_number_begin, number_of_ranks, time_step_number)
    line_number_begin = time_step_begin
    time_step_begins.append(time_step_begin)
    time_step_ends.append(time_step_end)

# determine the ranges for the nonlinear iterations (time step items)
time_step_items_begins = []
time_step_items_ends = []
for time_step in range(1, number_of_time_steps):
    time_step_item_begins, time_step_item_ends = parseTimeStep(lines, time_step_begins, time_step_ends, time_step, number_of_ranks)
    time_step_items_begins.append(time_step_item_begins)
    time_step_items_ends.append(time_step_item_ends)

for time_step_number in range(1, number_of_time_steps):
    time_step_item_begins = time_step_items_begins[time_step_number-1]
    time_step_item_ends = time_step_items_ends[time_step_number-1]
    sum_assembly_time_step = 0
    sum_solver_time_step = 0
    sum_linear_iterations_time_step = 0
    for iteration in range(0, len(time_step_item_begins)):
        time_step_item = TimeStepItem(number_of_ranks)
        begin = time_step_item_begins[iteration]
        end = time_step_item_ends[iteration]
        parseTimeStepItem(lines, begin, end, time_step_item, number_of_ranks)
        sum_assembly_time_step += time_step_item.assembly_time.mean()
        sum_solver_time_step += time_step_item.run_time_linear_solver.mean()
        sum_linear_iterations_time_step += time_step_item.number_of_linear_iterations
        #print(str(time_step_number) + ' ' + str(iteration+1) + ' ' + str(time_step_item.assembly_time.mean()) + ' ' + str(time_step_item.number_of_linear_iterations) + ' ' + str(time_step_item.run_time_linear_solver.mean()))
    print(str(time_step_number) + ' ' + str(len(time_step_item_begins)) + ' ' + str(sum_assembly_time_step) + ' ' + str(sum_linear_iterations_time_step) + ' ' + str(sum_solver_time_step))
