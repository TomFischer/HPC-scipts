#!/usr/bin/env python

import sys
import pandas as pd

def readCSVs(first_core, last_core):
    df = pd.read_csv(str(first_core) + '.txt')
    df['core'] = first_core

    for core in range(first_core+1, last_core):
        df_t = pd.read_csv(str(core) + '.txt')
        df_t['core'] = core
        df = df.append(df_t)

    return df

def printStatistics(df):
    # print the header
    print('TimeStep,Iteration,AssemblyTimeMin,AssemblyTimeMean,AssemblyTimeMedian,AssemblyTimeMax,AssemblyTimeStd,LinearSolverTimeMin,LinearSolverTimeMean,LinearSolverTimeMedian,LinearSolverTimeMax,LinearSolverTimeStd')
    # calculate and print the statistical data
    for i in range(0, df['TimeStep'].max()+1):
        time_step = df[df['TimeStep'] == i]
        for j in range(1, time_step['Iteration'].max()+1):
            iteration=time_step[time_step['Iteration'] == j]
            print(str(i) + ',' + str(j)
                  + ',' + str(iteration['AssemblyTime'].min())
                  + ',' + str(iteration['AssemblyTime'].mean())
                  + ',' + str(iteration['AssemblyTime'].median())
                  + ',' + str(iteration['AssemblyTime'].max())
                  + ',' + str(iteration['AssemblyTime'].std())
                  + ',' + str(iteration['LinearSolverTime'].min())
                  + ',' + str(iteration['LinearSolverTime'].mean())
                  + ',' + str(iteration['LinearSolverTime'].median())
                  + ',' + str(iteration['LinearSolverTime'].max())
                  + ',' + str(iteration['LinearSolverTime'].std())
            )

def printSums(df, last_core):
    # calculate the sum
    assembly_max = 0
    linear_solver_max = 0
    for i in range(0, df['TimeStep'].max()+1):
        time_step = df[df['TimeStep'] == i]
        for j in range(1, time_step['Iteration'].max()+1):
            iteration=time_step[time_step['Iteration'] == j]
            assembly_max = assembly_max + iteration['AssemblyTime'].max()
            linear_solver_max = linear_solver_max + iteration['LinearSolverTime'].max()
    #print('sum of assembler times (max): ' + str(assembly_max))
    #print('sum of linear solver times (max): ' + str(linear_solver_max))
    print(str(last_core) + ',' + str(assembly_max) + ',' + str(linear_solver_max))


def main():
    first_core=int(sys.argv[1])
    last_core=int(sys.argv[2]) + 1
    df = readCSVs(first_core, last_core)
    #df.to_csv('complete_data.csv', ',')
    #printStatistics(df)
    printSums(df, last_core)

main()
