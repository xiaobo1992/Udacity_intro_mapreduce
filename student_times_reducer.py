#!/usr/bin/python

import sys

old_id = None
list = [0]

def most_occurance(list):
	occur = dict()
	for item in list:
		if item not in occur.keys():
			occur[item] = 1
		else:
			occur[item] += 1
	count = 0
	for key in occur:
		if occur[key] > count:
			count = occur[key]

	c = []
	for key in occur:
		if occur[key] == count:
			c.append(key)

	return c


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	author_id, hour = data_mapped
		
	if old_id != author_id:
		if old_id != None:
			l = most_occurance(list)
			for key in l:
				print old_id,"\t",key
		
		list = []
		old_id = author_id
	
	if old_id == author_id:
		list.append(hour)
 
if old_id != None:
	l = most_occurance(list)
	for key in l:
		print old_id,"\t",key
