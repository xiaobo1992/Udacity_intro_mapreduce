#!/usr/bin/python

import sys

count = 0
oldKey = None
highestKey = None
highestHit = 0
for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue
	thisKey, thisValue = data_mapped
	
	if oldKey != thisKey:
		#print oldKey,"\t",count
		if count > highestHit:
			highestKey = oldKey
			highestHit = count
		oldKey = thisKey
		count = 0
	
	if oldKey == thisKey:
		count += 1

if oldKey != None:
	if count > highestHit:
		highestKey = oldKey
		highestHit = count
	#print oldKey,"\t",count
print highestKey,"\t",highestHit
