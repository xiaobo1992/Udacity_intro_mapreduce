#!/usr/bin/python

import sys

old_id = None
list = [0]
question = 0
ans = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 3:
		continue

	id, type, length  = data_mapped
		
	if old_id != id:
		if old_id != None:
			if len(ans) > 0:
				avg = sum(ans) / float(len(ans))
				print old_id,"\t",question,"\t",avg
			else:
				print old_id,"\t",question,"\t",0
		ans = []
		question = 0
		old_id = id	
	
	if old_id == id:
		#print type == "question"
		#print len(type)
		type = type.strip()
		if type == "question":
			
			question = length
		else:
			ans.append((int)(length))
 
if old_id != None:
	if len(ans) > 0:
		avg = sum(ans) / float(len(ans))
		print old_id,"\t",question,"\t",avg
	else:
		print old_id,"\t",question,"\t",0
