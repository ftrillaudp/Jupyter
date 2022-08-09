# OCC VIEWER #
# Initialize Salome:
salome.salome_init(0)
# Initialization of the tree view
gg = salome.ImportComponentGUI('GEOM')
# Visual parameters
ipar_tmp = salome.myStudy.GetCommonParameters('Interface Applicative', 1)
ipar = iparameters.IParameters(ipar_tmp, True)
# Visual properties:
# VTKViewer:
ipar.setProperty('AP_ACTIVE_VIEW', 'VTKViewer_0_0')
ipar.append('AP_MODULES_LIST', 'Mesh')
# OCC viewer:
ipar.setProperty('AP_ACTIVE_VIEW', 'OCCViewer_0_0')
ipar.setProperty('AP_ACTIVE_MODULE', 'Geometry')
# State of the GUI interface:
ipar.setProperty('AP_SAVEPOINT_NAME', 'State: 1')


# PATH #
if not folderDict:
    folderDict = {
        'hdf': parentPathDirectoryName+'/HdfFiles',
        'dat': parentPathDirectoryName+'/DataFiles',
        'med': parentPathDirectoryName+'/MedFiles',
        'unv': parentPathDirectoryName+'/UnvFiles',
        'vtk': parentPathDirectoryName+'/VtkFiles',
        'stl': parentPathDirectoryName+'/StlFiles',
        'step': parentPathDirectoryName+'/StepFiles',
        'brep': parentPathDirectoryName+'/BrepFiles',
        'iges': parentPathDirectoryName+'/IgesFiles',
        'cgns': parentPathDirectoryName+'/CgnsFiles',
        'sauv': parentPathDirectoryName+'/SauvFiles',
        'external': parentPathDirectoryName+'/ExternalFiles',
    }
if not listOfExtentions:
    listOfExtentions = list(folderDict.keys())[0:-1]

listOfFolders = list(folderDict.values())
# Creation of folders if missing
for i, value in enumerate(listOfFolders):
    checkFolder = os.path.exists(value)
    if checkFolder:
        print('Folder '+value+' already exists.')
    else:
        os.makedirs(value)
        print('created folder: ', value)



# GEOMETRIES #
# Solids:
listOfSolids = list(solidDict)
listOfMaterials = list(map(lambda x: x[0], list(solidDict.values())))
listOfSolidColors = list(map(lambda x: x[1], list(solidDict.values())))
listOfSolidGroups = list()
listOfSolidGroupIDs = list()
listOfSolidMeshGroups = list()
listForAssembly = list()
listOfSolidNumbers = list()
for i in range(0, len(listOfSolids)):
    listOfSolidNumbers.append('S'+'{0:03d}'.format(i+1))

# Faces:
listOfFaces = list(faceDict.keys())
listOfFaceColors = list(faceDict.values())
listOfFaceGroups = list()
listOfFaceGroupIDs = list()
listOfFaceMeshGroups = list()
listOfFaceNumbers = list()
for i in range(0, len(listOfFaces)):
    listOfFaceNumbers.append('F'+'{0:03d}'.format(i+1))

#  Edges:
listOfEdges = list(edgeDict.keys())
listOfEdgeColors = list(edgeDict.values())
listOfEdgeGroups = list()
listOfEdgeGroupIDs = list()
listOfEdgeMeshes = list()
listOfEdgeMeshGroups = list()
listOfEdgeNumbers = list()
for i in range(0, len(listOfEdges)):
    listOfEdgeNumbers.append('E'+'{0:03d}'.format(i+1))



# GEOMETRY PROPERTIES
dictionaryOfBasicProperties = dict()
# define the precision of the float to be printed out.
floatPrecision = '{0:.3g}'


# NOTEBOOK
notebook = salome_notebook.notebook
for i, value in enumerate(listOfParameterValues):
    notebook.set(varname(listOfParameterValues[i]), value)

pass
# DATA FILE
# Create a data files. Automatically generated from definition of parameters.
# File listing parameters for Gmsh ###
myFile001 = open(folderDict['dat']+'dataGmsh.dat', 'w')
for i, value in enumerate(listOfParameterValues):
    myFile001.write(varname(listOfParameterValues[i])+' = '+str(value)+';\n')
myFile001.close()
print('* Creation of data file: dataGmsh.par')

# File listing parameters for Elmer
myFile002 = open(folderDict['dat']+'dataElmer.dat', 'w')
for i, value in enumerate(listOfParameterValues):
    myFile002.write('$ '+varname(listOfParameterValues[i])+' = '+str(value)+'\n')
    #myFile002.write('# '+varname(listOfParameterValues[i])+' = '+str(value)+'\n')
myFile002.close()
print('* Creation of data file: dataElmer.par')

# Creation of readMe.txt file, listing the geometries and the corresponding material
myFile003 = open(folderDict['dat']+'readMe.txt', 'w')
myFile003.write('********************\n')
myFile003.write('*** SALOME MODEL ***\n')
myFile003.write('********************\n\n')
myFile003.write('*** AUTHOR: Frederic Trillaud\n')
myFile003.write('*** DATE: '+str(date.today())+'\n\n')
myFile003.write('*** Solids ***\n')
for i, v in enumerate(listOfSolids):
    myFile003.write(listOfSolids[i]+', material: '+listOfMaterials[i]+'\n')
myFile003.write('\n*** Faces ***\n')
for i, v in enumerate(listOfFaces):
    myFile003.write(listOfFaces[i]+'\n')
myFile003.write('\n*** Edges ***\n')
for i, v in enumerate(listOfEdges):
    myFile003.write(listOfEdges[i]+'\n')
myFile003.close()
print('* Creation of information file: readMe.txt')


# BASIC GEOMETRIES
# Origin:
OOO = geompy.MakeVertex(0, 0, 0)

# Main coordinates (Cartesian)
VX = geompy.MakeVectorDXDYDZ(1, 0, 0)
VY = geompy.MakeVectorDXDYDZ(0, 1, 0)
VZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

# Basic planes:
planeVXVZ = geompy.MakePlane2Vec(VX, VY, 1)
planeVYVZ = geompy.MakePlane2Vec(VY, VX, 1)
planeVXVY = geompy.MakePlane2Vec(VX, VZ, 1)
planes = geompy.MakeCompound([planeVXVY, planeVXVZ, planeVYVZ])


pass
