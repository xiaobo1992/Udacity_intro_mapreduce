#!/usr/bin/python

import sys
import operator

old_id = None
res = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	id, value  = data_mapped
		
	if old_id != id:
		if old_id != None:
			#res[old_id] = count
			print old_id,"\t",res
		res = []
		res.append(value)
		old_id = id	
	elif old_id == id:
		res.append(value)
 
if old_id != None:
	#res[old_id] = count
	print old_id,"\t",res
