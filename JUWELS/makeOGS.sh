#!/usr/bin/env bash

module load GCC CMake ParaStationMPI Python Eigen PETSc Boost

base_working_dir=w

if [ "$#" -eq 1 ]
then
    base_working_dir=$1
fi

# create directory for OGS
ogs_dir=o
mkdir -p $base_working_dir/$ogs_dir
cd $base_working_dir/$ogs_dir

git lfs clone git@github.com:ufz/ogs.git s
cd s
git remote add ogs-bgr git@gitlab.opengeosys.org:ufz-bgr/ogs.git

# install git large filesystem
git lfs install
git lfs fetch
cd ..

# make partmesh
mkdir br
cd br

PROJECT=$PROJECT_ogs6hpc2

cmake ../s/ -DCMAKE_BUILD_TYPE=Release -DOGS_EIGEN_DYNAMIC_SHAPE_MATRICES=Off -DOGS_USE_PCH=Off -DVTK_DIR=$PROJECT/$base_working_dir/vtk/vtk-8/build_release/ -DEIGEN3_INCLUDE_DIR=/gpfs/software/juwels/stages/2019a/software/Eigen/3.3.7-GCCcore-8.3.0/include -DOGS_BUILD_METIS=On -DOGS_BUILD_UTILS=On -DOGS_USE_CONAN=OFF

make -j20 partmesh

# make ogs parallel version
cd ..
mkdir br_petsc
cd br_petsc
CC=`which mpicc` CXX=`which mpic++` cmake ../s/ -DCMAKE_BUILD_TYPE=Release -DOGS_EIGEN_DYNAMIC_SHAPE_MATRICES=Off -DOGS_USE_PCH=Off -DVTK_DIR=$PROJECT/$base_working_dir/vtk/vtk-8/build_release/ -DEIGEN3_INCLUDE_DIR=/gpfs/software/juwels/stages/2019a/software/Eigen/3.3.7-GCCcore-8.3.0/include -DOGS_USE_PETSC=On -DOGS_USE_MPI=On -DOGS_USE_CONAN=OFF
make -j20 ogs
