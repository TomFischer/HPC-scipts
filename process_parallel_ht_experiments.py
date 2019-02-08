#!/bin/python

import numpy as np
import pandas as pd
import re # regular expressions
import sys
import logging
import glob
import csv

class TimeStepItem:
    """Class to store information about one linear step"""
    def __init__(self, number_processes):
        self.assembly_time = np.zeros((number_processes))
        self.number_of_linear_iterations = -1
        self.run_time_linear_solver = np.zeros((number_processes))
        self.convergence_history = []

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

def parseTimeStepItem(lines, begin, end, time_step_item):
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
        match = re.search('.* KSP Residual norm (.*)', line)
        if match:
            time_step_item.convergence_history.append(float(match.group(1)))
    if time_step_item.number_of_linear_iterations == -1:
        logging.debug('could not determine the number of linear iterations in time step item in the range [' + str(begin) + ', ' + str(end) + ')')

# returns the first and the last line of the time step item
def parseTimeStepItemRange(lines, time_step_begin, time_step_end, time_step_item_number, number_of_ranks):
    # search strings
    begin_expression = '.* Assembly took *.'
    end_expression = '.* Iteration #*.'

    time_step_item_begin = -1 # line number the time step item begin
    time_step_item_end = -1 # line number the time step item

    # counts the time step begin item occurrences that are already read
    time_step_item_begin_counter = 0
    # counts the time step end item occurrences that are already read
    time_step_item_end_counter = 0

    for i in range(time_step_begin, time_step_end):
        line = lines[i]
        # search for the time step item begin
        match = re.search(begin_expression, line)
        if match:
            time_step_item_begin_counter += 1
            if time_step_item_begin_counter == (time_step_item_number-1) * number_of_ranks + 1:
                time_step_item_begin = i
                continue
        # search for the time step item end
        match = re.search(end_expression, line)
        if match:
            time_step_item_end_counter += 1
            if time_step_item_end_counter == time_step_item_number * number_of_ranks:
                time_step_item_end = i
                return time_step_item_begin, time_step_item_end

    # if the function returns here the time step item is not correctly read
    return time_step_item_begin, time_step_item_end

# returns the first and the last line of the time step
def parseTimeStep(lines, time_step_begins, time_step_ends, time_step_number, number_of_ranks):
    time_step_item_number = 1
    time_step_item_begins = []
    time_step_item_ends = []
    # parse the first time step item
    time_step_item_begin, time_step_item_end = parseTimeStepItemRange(lines, time_step_begins[time_step_number-1], time_step_ends[time_step_number-1], time_step_item_number, number_of_ranks)
    # if the line number of the time step item end marker > -1 all is fine
    if time_step_item_end > -1:
        time_step_item_begins.append(time_step_item_begin)
        time_step_item_ends.append(time_step_item_end)
    else:
        return time_step_item_begins, time_step_item_ends

    time_step_item_number += 1
    while time_step_item_end > -1:
        time_step_item_begin, time_step_item_end = parseTimeStepItemRange(lines, time_step_begins[time_step_number-1], time_step_ends[time_step_number-1], time_step_item_number, number_of_ranks)
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
        match = re.search(begin_expression, lines[i])
        if match and time_step_begin == -1:
            time_step_begin = i
        match = re.search(end_expression, lines[i])
        if match:
            time_step_end_cnt += 1
        if time_step_end_cnt == number_of_ranks:
            time_step_end = i+1
            #logging.debug('time step ' + str(time_step_number) + ' in range [' + str(time_step_begin) + ', ' + str(time_step_end) + ')')
            return time_step_begin, time_step_end
    #logging.debug('time step ' + str(time_step_number) + ' in range [' + str(time_step_begin) + ', ' + str(time_step_end) + ')')
    return time_step_begin, len(lines)


#log_level = getattr(logging, loglevel.upper(), None)
#if not isinstance(log_level, int):
#    raise ValueError('Invalid log level: %s' % loglevel)
#logging.basicConfig(level=log_level)
logging.basicConfig(level=logging.DEBUG)
#logging.basicConfig(level=logging.INFO)

time_steps = []
lines = open(sys.argv[1]).readlines()
number_of_ranks = int(sys.argv[2])
number_of_time_steps = int(sys.argv[3])+1
time_step_begins = []
time_step_ends = []

# determine the range for each time step
line_number_begin = 0
for time_step_number in range(1, number_of_time_steps):
    time_step_begin, time_step_end = getTimeStepRange(lines, line_number_begin, number_of_ranks, time_step_number)
    line_number_begin = time_step_begin
    time_step_begins.append(time_step_begin)
    time_step_ends.append(time_step_end)

# determine the ranges for the nonlinear iterations (time step items)
time_step_items_begins = []
time_step_items_ends = []
for time_step in range(1, number_of_time_steps):
#    logging.debug('*** parsing item of time step ' + str(time_step) + ' ***')
    time_step_item_begins, time_step_item_ends = parseTimeStep(lines, time_step_begins, time_step_ends, time_step, number_of_ranks)
    time_step_items_begins.append(time_step_item_begins)
    time_step_items_ends.append(time_step_item_ends)

print('time_step non-linear_iteration_number assembly_time number_linear_iterations linear_iterations_time')
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
        parseTimeStepItem(lines, begin, end, time_step_item)
        sum_assembly_time_step += time_step_item.assembly_time.mean()
        sum_solver_time_step += time_step_item.run_time_linear_solver.mean()
        sum_linear_iterations_time_step += time_step_item.number_of_linear_iterations
        for i in range(0, len(time_step_item.assembly_time)):
            print(str(time_step_number) + ' ' + str(iteration+1) + ' ' + str(time_step_item.assembly_time[i]) + ' ' + str(time_step_item.number_of_linear_iterations) + ' ' + str(time_step_item.run_time_linear_solver[i]))
        # print(str(time_step_number) + ' ' + str(iteration+1) + ' ' + str(time_step_item.assembly_time.min()) + ' ' + str(time_step_item.assembly_time.max()) + ' ' + str(time_step_item.assembly_time.mean()) + ' ' + str(time_step_item.assembly_time.var()) + ' ' + str(time_step_item.number_of_linear_iterations) + ' ' + str(time_step_item.run_time_linear_solver.min()) + ' ' + str(time_step_item.run_time_linear_solver.max()) + ' ' + str(time_step_item.run_time_linear_solver.mean()) + ' ' + str(time_step_item.run_time_linear_solver.var()))
#        with open(str(time_step_number) + '-' + str(iteration+1) + '.csv', 'w') as output:
#            writer = csv.writer(output, delimiter='\n', lineterminator='\n')
#            writer.writerows([time_step_item.convergence_history])
    #print(str(time_step_number) + ' ' + str(len(time_step_item_begins)) + ' ' + str(sum_assembly_time_step) + ' ' + str(sum_linear_iterations_time_step) + ' ' + str(sum_solver_time_step))
