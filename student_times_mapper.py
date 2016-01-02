#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin,delimiter="\t")
i = 0;
for line in reader:
	
	if i == 0:
		#print line,len(line)
		i += 1
	else:
		id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
		added_at = (int)(added_at[11:13])
		print author_id,"\t", added_at
		#print id,"\t",node_type,"\t",parent_id,len(body)
