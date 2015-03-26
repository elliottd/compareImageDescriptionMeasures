import sys
import os

inputfile = sys.argv[1]
directory = "/".join(x for x in inputfile.split("/")[:-1])
outputdir = directory+"/rouge-references/"

try:
  os.mkdir(outputdir)
except OSError,e:
  if e.errno == 17:
    print "Directory already existed, continuing"

handle = open(inputfile)
data = handle.readlines()
handle.close()

data = [x.replace("\n","") for x in data]

prefix = inputfile.split("/")[-1]
for (x,y) in enumerate(data):
  handle = open("%s/%s-%d" % (outputdir, prefix, x), "w")
  handle.write(y)
  handle.close()
