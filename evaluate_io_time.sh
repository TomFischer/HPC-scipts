#!/bin/bash
set -x

args=${BASH_ARGV[*]}
echo "args are: $@"
filename=("$@")[1]
echo "filename: $filename"

echo "timestep: $@[2]"
ts=${args[2]}

echo $ts
pattern="Output of timestep ${ts} took"

grep "$pattern" $1 > /tmp/ts_${ts}
awk '{print $8}' /tmp/ts_${ts} | sort -n > /tmp/ts_${ts}_sorted
t_min=`head -1 /tmp/ts_${ts}_sorted`
t_max=`tail -1 /tmp/ts_${ts}_sorted`
echo ${t_min} ${t_max}
