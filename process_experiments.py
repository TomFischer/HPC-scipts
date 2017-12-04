#!/bin/python

import numpy as np
import pandas as pd
import re # regular expressions
import sys
import glob
import pylab

# reading and parsing functions

def tryMatch(line, regex, array):
    match = re.search(regex, line)
    if match:
        array.append(float(match.group(1)))

def readSingleFile(filename):
    mesh = []
    assembly = []
    output0 = []
    output1 = []
    dirichlet = []
    linear_solver = []
    iteration1 = []
    solving_timestep1 = []
    timestep1 = []
    execution = []

    for line in open(filename):
        tryMatch(line, '.*time.*Reading the mesh took (.*) s', mesh)
        tryMatch(line, '.*time.*Assembly took (.*) s', assembly)
        tryMatch(line, '.*time.*Output of timestep 0 took (.*) s', output0)
        tryMatch(line, '.*time.*Applying Dirichlet BCs took (.*) s', dirichlet)
        tryMatch(line, '.*time.*Linear solver took (.*) s', linear_solver)
        tryMatch(line, '.*time.*Iteration #1 took (.*) s', iteration1)
        tryMatch(line, '.*time.*Solving process #0 took (.*) s in time step #1', solving_timestep1)
        tryMatch(line, '.*time.*Time step #1 took (.*) s', timestep1)
        tryMatch(line, '.*time.*Output of timestep 1 took (.*) s', output1)
        #tryMatch(line, '.Output of timestep 1 took (.*) s', output1)
        tryMatch(line, '.*time.*Execution took (.*) s', execution)

    print('filename: ' + filename)
    # print('length of array mesh: ' + str(len(mesh)))
    # print('length of array assembly: ' + str(len(assembly)))
    # print('length of array output0: ' + str(len(output0)))
    # print('length of array dirichlet: ' + str(len(dirichlet)))
    # print('length of array linear_solver: ' + str(len(linear_solver)))
    # print('length of array iteration1: ' + str(len(iteration1)))
    # print('length of array solving_timestep1: ' + str(len(solving_timestep1)))
    # print('length of array timestep1: ' + str(len(timestep1)))
    # print('length of array output1: ' + str(len(output1)))
    # print('length of array execution: ' + str(len(execution)))

    print('output time step 1 : ', output1)

    df = pd.DataFrame(data={
            'mesh' : mesh,
            'assembly' : assembly,
            'output0' : output0,
            'dirichlet' : dirichlet,
            'linear_solver' : linear_solver,
            'iteration1' : iteration1,
            'solving_timestep1' : solving_timestep1,
            'timestep1' : timestep1,
            'output1' : output1,
            'execution' : execution
        })
    df.columns = pd.MultiIndex.from_product([['times'],df.columns.get_values()])
    return df

def readFilesForExperiment(file_list):
    frames = []
    for i, f in enumerate(file_list):
        #print(f)
        frames.append(readSingleFile(f))
        frames[-1]['run'] = i
        # JURECA
        #match = re.search('.*x([0-9]+)/([0-9]+)/results/.*out', f)
        # TAURUS
        match = re.search('.*x([0-9]+)/([0-9]+)/.*out', f)

        # Number of cells in a cube with so many divisions along each side
        frames[-1]['cells'] = int(match.group(1))**3

        # Number of partitions of the simulation
        frames[-1]['partitions'] = int(match.group(2))
    return frames

# functions for evaluation

def computeStatisticsForExperiment(frames, column):
    mins = []
    maxs = []
    means = []
    std_deviations = []

    # read describe
    for frame in frames:
        mins.append(frame.times[column].min())
        maxs.append(frame.times[column].max())
        means.append(frame.times[column].mean())
        std_deviations.append(frame.times[column].std())

    statistics_frame = pd.DataFrame(data={
        'minima' : mins,
        'maxima' : maxs,
        'means' : means,
        'standard_deviations' : std_deviations
    })

    return statistics_frame


def evaluateExperimentsForFixedNumberOfProcesses(number, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions):
    glob_name = sys.argv[1]
    glob_name += '/'
    glob_name += str(number)
    # juelich
    #glob_name += '/results/*.out'
    # taurus
    glob_name += '/*.out'
    print (glob_name)
    file_list = glob.glob(glob_name)
    print (file_list)
    raw_data_frames = readFilesForExperiment(file_list)

    cells.append(raw_data_frames[0].cells[0])
    partitions.append(raw_data_frames[0].partitions[0])

    statistics = computeStatisticsForExperiment(raw_data_frames, 'mesh')
    mesh.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'output0')
    output0.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'assembly')
    assembly.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'dirichlet')
    dirichlet.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'linear_solver')
    linear_solver.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'iteration1')
    iteration1.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'solving_timestep1')
    solving_timestep1.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'timestep1')
    timestep1.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'output1')
    output1.append(float(statistics.minima.mean()))
    statistics = computeStatisticsForExperiment(raw_data_frames, 'execution')
    execution.append(float(statistics.minima.mean()))

cells = []
partitions = []
mesh = []
assembly = []
output0 = []
output1 = []
dirichlet = []
linear_solver = []
iteration1 = []
solving_timestep1 = []
timestep1 = []
execution = []

# JURECA and TAURUS
#evaluateExperimentsForFixedNumberOfProcesses(24, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
#evaluateExperimentsForFixedNumberOfProcesses(48, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
#evaluateExperimentsForFixedNumberOfProcesses(72, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
#evaluateExperimentsForFixedNumberOfProcesses(96, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
#evaluateExperimentsForFixedNumberOfProcesses(120, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)

# mistral
evaluateExperimentsForFixedNumberOfProcesses(36, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
evaluateExperimentsForFixedNumberOfProcesses(72, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
evaluateExperimentsForFixedNumberOfProcesses(108, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)
evaluateExperimentsForFixedNumberOfProcesses(144, mesh, output0, assembly, dirichlet, linear_solver, iteration1, solving_timestep1, timestep1, output1, execution, cells, partitions)

s = assembly[0]
pylab.plot(partitions, [s / x for x in assembly], label='assembly')

s = mesh[0]
pylab.plot(partitions, [s / x for x in mesh], label='reading mesh')

s = linear_solver[0]
pylab.plot(partitions, [s / x for x in linear_solver], label='linear solver')

s = output0[0]
pylab.plot(partitions, [s / x for x in output0], label='output0')

s = output1[0]
pylab.plot(partitions, [s / x for x in output1], label='output1')

s = execution[0]
pylab.plot(partitions, [s / x for x in execution], label='execution')

# JURECA
#idealy = np.arange(1,6)
#idealx = [x * 24 for x in idealy]
#pylab.plot(idealx, idealy, label='ideal')

# mistral
idealy = np.arange(1,5)
idealx = [x * 36 for x in idealy]
pylab.plot(idealx, idealy, label='ideal')

pylab.legend()
pylab.xlabel("number of processes")
# JURECA
# pylab.ylabel("scaling $\\frac{t(N)}{t(24)}$")
# mistral
pylab.ylabel("scaling $\\frac{t(N)}{t(36)}$")
pylab.show()

