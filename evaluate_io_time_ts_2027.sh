#!/bin/bash

grep 'Output of timestep 2027 took' $1 > /tmp/ts_2027
awk '{print $8}' /tmp/ts_2027 | sort -n > /tmp/ts_2027_sorted
t_min=`head -1 /tmp/ts_2027_sorted`
t_max=`tail -1 /tmp/ts_2027_sorted`
echo ${t_min} ${t_max}
