# Solids:
if areSolidGroupsWanted:
    print(' *** Solids: ')
    for i in range(0, len(listOfSolids)):
        listOfSolidGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['SOLID']))
    k = 0
    # SOL001: coil 11
    listOfTemporarySolidIDs = [2]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])
    # SOL003: air
    k = k+1
    listOfTemporarySolidIDs = [24]
    for j, v in enumerate(listOfTemporarySolidIDs):
        geompy.AddObject(listOfSolidGroups[k], v)
    print(listOfSolidNumbers[k]+': '+listOfSolids[k])

# Faces:
if areFaceGroupsWanted:
    print(' *** Faces:')
    if listOfFaces:
        for i in range(0, len(listOfFaces)):
            listOfFaceGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['FACE']))
        k = 0
        # FAC008: air boundary
        listOfTemporaryFaceIDs_air = [26]
        for j, v in enumerate(listOfTemporaryFaceIDs_air):
            geompy.AddObject(listOfFaceGroups[k], v)
        print(listOfFaceNumbers[k]+': '+listOfFaces[k])

# Edges:
if areEdgeGroupsWanted:
    print(' *** Edges:')
    if listOfEdges:
        for i in range(0, len(listOfEdges)):
            listOfEdgeGroups.append(geompy.CreateGroup(assembly, geompy.ShapeType['EDGE']))
        k = 0
        # EDG001: axis
        listOfTemporaryEdgeIDs_axis = [34]
        for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
            geompy.AddObject(listOfEdgeGroups[k], v)
        print(listOfEdgeNumbers[k]+': '+listOfEdges[k])

# Submesh:
if areSubmeshGroupsWanted:
    print(' *** Submeshed solids: coils')
    submeshSolidGroup = geompy.CreateGroup(assembly, geompy.ShapeType['SOLID'])
    geompy.UnionList(submeshSolidGroup, listOfSolidGroups[0:numberOfCoils])

    print(' *** Submeshed faces: air boundary')
    submeshFaceGroup = geompy.CreateGroup(assembly, geompy.ShapeType['FACE'])
    for j, v in enumerate(listOfTemporaryFaceIDs_air):
        geompy.AddObject(submeshFaceGroup, v)

    print(' *** Submeshed edges: axis')
    submeshEdgeGroup = geompy.CreateGroup(assembly, geompy.ShapeType['EDGE'])
    for j, v in enumerate(listOfTemporaryEdgeIDs_axis):
        geompy.AddObject(submeshEdgeGroup, v)


pass
