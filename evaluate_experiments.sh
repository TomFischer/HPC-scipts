#!/bin/bash

CUBE_EDGE_SIZE=$1
# path to the statistic tools
PATH_TO_TOOLS=$2
# path for the results
RESULT_BASE_PATH=$3

reading_mesh=`${PATH_TO_TOOLS}/average -i $RESULT_BASE_PATH/reading_mesh.txt`
assembly=`${PATH_TO_TOOLS}/average -i $RESULT_BASE_PATH/assembly.txt`
dirichlet=`${PATH_TO_TOOLS}/average -i $RESULT_BASE_PATH/dirichlet.txt`
linear_solver=`${PATH_TO_TOOLS}/average -i $RESULT_BASE_PATH/linear-solver.txt`
process=`${PATH_TO_TOOLS}/average -i $RESULT_BASE_PATH/process.txt`
total=`${PATH_TO_TOOLS}/average -i $RESULT_BASE_PATH/total.txt`
total_size=$((CUBE_EDGE_SIZE*CUBE_EDGE_SIZE*CUBE_EDGE_SIZE))
echo "${total_size} ${reading_mesh} ${assembly} ${dirichlet} ${linear_solver} ${process} ${total}"

