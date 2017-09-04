#!/bin/bash

#SBATCH --job-name partition_mesh
#SBATCH --ntasks=1
#SBATCH --nodes=1

#SBATCH --output=%j_out.txt
#SBATCH --error=%j_err.txt
#SBATCH --mail-type=begin,end,fail
#SBATCH --mail-user=thomas.fischer3@mailbox.tu-dresden.de
#SBATCH --mem=25000M
#SBATCH --time=00:15:00
#SBATCH --partition=haswell,sandy,west
#SBATCH -A p_scads

module load gcc/7.1.0

input=/scratch/p_scads/thfische/gwf/292x292x292/96/cube_1x1x1
srun ~thfische/w/o/br/bin/partmesh -m -n 96 -i $input
