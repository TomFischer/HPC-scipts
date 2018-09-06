#!/bin/sh

declare -a PETSc_KSPSolvers=("bcgs" "gmres" "fgmres" "tfqmr")
declare -a PETSc_Preconditioners=("jacobi" "hypre" "hypre")
declare -a PETSc_Preconditioner_Options=("" " -pc_hypre_type boomeramg" " -pc_hypre_type pilut")
declare -a PETSc_Norm_Options=("default" "preconditioned" "unpreconditioned")

model_revision=$1
tend=$2
ntasks=$3
temp_out_dir=$4
project_dir=$5/${model_revision}/${ntasks}
runtime=$6


for solver in "${PETSc_KSPSolvers[@]}"
do
    pc_options_idx=0
    for pc in "${PETSc_Preconditioners[@]}"
    do
        for norm_type in "${PETSc_Norm_Options[@]}"
        do
            project_file=Ra_795_fault_${solver}_${pc}_norm_type_${norm_type}_rtol_1e-10_atol_1e-10_tend_${tend}.prj
            cp templates/${model_revision}.prj ${project_dir}/${project_file}
            sed --in-place "s/LINEARSOLVER/${solver}/" ${project_dir}/${project_file}
            sed --in-place "s/PC/${pc}${PETSc_Preconditioner_Options[$pc_options_idx]}/" ${project_dir}/${project_file}
            sed --in-place "s/NORM_TYPE/${norm_type}/" ${project_dir}/${project_file}
            submit_script=${solver}_${pc}_${norm_type}.sh
            cp templates/eve_ht_script ${project_dir}/${submit_script}
            sed --in-place "s/PROJECTFILE/${project_file}/" ${project_dir}/${submit_script}
            sed --in-place "s/NTASKS/${ntasks}/" ${project_dir}/${submit_script}
            num_compute_nodes=$(($ntasks / 24))
            sed --in-place "s/NNODES/${num_compute_nodes}/" ${project_dir}/${submit_script}
            sed --in-place "s/MODELREVISION/${model_revision}/" ${project_dir}/${submit_script}
            sed --in-place "s/RUNTIME/${runtime}/" ${project_dir}/${submit_script}
            sed --in-place "s#TEMP_OUTPUT_DIR#${temp_out_dir}#" ${project_dir}/${submit_script}
        done
        pc_options_idx+=1
    done
done
