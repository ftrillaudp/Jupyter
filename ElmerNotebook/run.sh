#!/bin/bash

if [ "$#" == "0" ]
then
	echo "Run name not set for logging purposes. You can give it with: ./run.sh run_name"
	logname=""
else
	echo "Run name set to $1."
	logname="$1-"
fi

#rm ./Log/* | tee -a $LOGFILE
DATE=$(date +%s)
LOGFILE="./Log/$logname$DATE.log"
echo " "
echo "Run the coil powering: coil-energization.sif" | tee $LOGFILE
rm ./RESU/coil_* | tee -a $LOGFILE
echo "*** ElmerSolver ***"
ElmerSolver coil-energization.sif | tee -a $LOGFILE
python ./Python/plot_ramp1.py | tee -a $LOGFILE
python ./Python/plot_ramp2.py | tee -a $LOGFILE
eog ./Python/ramp1.png ./Python/ramp2.png &
echo "Run the coil extraction: coil-extraction.sif" | tee -a $LOGFILE
ElmerSolver coil-extraction.sif | tee -a $LOGFILE
python ./Python/plot_all.py | tee -a $LOGFILE
eog ./Python/all_current.png ./Python/all_voltage.png &
