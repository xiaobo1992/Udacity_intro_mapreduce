#!/usr/bin/python

import sys

for line in sys.stdin:
	data = line.strip().split(" ")
	#print data	
	if len(data) == 10:
		IP = data[0]
		url = data[6]	
		if url.startswith("http://www.the-associates.co.uk"):
			url = url[len("http://www.the-associates.co.uk"):]	
			#print url	
		print "{0}\t{1}".format(url,1)
