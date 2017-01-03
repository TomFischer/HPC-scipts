#!/bin/bash

ID=$(echo $1 | cut -d'-' -f 2)
ID=$(echo $ID | cut -d'.' -f 1)

PATH_TO_TOOLS=~/w/statistics/b/
RESULT_BASE_PATH=~/Desktop/ToDo/HPC/
RESULT_PATH=$RESULT_BASE_PATH/$ID

if [ ! -d "$RESULT_PATH" ]; then
    mkdir -p $RESULT_PATH
fi

grep 'reading mesh' $1 | awk '{print $6}' | cut -d':' -f 2 > $RESULT_PATH/reading_mesh.txt
${PATH_TO_TOOLS}/max -i $RESULT_PATH/reading_mesh.txt >> $RESULT_BASE_PATH/reading_mesh.txt

#grep 'Output took' $1 | awk '{print $5}' # | cut -d':' -f 2 > $ID-reading_mesh.txt

grep 'Assembly took' $1 | awk '{print $5}' > $RESULT_PATH/assembly.txt
${PATH_TO_TOOLS}/max -i $RESULT_PATH/assembly.txt >> $RESULT_BASE_PATH/assembly.txt

grep 'Applying Dirichlet BCs took' $1 | awk '{print $7}' > $RESULT_PATH/dirichlet.txt
${PATH_TO_TOOLS}/max -i $RESULT_PATH/dirichlet.txt >> $RESULT_BASE_PATH/dirichlet.txt

grep 'Linear solver took' $1 | awk '{print $6}' > $RESULT_PATH/linear-solver.txt
${PATH_TO_TOOLS}/max -i $RESULT_PATH/linear-solver.txt >> $RESULT_BASE_PATH/linear-solver.txt

grep 'Solving process' $1 | awk '{print $7}' > $RESULT_PATH/process.txt
${PATH_TO_TOOLS}/max -i $RESULT_PATH/process.txt >> $RESULT_BASE_PATH/process.txt

grep 'Execution took' $1 | awk '{print $5}' > $RESULT_PATH/total.txt
${PATH_TO_TOOLS}/max -i $RESULT_PATH/total.txt >> $RESULT_BASE_PATH/total.txt

