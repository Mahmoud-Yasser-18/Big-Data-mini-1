#!/usr/bin/python3

import sys
word = None
count_up = 0
count_down = 0
top_records_up=[]
top_records_down=[]

for line in sys.stdin:
    try:
        key, value = line.strip().split(sep='\t')
        value=abs(int(value))
    except:
        continue
    try:
        if key[:3]=="__u":
            if value > top_records_up[0][0] or len(top_records_up)<10:
                top_records_up.append((value,key))
                top_records_up=sorted(top_records_up)[-10:]
        else:
            if value > top_records_down[0][0] or len(top_records_down)<10:
                top_records_down.append((value,key))
                top_records_down=sorted(top_records_down)[-10:]


    except:
        if line.split("\t")[0][:3]=="__u":
            top_records_up.append((value,key))
        else:
            top_records_down.append((value,key))

for record in top_records_up:
    print(record[1],record[0],sep='\t')

for record in top_records_down:
    print(record[1],record[0],sep='\t')
