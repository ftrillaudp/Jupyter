# Printing id number and corresponding geometry:
print(listOfSolidNumbers[0]+": "+listOfSolids[0])

# Volume
solid001_1 = geompy.MakeCylinderRH(coilInnerRadius, coilThickness)
solid001_2 = geompy.MakeCylinderRH(coilInnerRadius+coilWidth, coilThickness)
solid001 = geompy.MakeCut(solid001_2, solid001_1)
solid001 = geompy.MakeTranslation(solid001, 0., 0., -0.5*coilThickness)

# List of geometries
listOfSolid001 = [solid001]

listForAssembly.append(solid001)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(solid001, "view001:coil_1"))

pass
