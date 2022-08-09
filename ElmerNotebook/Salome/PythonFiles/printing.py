# LUMPED GEOMETRIES #
# Adding basic geometries to visualizatin tree:
planesID = geompy.addToStudy(planes, 'PlanesOXYZ')
planeVXVZID = geompy.addToStudyInFather(planes, planeVXVZ, 'planeOXZ')
planeVXVYID = geompy.addToStudyInFather(planes, planeVXVY, 'planeOXY')
planeVYVZID = geompy.addToStudyInFather(planes, planeVYVZ, 'planeOYZ')
VXID = geompy.addToStudyInFather(planeVXVY, VX, 'VX')
VYID = geompy.addToStudyInFather(planeVXVY, VY, 'VY')
VZID = geompy.addToStudyInFather(planeVXVZ, VZ, 'VZ')

# Adding geometries to OCC Viewer:
assemblyID = geompy.addToStudy(assembly, 'Assembly')
gg.createAndDisplayGO(assemblyID)
gg.setDisplayMode(assemblyID, 1)

# Adding tooling
if areToolsViewWanted:
    toolsID = geompy.addToStudy(tools, 'Tools')
    print(' * Tools added')

# GROUPS #
# solid:
if areSolidGroupsWanted:
    print(' * Solids added')
    for i, value in enumerate(listOfSolidGroups):
        listOfSolidGroupIDs.append(geompy.addToStudyInFather(assembly, value, listOfSolidNumbers[i]+': '+listOfSolids[i]))
        listOfSolidGroups[i].SetColor(SALOMEDS.Color(listOfSolidColors[i][0],listOfSolidColors[i][1],listOfSolidColors[i][2]))

# Faces:
if areFaceGroupsWanted:
    if listOfFaces:
        print(' * Faces')
        for i, value in enumerate(listOfFaceGroups):
            listOfFaceGroupIDs.append(geompy.addToStudyInFather(assembly, value, listOfFaceNumbers[i]+': '+listOfFaces[i]))
            listOfFaceGroups[i].SetColor(SALOMEDS.Color(listOfFaceColors[i][0],listOfFaceColors[i][1],listOfFaceColors[i][2]))

# Edges:
if areEdgeGroupsWanted:
    print(' * Wires')
    for i, value in enumerate(listOfEdgeGroups):
        listOfEdgeGroupIDs.append(geompy.addToStudyInFather(assembly, value, listOfEdgeNumbers[i]+': '+listOfEdges[i]))
        listOfEdgeGroups[i].SetColor(SALOMEDS.Color(listOfEdgeColors[i][0],listOfEdgeColors[i][1],listOfFaceColors[i][2]))


pass
