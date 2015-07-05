import sys
import os

inputfile = sys.argv[1]
directory = "/".join(x for x in inputfile.split("/")[:-1])
filename = inputfile.split("/")[-1]
outputdir = directory+"/perline-"+filename

try:
  os.mkdir(outputdir)
except OSError,e:
  if e.errno == 17:
    pass # No need to recreate the directory

handle = open(inputfile)
data = handle.readlines()
handle.close()

data = [x.replace("\n","") for x in data]

for (x,y) in enumerate(data):
  handle = open("%s/%d" % (outputdir, x), "w")
  handle.write(y)
  handle.close()
