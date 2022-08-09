# AUTHOR: Frederic Trillaud <ftrillaudp@gmail.com>
# UNIVERSITY: UNAM
# DATE (english): 08/08/2022


# INCLUDE
# Salome:
import salome
import GEOM
import SMESH
from salome.smesh import smeshBuilder
smesh = smeshBuilder.New()
from salome.StdMeshers import StdMeshersBuilder
from salome.geom import geomBuilder
geompy = geomBuilder.New()
import StdMeshers
import NETGENPlugin
import SALOMEDS
import iparameters
import salome_notebook
import MEDLoader
import SALOMEDS

# Python:
import os
import glob
import pathlib
import sys
import re
import shutil
import subprocess
import numpy as np
import scipy as sp
import math
from datetime import date


# UDF #
def varname(var, dir=locals()):
    return [key for key, val in dir.items() if id(val) == id(var)][0]

# CURRENT AND PARENT DIRECTORIES #
basePathDirectoryName = os.path.dirname(os.path.realpath(sys.argv[0]))
parentPathDirectoryName = os.path.dirname(basePathDirectoryName)
# If run from GUI, a change is required:
result = basePathDirectoryName.find('PythonFiles')
if (result == -1):
    parentPathDirectoryName = basePathDirectoryName
    basePathDirectoryName = basePathDirectoryName+'/PythonFiles'


# INITIALIZATION OF PARAMETERS #
print(' ')
print('### Initialization of parameters ###')
exec(open(basePathDirectoryName+'/parameters.py').read())
print('### Automatic data ###')
exec(open(basePathDirectoryName+'/automatic.py').read())
print(' ')


# MAIN #
if runTools:
    print('### Tools ###')
    exec(open(basePathDirectoryName+'/tools.py').read())
print(' ')

if runGeometries:
    print('### Geometrical models ###')
    for i, value in enumerate(listOfSolids):
        exec(open(basePathDirectoryName+'/solid'+'{0:03d}'.format(i+1)+'_'+value+'.py').read())
print(' ')

if runAssembly:
    exec(open(basePathDirectoryName+'/assembly.py').read())
    exec(open(basePathDirectoryName+'/properties.py').read())
print(' ')

if runVisualization:
    print('### Geometrical groups ###')
    exec(open(basePathDirectoryName+'/geometricGroups.py').read())
    print('### Visualization ###')
    exec(open(basePathDirectoryName+'/printing.py').read())
print(' ')

if runMeshing:
    print('### Meshes ###')
    exec(open(basePathDirectoryName+'/meshes.py').read())
    print('### Mesh groups ###')
    exec(open(basePathDirectoryName+'/meshGroups.py').read())
    print('### Exporting mesh files ###')
    exec(open(basePathDirectoryName+'/exportMeshes.py').read())
print(' ')


# SAVE #
currentStudy = salome.myStudy
name_tmp = folderDict['hdf']+GlobalFileName+'.hdf'
salome.myStudy.SaveAs(name_tmp, currentStudy, False)
geompy.init_geom()


pass
