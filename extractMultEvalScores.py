import sys

handle = open(sys.argv[1])
data = handle.readlines()
handle.close()

extracted = []

outputFile = sys.argv[1].replace("opt1","csv") # Keep the original MultEval file
handle = open(outputFile, "w")
handle.write("id\ttext\tbleu4\tmeteor\tter\n");

for line in data:
  line = line.replace("\n", "")
  line = line.split("|||")
  num = line[0].strip()
  description = line[1].strip()

  scores = line[2] # Extract the BLEU4, Meteor, and TER scores
  scores = scores.split(" ")
  bleu4 = scores[1].split("=")[1]
  meteor = scores[2].split("=")[1]
  ter = scores[3].split("=")[1]

  handle.write("%s\t%s\t%s\t%s\t%s\n" % (num, description, bleu4, meteor, ter))

handle.close()
