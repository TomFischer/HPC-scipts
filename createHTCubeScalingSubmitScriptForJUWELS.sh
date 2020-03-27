#!/bin/sh

declare -a compute_nodes=("9" "10" "16" "32" "50" "64" "90" "96" "128" "160" "180" "192" "256")
declare -a PETSc_KSPSolvers=("gmres")
declare -a PETSc_Preconditioners=("jacobi")
declare -a PETSc_Preconditioner_Options=("" " -pc_hypre_type boomeramg" "")

# todo: -ksp_norm_type unpreconditioned

cores_per_node=48
model_revision=rev3
branch_name="ConvergenceImprovements"

runtime=$1
base_data_path=$2
base_output_path=$3
script_home=$2/w/HPC-scripts/

for nodes in "${compute_nodes[@]}"
do
    ntasks=$((${nodes}*${cores_per_node}))
    project_dir=${model_revision}/${ntasks}

    # test if project dir exists
    if [ ! -d "$project_dir" ]; then
        mkdir -p $project_dir
    fi

    for solver in "${PETSc_KSPSolvers[@]}"
    do
        pc_options_idx=0
        for pc in "${PETSc_Preconditioners[@]}"
        do
            project_file=Ra_795_fault_${solver}_${pc}_${branch_name}_scaling_experiment_50_ts.prj
            cp $script_home/templates/FaultedCube_HT_${branch_name}_scaling_experiment_50_ts.prj ${project_dir}/${project_file}
            sed --in-place "s/LINEARSOLVER/${solver}/" ${project_dir}/${project_file}
            sed --in-place "s/PC/${pc}${PETSc_Preconditioner_Options[$pc_options_idx]}/" ${project_dir}/${project_file}

            submit_script=${solver}_${pc}_HT_FracturedCube_Scaling.sh
            cp $script_home/templates/juwels_ht_script ${project_dir}/${submit_script}
            sed --in-place "s/PROJECTFILE/${project_file}/" ${project_dir}/${submit_script}
            sed --in-place "s/NTASKS/${ntasks}/" ${project_dir}/${submit_script}
            sed --in-place "s/NNODES/${nodes}/" ${project_dir}/${submit_script}
            sed --in-place "s/MODELREVISION/${model_revision}/" ${project_dir}/${submit_script}
            sed --in-place "s/RUNTIME/${runtime}/" ${project_dir}/${submit_script}
            sed --in-place "s#BASE_DATA_PATH#${base_data_path}#" ${project_dir}/${submit_script}
            sed --in-place "s#BASE_OUTPUT_PATH#${base_output_path}#" ${project_dir}/${submit_script}
            pc_options_idx+=1
        done
    done
done
