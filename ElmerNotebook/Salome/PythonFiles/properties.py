for i, value in enumerate(listForAssembly[0:-1]):
    basicTemporaryProperties = geompy.BasicProperties(value)
    coordinatesOfTemporaryCenterOfMass = geompy.PointCoordinates(geompy.MakeCDG(value))
    dictionaryOfBasicProperties[listOfSolidNumbers[i]+'_'+listOfSolids[i]] = [listOfMaterials[i], floatPrecision.format(basicTemporaryProperties[1]), floatPrecision.format(basicTemporaryProperties[2]), floatPrecision.format(coordinatesOfTemporaryCenterOfMass[0]), floatPrecision.format(coordinatesOfTemporaryCenterOfMass[1]), floatPrecision.format(coordinatesOfTemporaryCenterOfMass[2])]


# Create a data file *.dat of properties
myFile003 = open(folderDict['dat']+'basicProperties.dat', 'w')
myFile003.write('###########################\n')
myFile003.write('### TABLE OF PROPERTIES ###\n')
myFile003.write('###########################\n\n')
myFile003.write('-------------------------------------------------------------------------------\n')
myFile003.write('Geometry:  Material, surface [m^2],  volume [m^3], center of mass (x, y, z) [m]\n')
myFile003.write('-------------------------------------------------------------------------------\n')
for key, value in sorted(dictionaryOfBasicProperties.items()):
    myFile003.write(key+': '+value[0]+', '+str(value[1])+', '+str(value[2])+', ('+str(value[3])+', '+str(value[4])+', '+str(value[5])+')\n')
myFile003.close()
print("*** Creation of data file: basicProperties.dat")


pass
