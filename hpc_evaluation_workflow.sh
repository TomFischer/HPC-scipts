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
mkdir processed_data
for i in `seq 0 $2`;
do
    python ~/w/HPC-scripts/process_ht_experiments.py --output_time part_out_files/$i.txt > processed_data/$i.txt
done

# evaluated the times
for i in `seq 0 $2`;
do
    awk -F ' ' '{sum += $0} END {print sum}' processed_data/$i.txt
    tail -n 1 processed_data/$i.txt
done

