#! /bin/bash

echo "Removing old log files:"
rm -v ./Log/*

# add a log file
echo "New log file handling:"
if [ "$#" == "0" ]
then
	echo "No log generated. To get a log file, run: ./main.sh log_name" | tee $LOGFILE
	logname=""
else
	echo "Log file name set to $1. It is stored in ./Log folder" | tee $LOGFILE
	logname="$1-"
fi

DATE=$(date +%s)
LOGFILE="./Log/$logname$DATE.log"

### Variables ###
echo "Get geometrical data provided by Salome model:" | tee $LOGFILE
name1=$(find ./Salome -type f -name "dataElmer.dat")
cp -v $name1 . | tee -a $LOGFILE

# name2=$(find ./Salome -type f -name "assembly.unv")
# echo $name2
# cp -v $name2 . | tee -a $LOGFILE
# ### remove the extension for multiple purposes
# filename=$(basename $name2 | cut -d. -f1)
# echo $filename

# echo " "
# echo "*** Conversion mesh: *.unv to *.mesh ***"
# rm -r ./MESH | tee -a $LOGFILE
# ElmerGrid 8 2 $filename.unv -out MESH | tee -a $LOGFILE
# # -autoclean
# # ElmerGrid 8 2 $filename.unv -out MESH -partdual -metiskway 4 | tee -a $LOGFILE
# # -autoclean
# # ElmerGrid 14 2 $filename.msh -out MESH | tee -a $LOGFILE
# # -autoclean
#
# # To see a mesh in gmsh format
# ElmerGrid 2 4 MESH -out mesh.msh | tee -a $LOGFILE

echo " "
echo "*** COMPILATION OF UDF (FORTRAN90) ***" | tee $LOGFILE
cd ./Fortran90
echo "  *** COMPILATION: dissipation.f90 ***" | tee $LOGFILE
elmerf90 -o dissipation.so dissipation.F90 | tee $LOGFILE
echo "  *** DONE ***"
echo "  *** COMPILATION: therConductivity.f90 ***" | tee $LOGFILE
elmerf90 -o therConductivity.so therConductivity.F90 | tee $LOGFILE
echo "  *** DONE ***"
echo "  *** COMPILATION: regularization.f90 ***" | tee $LOGFILE
elmerf90 -o regularization.so regularization.F90 | tee $LOGFILE
echo "  *** DONE ***"
echo "  *** COMPILATION: electricalConductivity.f90 ***" | tee $LOGFILE
elmerf90 -o electricalConductivity.so electricalConductivity.F90 | tee $LOGFILE
echo "  *** DONE ***"
echo "  *** COMPILATION: checkMeshSize.f90 ***" | tee $LOGFILE
elmerf90 -o checkMeshSize.so checkMeshSize.F90 | tee $LOGFILE
echo "  *** DONE ***"
cd ..

echo " "
echo "*** ELMERSOLVER ***"
echo "*** Cleaning past results" | tee $LOGFILE
rm -v ./RESU/coil_* | tee -a $LOGFILE
echo "*** Run the coil powering: coil-energization.sif" | tee $LOGFILE
ElmerSolver coil-energization.sif | tee -a $LOGFILE
#mpirun -np 4 coil-energization.sif | tee -a $LOGFILE
echo "Run the coil extraction: coil-extraction.sif" | tee -a $LOGFILE
ElmerSolver coil-extraction.sif | tee -a $LOGFILE
#mpirun -np 4 coil-extraction.sif | tee -a $LOGFILE
