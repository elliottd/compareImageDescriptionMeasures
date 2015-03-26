import json

candidates = open("candidates").readlines()
judgements = open("judgements").readlines()

#jsonout = []
#
#for c,j in zip(candidates,judgements[1:]):
#  c = c.replace("\n","")
#  imageid = j.split(",")[4]
#  imageid = imageid.replace('"',"")
#  jsonout.append({"image_id": imageid, "caption": c})

jsonout = []
for x in range(0,5):

  refs = open("ref-%d" % x).readlines()
  
  
  for c,j in zip(refs,judgements[1:]):
    c = c.replace("\n","")
    imageid = j.split(",")[4]
    imageid = imageid.replace('"',"")
    jsonout.append({"image_id": imageid, "caption": c})

print json.dumps(jsonout)
