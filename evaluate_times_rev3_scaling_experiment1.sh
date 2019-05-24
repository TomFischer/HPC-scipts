#!/bin/bash

io_0=`~/w/HPC-scripts/HPC-scipts/evaluate_io_time_ts_0.sh $1`
io_25=`~/w/HPC-scripts/HPC-scipts/evaluate_io_time_ts_25.sh $1`
execution=`~/w/HPC-scripts/HPC-scipts/evaluate_execution_time.sh $1`
echo ${io_0} ${io_25} ${execution}
