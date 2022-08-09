# Printing id number and corresponding geometry:
print(listOfSolidNumbers[len(listForAssembly)]+": "+listOfSolids[len(listForAssembly)])

# Vertexes
vertex001 = geompy.MakeVertex(0., 0., -1.5*coilThickness)
vertex002 = geompy.MakeVertex(0., 0., 1.5*coilThickness)

# Edges
edge001 = geompy.MakeEdge(vertex001, vertex002)

# Volume
solid002 = geompy.MakeSphereR(airRadius)
solid002 = geompy.MakeCut(solid002, geompy.MakeCompound(listForAssembly))


# List of geometries #
listOfsolid002 = [solid002, edge001]
listForAssembly.append(solid002)
listForAssembly.append(edge001)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid002, "view002: air"))


pass
