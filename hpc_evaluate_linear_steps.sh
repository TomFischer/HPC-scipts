#!/usr/bin/env bash

upper=$((${2}-1))

# partition the out.txt file
mkdir part_out_files
for i in `seq 0 $upper`;
do
    if [ ! -f part_out_files/$i.txt ];
    then
        grep "\[$i\]" $1 > part_out_files/$i.txt
    fi
done

# process the files in part_out_files folder
wd=`pwd`
detailed_output_folder=processed_data/linearsteps
script_path=$HOME/w/HPC-scripts/
mkdir -p $detailed_output_folder
for i in `seq 0 $upper`;
do
    python ${script_path}/process_ht_experiments.py --linearsteps_as_csv part_out_files/$i.txt > $detailed_output_folder/$i.txt
done

cd $detailed_output_folder
python ${script_path}/combine_detailed_data.py 0 $upper
cd $wd


