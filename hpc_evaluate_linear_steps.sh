#!/usr/bin/env bash

# partition the out.txt file
mkdir part_out_files
for i in `seq 0 $2`;
do
    if [ ! -f part_out_files/$i.txt ];
    then
        grep "\[$i\]" $1 > part_out_files/$i.txt
    fi
done

# process the files in part_out_files folder
mkdir -p processed_data/linearsteps
for i in `seq 0 $2`;
do
    python ~/w/HPC-scripts/process_ht_experiments.py --linearsteps_as_csv part_out_files/$i.txt > processed_data/linearsteps/$i.txt
done


