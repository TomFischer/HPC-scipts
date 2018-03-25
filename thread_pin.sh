#!/usr/bin/env bash

RANK=${OMPI_COMM_WORLD_RANK:=$PMI_RANK}
if [ $(expr $RANK % 2) = 0  ]
then
     #export GOMP_CPU_AFFINITY=0,2,4,6,8,10,12,14,16,18
     numactl -C 0,2,4,6,8,10,12,14,16,18 $@
else
     #export GOMP_CPU_AFFINITY=1,3,5,7,9,11,13,15,17,19
     numactl -C 1,3,5,7,9,11,13,15,17,19 $@
fi
