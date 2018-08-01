#!/bin/sh

declare -a PETSc_KSPSolvers=("bcgs" "gmres")
declare -a PETSc_Preconditioners=("jacobi" "boomeramg")

model_revision=$1
tend=$2
ntasks=$3
project_dir=$4
runtime=0:15:00

for solver in "${PETSc_KSPSolvers[@]}"
do
    for pc in "${PETSc_Preconditioners[@]}"
    do
        project_file=Ra_795_fault_${solver}_${pc}_rtol_1e-10_atol_1e-10_tend_${tend}.prj
        cp templates/${model_revision}.prj ${project_dir}/${project_file}
        sed --in-place "s/LINEARSOLVER/${solver}/" ${project_dir}/${project_file}
        sed --in-place "s/PC/${pc}${PETSc_Preconditioner_Options[$pc_options_idx]}/" ${project_dir}/${project_file}
        submit_script=${solver}_${pc}_1e-10_dirichlet.sh
        cp templates/jureca_ht_script ${project_dir}/${submit_script}
        sed --in-place "s/PROJECTFILE/${project_file}/" ${project_dir}/${submit_script}
        sed --in-place "s/NTASKS/${ntasks}/" ${project_dir}/${submit_script}
        num_compute_nodes=$(($ntasks / 24))
        sed --in-place "s/NNODES/${num_compute_nodes}/" ${project_dir}/${submit_script}
        sed --in-place "s/MODELREVISION/${model_revision}/" ${project_dir}/${submit_script}
        sed --in-place "s/RUNTIME/${runtime}/" ${project_dir}/${submit_script}
    done
done
