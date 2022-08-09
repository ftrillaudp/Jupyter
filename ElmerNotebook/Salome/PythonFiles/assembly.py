if isMakePartitionWanted:
    print(" *** Partition ***")
    assembly = geompy.MakePartition(listForAssembly)
else:
    print(" *** Compound ***")
    assembly = geompy.MakeCompound(listForAssembly)

# Glueing faces for meshing
if isMakeGlueFacesWanted:
    assembly = geompy.MakeGlueFaces(assembly, tolerance)


pass
