import sys
import re
import os
import glob

rougeoutput = glob.glob("ROUGE_result/[0-9]*")
rougeoutput = [x.replace("ROUGE_result/","") for x in rougeoutput]
rougeoutput.sort(key=int)

output = open("ROUGE_result/rougeScores", "w")

for f in rougeoutput:
  ROUGE_output_file = open("ROUGE_result/"+f)

  ROUGE_output_file.seek(0)
  for line in ROUGE_output_file:
    match = re.findall('X ROUGE-SU4 Average_R: ([0-9.]+)',line)
    if match != []:
      output.write("%f\n" % float(match[0])) # Multiply by 100 : range [0,100]
  ROUGE_output_file.close()

output.close()
