#!/bin/sh

base_path=~/w/o

test_path=${base_path}/s/Tests/Data/Parabolic/HT/ConstViscosity
mesh_generator=${base_path}/build_serial/bin/generateStructuredMesh
property_generator=${base_path}/build_serial/bin/createProperty
partitioner=${base_path}/build_serial/bin/partmesh

d=$1
np=$2

data_dir=$3
wd=$data_dir/${d}x${d}

if [ ! -d "$wd" ]; then
    mkdir $wd;
    echo "Create directory $wd ... done";
fi

if [ ! -f "$wd/square_5500x5500.vtu" ]; then
    ${mesh_generator} -e quad --lx 5500 --ly 5500 --nx ${d} --ny ${d} -o $wd/square_5500x5500.vtu;
    echo "Create mesh square_5500x5500.vtu in ${wd} ... done";
    ${property_generator} -i $wd/square_5500x5500.vtu -o $wd/square_5500x5500.vtu;
    echo "Create initial condition for the mesh square_5500x5500.vtu in ${wd} ... done";

fi

# preparations for multiple partitions
if [ ! -f "${wd}/square_5500x5500.mesh" ]; then
    ${partitioner} -i $wd/square_5500x5500.vtu --ogs2metis
    echo "OGS2Metis ... done";
fi

if [ ! -d "${wd}/${np}" ]; then
    echo "Partition mesh into ${np} partitions";
    mkdir ${wd}/${np};
    ln -s ${wd}/square_5500x5500.vtu ${wd}/${np}/square_5500x5500.vtu;
    ln -s ${wd}/square_5500x5500.mesh ${wd}/${np}/square_5500x5500.mesh;
    ${partitioner} -m -n ${np} -i ${wd}/${np}/square_5500x5500
    echo "partmesh -m -np ${np} -i ${wd}/${np}/square_5500x5500 ... done";
    cp ${test_path}/square_5500x5500.gml ${wd}/${np}/;
    cp templates/ogs6 ${wd}/${np}/ogs6_${np}_${d}x${d}_benchmark.sh;
    cp ${test_path}/square_5500x5500.prj ${wd}/${np}/;

    mkdir ${wd}/${np}/results
fi
