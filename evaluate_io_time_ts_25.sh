#!/bin/bash

grep 'Output of timestep 25 took' $1 > /tmp/ts_25
awk '{print $8}' /tmp/ts_25 | sort -n > /tmp/ts_25_sorted
t_min=`head -1 /tmp/ts_25_sorted`
t_max=`tail -1 /tmp/ts_25_sorted`
echo ${t_min} ${t_max}
