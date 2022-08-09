# Grouping tools #
listOfTools = []
tools = geompy.MakeCompound(listOfTools)


# Visualization #
if isIntermediateSolidViewWanted:
    gg.createAndDisplayGO(geompy.addToStudy(tools, "viewTool"))


pass
