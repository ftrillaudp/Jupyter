# Here is defined the name in the exported meshes
if areMeshGroupsWanted:
    if listOfSolids:
        print(" *** Solids: ")
        for i, value in enumerate(listOfSolidGroups):
            listOfSolidMeshGroups.append(assemblyMesh.GroupOnGeom(value, listOfSolids[i], SMESH.VOLUME))
            print(listOfSolidNumbers[i]+": "+listOfSolids[i])
    if listOfFaces:
        print(" *** Faces: ")
        for i, value in enumerate(listOfFaceGroups):
            listOfFaceMeshGroups.append(assemblyMesh.GroupOnGeom(value, listOfFaces[i], SMESH.FACE))
            print(listOfFaceNumbers[i]+": "+listOfFaces[i])
    if listOfEdges:
        print(" *** Edges: ")
        for i, value in enumerate(listOfEdgeGroups):
            listOfEdgeMeshGroups.append(assemblyMesh.GroupOnGeom(value, listOfEdges[i], SMESH.EDGE))
            print(listOfEdgeNumbers[i]+": "+listOfEdges[i])


pass
