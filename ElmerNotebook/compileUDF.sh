#! /bin/bash

echo "*** COMPILATION OF UDF (FORTRAN90) ***"
cd ./Fortran90
echo "  *** COMPILATION: dissipation.f90"
elmerf90 -o dissipation.so dissipation.F90
echo "  *** DONE ***"
echo "  *** COMPILATION: therConductivity.f90"
elmerf90 -o therConductivity.so therConductivity.F90
echo "  *** DONE ***"
echo "  *** COMPILATION: regularization.f90"
elmerf90 -o regularization.so regularization.F90
echo "  *** DONE ***"
echo "  *** COMPILATION: electricalConductivity.f90"
elmerf90 -o electricalConductivity.so electricalConductivity.F90
echo "  *** DONE ***"
echo "  *** COMPILATION: checkMeshSize.f90"
elmerf90 -o checkMeshSize.so checkMeshSize.F90
echo "  *** DONE ***"
cd ..
