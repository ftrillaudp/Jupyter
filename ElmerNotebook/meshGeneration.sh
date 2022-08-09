#!/bin/bash

#!/bin/bash

#Get salome. The user gives the absolute path to salome bin file
salome="/opt/SALOME-9.9.0-native-UB20.04-SRC/binsalome"
namef=$(find ./ -type f -name "main.py")
echo $namef
pathf=$(readlink -f $namef)

#Run salome to generate the *.unv file (mesh)
$salome -t $pathf

#Get the *.unv file and copy it in the local directory
name=$(find ./ -type f -name "assembly.unv")
cp -v $name .
#Get the geometric parameters to be used by Elmer solver
namedat=$(find ./ -type f -name "dataElmer.dat")
cp -v $namedat .

#remove the extension
filename=$(basename $name | cut -d. -f1)

#Clean the mesh folder and genrrate a new mesh for Elmer
rm -r ./MESH; ElmerGrid 8 2 $filename.unv -out MESH -autoclean -timer
#To visualize the mesh in gmsh format
ElmerGrid 2 4 MESH -out $filename.msh
