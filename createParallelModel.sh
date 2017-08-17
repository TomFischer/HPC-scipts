#!/bin/sh

mesh_generator=~/w/o/br/bin/generateStructuredMesh
partitioner=~/w/o/br/bin/partmesh

d=$1
np=$2

data_dir=$3
wd=$data_dir/${d}x${d}x${d}

if [ ! -d "$wd" ]; then
    mkdir $wd;
    echo "Create directory $wd ... done";
fi

if [ ! -f "$wd/cube_1x1x1.vtu" ]; then
    ${mesh_generator} -e hex --lx 1 --ly 1 --lz 1 --nx ${d} --ny ${d} --nz ${d} -o $wd/cube_1x1x1.vtu;
    echo "Create mesh cube_1x1x1.vtu in ${wd} ... done";
fi

# preparations for multiple partitions
if [ ! -f "${wd}/cube_1x1x1.mesh" ]; then
    ${partitioner} -i $wd/cube_1x1x1.vtu --ogs2metis
    echo "OGS2Metis ... done";
fi

if [ ! -d "${wd}/${np}" ]; then
    echo "Partition mesh into ${np} partitions";
    mkdir ${wd}/${np};
    ln -s ${wd}/cube_1x1x1.vtu ${wd}/${np}/cube_1x1x1.vtu;
    ln -s ${wd}/cube_1x1x1.mesh ${wd}/${np}/cube_1x1x1.mesh;
    ${partitioner} -m -n ${np} -i ${wd}/${np}/cube_1x1x1
    echo "partmesh -m -np ${np} -i ${wd}/${np}/cube_1x1x1 ... done";
    cp templates/cube_1x1x1.gml ${wd}/${np}/;
    cp templates/ogs6 ${wd}/${np}/ogs6_${np}_${d}x${d}x${d}_benchmark.sh;
    sed -i "s/NNN/${np}/" ${wd}/${np}/ogs6_${np}_${d}x${d}x${d}_benchmark.sh;
    cp templates/cube_1x1x1.prj ${wd}/${np}/;

    mkdir ${wd}/${np}/results
fi
