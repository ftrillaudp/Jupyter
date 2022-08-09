print(" *** Solid mesh (3D):")
assemblyMesh = smesh.Mesh(assembly, "Assembly")

# 1D2D3D algorithm:
NETGEN_1D_2D_3D_1 = assemblyMesh.Tetrahedron(algo = smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Parameters_1 = smesh.CreateHypothesis('NETGEN_Parameters', 'NETGENEngine')
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetMaxSize( 0.1 )
NETGEN_3D_Parameters_1.SetMinSize( 0.0005 )
NETGEN_3D_Parameters_1.SetSecondOrder( 0 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 3 )
NETGEN_3D_Parameters_1.SetChordalError( 0.1 )
NETGEN_3D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_3D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_3D_Parameters_1.SetFuseEdges( 1 )
NETGEN_3D_Parameters_1.SetQuadAllowed( 0 )
# Local size: (it does not work in script, falling back to submesh generation)
# NETGEN_3D_Parameters_1.SetLocalSizeOnShape(submeshFaceGroup, 0.2)
# Local size and submeshes:
if areSubmeshGroupsWanted:
    # 1D submesh of edges:
    Regular_1D = assemblyMesh.Segment(geom=submeshEdgeGroup)
    Number_of_Segments_1 = Regular_1D.NumberOfSegments(200)
    # 2D submesh of faces:
    NETGEN_1D_2D_1 = assemblyMesh.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=submeshFaceGroup)
    NETGEN_2D_Parameters_1 = NETGEN_1D_2D_1.Parameters()
    NETGEN_2D_Parameters_1.SetMaxSize( 0.12 )
    NETGEN_2D_Parameters_1.SetMinSize( 0.0005)
    NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
    NETGEN_2D_Parameters_1.SetOptimize( 1 )
    NETGEN_2D_Parameters_1.SetFineness( 2 )
    NETGEN_2D_Parameters_1.SetChordalError( 0.1 )
    NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
    NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
    NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
    NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
    # 3D submesh of solids:
    NETGEN_1D_2D_3D_2 = assemblyMesh.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D, geom=submeshSolidGroup)
    NETGEN_3D_Parameters_2 = NETGEN_1D_2D_3D_2.Parameters()
    NETGEN_3D_Parameters_2.SetMaxSize( 0.01 )
    NETGEN_3D_Parameters_2.SetMinSize( 0.0005 )
    NETGEN_3D_Parameters_2.SetSecondOrder( 0 )
    NETGEN_3D_Parameters_2.SetOptimize( 1 )
    NETGEN_3D_Parameters_2.SetFineness( 3 )
    NETGEN_3D_Parameters_2.SetChordalError( 0.1 )
    NETGEN_3D_Parameters_2.SetChordalErrorEnabled( 0 )
    NETGEN_3D_Parameters_2.SetUseSurfaceCurvature( 1 )
    NETGEN_3D_Parameters_2.SetFuseEdges( 1 )
    NETGEN_3D_Parameters_2.SetQuadAllowed( 0 )
    # Set names of Mesh objects
    smesh.SetName(NETGEN_1D_2D_3D_1.GetSubMesh(), 'Submeshed solids')
    smesh.SetName(NETGEN_1D_2D_1.GetSubMesh(), 'Submeshed faces')
    smesh.SetName(NETGEN_2D_Parameters_1, 'Submesh Parameters (2D)')
    smesh.SetName(NETGEN_3D_Parameters_2, 'Submesh Parameters (3D)')

isDone_a = assemblyMesh.Compute()

# Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D_1.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(assemblyMesh.GetMesh(), 'Meshed assembly')
smesh.SetName(NETGEN_3D_Parameters_1, 'Mesh Parameters')




pass
