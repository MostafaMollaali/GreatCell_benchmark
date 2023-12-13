#!/bin/bash
#SBATCH --job-name=qTaskG
#SBATCH --chdir=/home/wwang/data_D/project/DECOVALEX2023/TaskG/GreatCellBenchmark/input/3D_HM
#SBATCH --output=/home/wwang/data_D/project/DECOVALEX2023/TaskG/GreatCellBenchmark/output/3D_HM/TaylorHood/log_%x_%j.txt
#SBATCH --error=/home/wwang/data_D/project/DECOVALEX2023/TaskG/GreatCellBenchmark/output/3D_HM/TaylorHood/err_%x_%j.txt
#SBATCH --time=0-96:00:00
#SBATCH -c 32
#SBATCH --mem-per-cpu=20G

#SBATCH --mail-user=wenqing.wang@ufz.de
#SBATCH --mail-type=BEGIN,END

###source /etc/profile.d/000-modules.sh
export MODULEPATH="/software/easybuild-broadwell/modules/all/Core:/software/modulefiles"
export MODULEPATH="/global/apps/modulefiles:$MODULEPATH:/home/wwang/Modulues"
#module use /software/easybuild-E5-2690v4/modules/all/Core/
module load foss/2022b
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/wwang/data_D/tools/intel/oneapi/compiler/2023.2.0/linux/compiler/lib/intel64_lin:/home/wwang/data_D/tools/intel/oneapi/mkl/2023.2.0/lib
source /home/wwang/data_D/tools/intel/oneapi/setvars.sh

#
# cd into the directory of your mpi bin and start a mpirun
#
APP="/data/envinf/wwang/build/ogs6_mkl/bin/ogs"
/bin/echo In directory: `pwd`
/bin/echo Number of CPUs: $SLURM_CPUS_PER_TASK
/bin/echo File name: $1

##ldd $APP
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-1}
export OGS_ASM_THREADS=${SLURM_CPUS_PER_TASK:-1}

echo ${SLURM_CPUS_PER_TASK:-1}

$APP /home/wwang/data_D/project/DECOVALEX2023/TaskG/GreatCellBenchmark/input/3D_HM/great_cell_HM_test2_quadratic_mesh.prj  -m /home/wwang/data_D/project/DECOVALEX2023/TaskG/GreatCellBenchmark/input/3D_HM/mesh  -o /home/wwang/data_D/project/DECOVALEX2023/TaskG/GreatCellBenchmark/output/3D_HM/TaylorHood

