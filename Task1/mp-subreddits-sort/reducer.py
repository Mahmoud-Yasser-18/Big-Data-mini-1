#!/usr/bin/python3

import sys
import bisect
word = None
count = 0
top_records=[]
for line in sys.stdin:
    try:
        key, value = line.strip().split(sep='\t')
        value=int(value)
    except:
        continue
    try:
        if value > top_records[0][0]:
            top_records.append((value,key))
            top_records=sorted(top_records)[-10:]
    except:
        top_records.append((value,key))

for record in top_records:
    print(record[1],record[0],sep='\t')
