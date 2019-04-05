#!/bin/bash

grep 'Output of timestep 0 took' $1 > /tmp/ts_0
awk '{print $8}' /tmp/ts_0 | sort -n > /tmp/ts_0_sorted
t_min=`head -1 /tmp/ts_0_sorted`
t_max=`tail -1 /tmp/ts_0_sorted`
echo ${t_min} ${t_max}
