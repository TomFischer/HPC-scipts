#!/bin/bash

bin_path=$PROJECT_ogs6hpc

io_0=`${bin_path}/w/HPC-scripts/evaluate_io_time_ts_0.sh $1`
io_50=`${bin_path}/w/HPC-scripts/evaluate_io_time_ts_50.sh $1`
execution=`${bin_path}/w/HPC-scripts/evaluate_execution_time.sh $1`
echo ${io_0} ${io_50} ${execution}
