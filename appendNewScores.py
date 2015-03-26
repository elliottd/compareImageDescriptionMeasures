import sys
import re
import os

newFile = sys.argv[1]
label = sys.argv[2]
existingFile = sys.argv[3]

newScores = open(newFile).readlines()
newScores = [x.replace("\n", "") for x in newScores]

handle = open(existingFile)
existingData = handle.readlines()
handle.close()

existingData = [x.replace("\n","") for x in existingData]

handle = open(existingFile, "w")

header = existingData[0]
header = header.replace("\n","")
header = "%s\t%s\n" % (header, label)
handle.write(header)

existingData = existingData[1:]

for (i,line) in enumerate(existingData):
  line += "\t"+str(newScores[i])+"\n"
  handle.write(line)

handle.close()

