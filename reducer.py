#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None
highestSale = 0
count = 0
num_of_sales = 0
total_values = 0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey != thisKey:
        #print oldKey, "\t", salesTotal
	print oldKey,"\t",highestSale
	#print oldKey,"\t",count
	oldKey = thisKey
	#list = []
	#num_of_sales += count
        #total_values += salesTotal
	#count = 0
	highestSale = 0
	#salesTotal = 0
	
    
    if oldKey == thisKey:
	#list.append(thisSale)
	#print thisSale, highestSale, float(thisSale) > highestSale
	if float(thisSale) > highestSale:
		#print oldKey,"\t",highestSale,thisSale,thisSale > highestSale
		highestSale = float(thisSale)
	#print oldKey,"\t",highestSale,"\t",thisSale    
    #oldKey = thisKey
    #salesTotal += float(thisSale)

if oldKey != None:
    #print oldKey, "\t", salesTotal
    print oldKey,"\t",highestSale
    #print oldKey,"\t",count
    #num_of_sales += count
    #total_values += salesTotal

#print num_of_sales,"\t",total_values
