#!/usr/bin/env bash

module load GCC CMake ParaStationMPI Python Eigen PETSc Boost

base_working_dir=w

if [ "$#" -eq 1 ]
then
    base_working_dir=$1
fi

# create directory for vtk
vtk_dir=vtk
mkdir -p $base_working_dir/$vtk_dir
cd $base_working_dir/$vtk_dir
git clone https://gitlab.kitware.com/vtk/vtk.git vtk-8
cd vtk-8
git checkout v8.1.2
# the patch is needed
git apply ../../../w/HPC-scripts/JUWELS/fix_vtk_add_override.patch
mkdir build_release
cd build_release

CC=`which gcc` CXX=`which g++` cmake .. -DCMAKE_BUILD_TYPE=Release -DVTK_USE_X=Off -DVTK_Group_Rendering=Off -DVTK_Group_StandAlone=Off -DModule_vtkIOParallelXML=On -DModule_vtkIOMPIParallel=On -DBUILD_TESTING=Off
make -j20
