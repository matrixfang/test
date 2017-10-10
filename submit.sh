#!/bin/bash
rootDir="/usr3/graduate/wyfang"
workDir="/GitHub/test"
logDir="/GitHub/test/log/"
qsub<<EOF
#$ -N "sr"
#$ -o ${rootDir}${logDir}sr.log
#$ -j y
#$ -V
#$ -P "roughsur"
#$ -l h_rt=36:00:00
#$ -M wyfang@bu.edu
#$ -m ae
cd ${rootDir}${workDir}
module load python/2.7.12
python test.py
EOF
