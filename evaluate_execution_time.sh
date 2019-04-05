#!/bin/bash

grep Execution $1 > /tmp/execution
awk '{print $5}' /tmp/execution | sort -n > /tmp/execution_sorted
t_min=`head -1 /tmp/execution_sorted`
t_max=`tail -1 /tmp/execution_sorted`
echo ${t_min} ${t_max}
