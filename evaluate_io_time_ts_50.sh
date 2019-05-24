#!/bin/bash

grep 'Output of timestep 50 took' $1 > /tmp/ts_50
awk '{print $8}' /tmp/ts_50 | sort -n > /tmp/ts_50_sorted
t_min=`head -1 /tmp/ts_50_sorted`
t_max=`tail -1 /tmp/ts_50_sorted`
echo ${t_min} ${t_max}
