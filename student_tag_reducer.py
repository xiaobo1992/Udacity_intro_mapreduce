#!/usr/bin/python

import sys
import operator

old_id = None
count = 0
question = 0
res = dict()

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	id, value  = data_mapped
		
	if old_id != id:
		if old_id != None:
			res[old_id] = count
			#print old_id,"\t",count
		count = 1
		old_id = id	
	elif old_id == id:
		count += 1
 
if old_id != None:
	res[old_id] = count
	#print old_id,"\t",count

sort_res = sorted(res.items(),key = operator.itemgetter(1),reverse =True)

i = 0
for item in sort_res:
	if i == 10:
		break
	print item[0],"\t",item[1]
	i += 1
