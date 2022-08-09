import glob
import os
import sys
import pathlib

mainfileLoc = glob.glob("./**/"+sys.argv[1], recursive=True)
print(mainfileLoc[0])

basePathDirectoryName = os.path.dirname(pathlib.Path(mainfileLoc[0]).absolute())
print(basePathDirectoryName)
parentPathDirectoryName = os.path.dirname(basePathDirectoryName)
print(parentPathDirectoryName)

# current working directory
print(pathlib.Path(mainfileLoc[0]).absolute())
